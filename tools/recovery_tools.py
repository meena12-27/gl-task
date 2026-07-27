from langchain_core.tools import tool

from services.recovery_service import RecoveryService


recovery_service = RecoveryService()



@tool
def recommend_recovery_action(shipment_id: str):
    """
    Recommend recovery action for disruption.
    """

    return recovery_service.recommend_action(
        shipment_id
    )



@tool
def compare_supplier_options(product_id: str):
    """
    Compare alternative suppliers.
    """

    return recovery_service.compare_suppliers(
        product_id
    )