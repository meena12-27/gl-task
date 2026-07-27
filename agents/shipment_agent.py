from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from prompts.shipment_prompt import SHIPMENT_SYSTEM_PROMPT
from utils.llm import get_llm


from tools.shipment_tools import (
    track_shipment,
    check_shipment_delay,
    find_affected_orders,
    check_route_status,
     get_shipment_destination
)



def create_shipment_agent():


    llm = get_llm()


    tools = [

        track_shipment,
        check_shipment_delay,
        find_affected_orders,
        check_route_status,
         get_shipment_destination

    ]


    prompt = ChatPromptTemplate.from_messages(
        [

            (
            "system",
            SHIPMENT_SYSTEM_PROMPT
            
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