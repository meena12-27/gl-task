from langgraph.graph import StateGraph, END


from graph.state import SupplyChainState
# from graph.router import route_request
from graph.human_approval import human_approval
from agents.supervisor_agent import create_supervisor_agent

from agents.shipment_agent import create_shipment_agent
from agents.inventory_agent import create_inventory_agent
from agents.supplier_agent import create_supplier_agent
from agents.recovery_agent import create_recovery_agent
from agents.reporting_agent import create_reporting_agent



shipment_agent = create_shipment_agent()
inventory_agent = create_inventory_agent()
supplier_agent = create_supplier_agent()
recovery_agent = create_recovery_agent()
reporting_agent = create_reporting_agent()
supervisor_agent = create_supervisor_agent()


def shipment_node(state):
    print("===== HISTORY SENT TO AGENT =====")
    print(state.get("history"))

    print("===== USER INPUT =====")
    print(state["user_input"])
    result = shipment_agent.invoke(
        {
            "input":
            state["user_input"],
            "history": state.get("history", "")
        }
    )

    state["response"] = result["output"]

    return state



def inventory_node(state):

    result = inventory_agent.invoke(
        {
            "input":
            state["user_input"],
            "history": state.get("history", "")
        }
    )

    state["response"] = result["output"]

    return state



def supplier_node(state):

    result = supplier_agent.invoke(
        {
            "input":
            state["user_input"],
            "history": state.get("history", "")
        }
    )

    state["response"] = result["output"]

    return state



def recovery_node(state):

    result = recovery_agent.invoke(
        {
            "input":
            state["user_input"],
            "history": state.get("history", "")
        }
    )

    state["response"] = result["output"]

    return state



def reporting_node(state):

    result = reporting_agent.invoke(
        {
            "input":
            state["user_input"],
            "history": state.get("history", "")
        }
    )

    state["response"] = result["output"]

    return state



workflow = StateGraph(SupplyChainState)


# workflow.add_node(
#     "router",
#     route_request
# )

workflow.add_node(
    "supervisor",
    supervisor_agent
)


workflow.add_node(
    "shipment",
    shipment_node
)


workflow.add_node(
    "inventory",
    inventory_node
)


workflow.add_node(
    "supplier",
    supplier_node
)


workflow.add_node(
    "recovery",
    recovery_node
)


workflow.add_node(
    "reporting",
    reporting_node
)

workflow.add_node(
"human_approval",
human_approval
)

# workflow.set_entry_point(
#     "router"
# )

workflow.set_entry_point(
    "supervisor"
)



workflow.add_conditional_edges(

    # "router",

    "supervisor",


    lambda state: state["category"],

    {

        "shipment":"shipment",

        "inventory":"inventory",

        "supplier":"supplier",

        "recovery":"recovery",

        "reporting":"reporting"

    }

)



workflow.add_edge(
    "shipment",
    END
)

workflow.add_edge(
    "inventory",
    END
)

workflow.add_edge(
    "supplier",
    END
)

workflow.add_edge(
    "recovery",
    END
)

workflow.add_edge(
    "reporting",
    END
)

workflow.add_edge(
"recovery",
"human_approval"
)


workflow.add_edge(
"human_approval",
END
)

app = workflow.compile()