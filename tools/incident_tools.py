from langchain_core.tools import tool

from services.incident_service import IncidentService


incident_service = IncidentService()



@tool
def create_incident(
    shipment_id: str,
    severity: str,
    description: str
):
    """
    Create a new supply chain incident.
    """

    return incident_service.create_incident(
        shipment_id,
        severity,
        description
    )



@tool
def check_incident_status(incident_id: str):
    """
    Check current incident status.
    """

    return incident_service.check_status(
        incident_id
    )



@tool
def escalate_incident(incident_id: str):
    """
    Escalate an incident to critical level.
    """

    return incident_service.escalate_incident(
        incident_id
    )