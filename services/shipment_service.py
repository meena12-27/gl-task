from services.data_loader import DataLoader


class ShipmentService:

    def __init__(self):
        self.loader = DataLoader()

        self.shipments = self.loader.get_shipments()
        self.orders = self.loader.get_orders()
        self.routes = self.loader.get_routes()


    def find_shipment(self, shipment_id):
        """
        Find shipment by ID
        """

        for shipment in self.shipments:
            if shipment["shipment_id"] == shipment_id:
                return shipment

        return None

    def get_destination(self, shipment_id):

        shipment = self.find_shipment(shipment_id)

        if not shipment:
            return "Shipment not found"


        route_id = shipment["route_id"]


        for route in self.routes:

            if route["route_id"] == route_id:

                return {
                    "shipment_id": shipment_id,
                    "origin": route["origin"],
                    "destination": route["destination"]
                }


        return "Route not found"
    
    def track_shipment(self, shipment_id):
        """
        Track current shipment status
        """

        shipment = self.find_shipment(shipment_id)

        if not shipment:
            return "Shipment not found"


        return {
            "shipment_id": shipment["shipment_id"],
            "status": shipment["status"],
            "current_location": shipment["current_location"],
            "eta": shipment["eta"]
        }


    def check_delay(self, shipment_id):

        shipment = self.find_shipment(shipment_id)

        if not shipment:
            return "Shipment not found"


        if shipment["delay_hours"] > 0:
            return {
                "delayed": True,
                "delay_hours": shipment["delay_hours"]
            }

        return {
            "delayed": False,
            "delay_hours": 0
        }


    def get_affected_orders(self, shipment_id):

        affected = []

        for order in self.orders:

            if order["shipment_id"] == shipment_id:
                affected.append(order)


        return affected



    def get_route_status(self, route_id):

        for route in self.routes:

            if route["route_id"] == route_id:
                return route


        return None