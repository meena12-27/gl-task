from tools.shipment_tools import (
    track_shipment,
    check_shipment_delay,
    find_affected_orders,
    check_route_status
)


print("\n--- TRACK SHIPMENT ---")

result = track_shipment.invoke(
    {
        "shipment_id": "SH002"
    }
)

print(result)



print("\n--- CHECK DELAY ---")

result = check_shipment_delay.invoke(
    {
        "shipment_id": "SH002"
    }
)

print(result)



print("\n--- AFFECTED ORDERS ---")

result = find_affected_orders.invoke(
    {
        "shipment_id": "SH002"
    }
)

print(result)





from tools.inventory_tools import (
    check_inventory,
    get_available_stock,
    identify_inventory_shortage
)


print("\n--- INVENTORY ---")

print(
    check_inventory.invoke(
        {
            "product_id":"P001"
        }
    )
)


print(
    get_available_stock.invoke(
        {
            "product_id":"P001"
        }
    )
)


print(
    identify_inventory_shortage.invoke(
        {
            "product_id":"P001"
        }
    )
)





from tools.supplier_tools import (
    search_supplier,
    check_supplier_availability,
    find_alternative_supplier
)


print("\n--- SUPPLIER ---")


print(
    search_supplier.invoke(
        {
            "supplier_id":"SUP001"
        }
    )
)


print(
    check_supplier_availability.invoke(
        {
            "supplier_id":"SUP001"
        }
    )
)


print(
    find_alternative_supplier.invoke(
        {
            "product_id":"P001"
        }
    )
)





from tools.incident_tools import (
    create_incident,
    check_incident_status,
    escalate_incident
)


print("\n--- INCIDENT ---")


incident = create_incident.invoke(
    {
        "shipment_id":"SH002",
        "severity":"High",
        "description":"Shipment delayed for testing"
    }
)

print(incident)






from tools.recovery_tools import (
    recommend_recovery_action,
    compare_supplier_options
)


print("\n--- RECOVERY ---")


print(
    recommend_recovery_action.invoke(
        {
            "shipment_id":"SH002"
        }
    )
)


print(
    compare_supplier_options.invoke(
        {
            "product_id":"P001"
        }
    )
)






from tools.reporting_tools import (
    generate_incident_summary,
    generate_shipment_report
)


print("\n--- INCIDENT SUMMARY ---")


result = generate_incident_summary.invoke(
    {
        "incident_id": "INC001"
    }
)

print(result)



print("\n--- SHIPMENT REPORT ---")


result = generate_shipment_report.invoke(
    {
        "shipment_id": "SH002"
    }
)

print(result)