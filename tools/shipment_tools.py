from langchain_core.tools import tool

from services.shipment_service import ShipmentService


shipment_service = ShipmentService()


@tool
def track_shipment(shipment_id: str):
    """
    Track shipment status, location and ETA.
    """

    return shipment_service.track_shipment(shipment_id)

@tool
def get_shipment_destination(shipment_id: str):
    """
    Find shipment destination using route information.
    """

    return shipment_service.get_destination(
        shipment_id
    )

@tool
def check_shipment_delay(shipment_id: str):
    """
    Check if shipment is delayed.
    """

    return shipment_service.check_delay(shipment_id)



@tool
def find_affected_orders(shipment_id: str):
    """
    Find customer orders affected by shipment issues.
    """

    return shipment_service.get_affected_orders(shipment_id)



@tool
def check_route_status(route_id: str):
    """
    Check route information and status.
    """

    return shipment_service.get_route_status(route_id)