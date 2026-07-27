from agents.shipment_agent import create_shipment_agent

agent=create_shipment_agent()

response=agent.invoke({
    'input':'Track shipment SH002'
})

print(response)


from agents.inventory_agent import create_inventory_agent


agent = create_inventory_agent()



response = agent.invoke(
    {
        "input":
        "Check inventory for product P001"
    }
)


print(response)


from agents.supplier_agent import create_supplier_agent


agent = create_supplier_agent()


response = agent.invoke(
    {
        "input":
        "Find alternative suppliers for product P001"
    }
)


print(response)



from agents.recovery_agent import create_recovery_agent


agent = create_recovery_agent()


response = agent.invoke(
    {
        "input":
        "Shipment SH002 is delayed. Recommend a recovery action."
    }
)


print(response)


from agents.reporting_agent import create_reporting_agent


agent = create_reporting_agent()


response = agent.invoke(
    {
        "input":
        "Generate a shipment report for SH002"
    }
)


print(response)