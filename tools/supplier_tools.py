from langchain_core.tools import tool

from services.supplier_service import SupplierService


supplier_service = SupplierService()



@tool
def search_supplier(supplier_id: str):
    """
    Find supplier details.
    """

    return supplier_service.supplier_details(
        supplier_id
    )



@tool
def check_supplier_availability(supplier_id: str):
    """
    Check supplier availability status.
    """

    return supplier_service.check_supplier_availability(
        supplier_id
    )



@tool
def find_alternative_supplier(product_id: str):
    """
    Find alternative suppliers for a product.
    """

    return supplier_service.find_alternative_suppliers(
        product_id
    )