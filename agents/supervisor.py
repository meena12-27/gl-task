from utils.llm import get_llm

from agents.shipment_agent import create_shipment_agent
from agents.inventory_agent import create_inventory_agent
from agents.supplier_agent import create_supplier_agent
from agents.recovery_agent import create_recovery_agent
from agents.reporting_agent import create_reporting_agent



def create_supervisor():


    llm = get_llm()


    shipment_agent = create_shipment_agent()
    inventory_agent = create_inventory_agent()
    supplier_agent = create_supplier_agent()
    recovery_agent = create_recovery_agent()
    reporting_agent = create_reporting_agent()



    agents = {

        "shipment": shipment_agent,
        "inventory": inventory_agent,
        "supplier": supplier_agent,
        "recovery": recovery_agent,
        "reporting": reporting_agent

    }


    return agents