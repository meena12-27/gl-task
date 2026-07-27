from langchain_core.tools import tool

from services.inventory_service import InventoryService


inventory_service = InventoryService()



@tool
def check_inventory(product_id: str):
    """
    Check inventory availability for a product.
    """

    return inventory_service.check_product_inventory(
        product_id
    )



@tool
def get_available_stock(product_id: str):
    """
    Get total available stock across warehouses.
    """

    return inventory_service.get_available_stock(
        product_id
    )



@tool
def identify_inventory_shortage(product_id: str):
    """
    Identify if a product has inventory shortage.
    """

    return inventory_service.check_shortage(
        product_id
    )



@tool
def check_warehouse_inventory(warehouse_id: str):
    """
    Check inventory available in warehouse.
    """

    return inventory_service.warehouse_stock(
        warehouse_id
    )