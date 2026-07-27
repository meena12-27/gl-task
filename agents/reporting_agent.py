from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor
)
from prompts.reporting_prompt import REPORTING_SYSTEM_PROMPT
from langchain_core.prompts import ChatPromptTemplate

from utils.llm import get_llm


from tools.reporting_tools import (
    generate_incident_summary,
    generate_shipment_report
)



def create_reporting_agent():

    llm = get_llm()


    tools = [

        generate_incident_summary,
        generate_shipment_report

    ]


    prompt = ChatPromptTemplate.from_messages(
        [

            (
"system",
REPORTING_SYSTEM_PROMPT
),

            (
    "human",
    """
Conversation History:
{history}

Current User Request:
{input}

"""),
            (
                'placeholder','{agent_scratchpad}'
            )

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