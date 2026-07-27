from utils.llm import get_llm


def create_supervisor_agent():

    llm = get_llm()


    def supervisor(state):

        prompt = f"""

You are a Supply Chain Supervisor Agent.

Your job is to decide which specialist agent should handle the request.

Available agents:

shipment:
- tracking shipments
- delays
- routes
- affected orders


inventory:
- stock availability
- warehouse inventory
- shortages


supplier:
- supplier details
- supplier availability
- alternatives


recovery:
- disruptions
- recovery actions
- alternative solutions


reporting:
- reports
- summaries


User request:

{state["user_input"]}


Return only one word:

shipment
inventory
supplier
recovery
reporting

"""


        result = llm.invoke(prompt)


        state["category"] = result.content.strip().lower()


        return state


    return supervisor