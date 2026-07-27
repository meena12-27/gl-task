from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)
from prompts.supplier_prompt import SUPPLIER_SYSTEM_PROMPT
from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_llm


from tools.supplier_tools import (
    search_supplier,
    check_supplier_availability,
    find_alternative_supplier
)



def create_supplier_agent():

    llm = get_llm()


    tools = [

        search_supplier,
        check_supplier_availability,
        find_alternative_supplier

    ]


    prompt = ChatPromptTemplate.from_messages(
        [

            (
"system",
SUPPLIER_SYSTEM_PROMPT
),

            (
    "human",
    """
Conversation History:
{history}

Current User Request:
{input}
"""),
            ('placeholder','{agent_scratchpad}')

        ]
    )


    agent = create_tool_calling_agent(
        llm,
        tools,
        prompt
    )


    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )


    return executor