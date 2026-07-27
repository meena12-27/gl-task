from langchain_core.tools import tool

from services.shipment_service import ShipmentService
from services.incident_service import IncidentService


shipment_service = ShipmentService()
incident_service = IncidentService()



@tool
def generate_incident_summary(incident_id: str):
    """
    Generate a summary of a supply chain incident.
    """

    incident = incident_service.get_incident(
        incident_id
    )


    if not incident:
        return "Incident not found"


    return {
        "incident": incident,
        "message":
            "Incident summary generated successfully"
    }



@tool
def generate_shipment_report(shipment_id: str):
    """
    Generate shipment operational report.
    """

    shipment = shipment_service.track_shipment(
        shipment_id
    )


    orders = shipment_service.get_affected_orders(
        shipment_id
    )


    return {
        "shipment": shipment,
        "affected_orders": orders
    }