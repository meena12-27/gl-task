from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)
from prompts.recovery_prompt import RECOVERY_SYSTEM_PROMPT
from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_llm


from tools.recovery_tools import (
    recommend_recovery_action,
    compare_supplier_options
)



def create_recovery_agent():

    llm = get_llm()


    tools = [

        recommend_recovery_action,
        compare_supplier_options

    ]


    prompt = ChatPromptTemplate.from_messages(
        [

           (
"system",
RECOVERY_SYSTEM_PROMPT
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