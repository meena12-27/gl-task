from services.supplier_service import SupplierService
from services.shipment_service import ShipmentService


class RecoveryService:


    def __init__(self):

        self.supplier_service = SupplierService()
        self.shipment_service = ShipmentService()



    def recommend_action(self, shipment_id):

        shipment = self.shipment_service.find_shipment(
            shipment_id
        )


        if not shipment:
            return "Shipment not found"



        if shipment["status"] == "Delayed":

            return {
                "recommendation":
                    "Find alternative supplier or reroute shipment",

                "reason":
                    "Shipment delay detected"
            }


        return {
            "recommendation":
                "Continue normal operation"
        }



    def compare_suppliers(self, product_id):

        suppliers = self.supplier_service.find_alternative_suppliers(
            product_id
        )


        return suppliers