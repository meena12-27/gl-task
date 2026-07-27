import json
import os


class DataLoader:
    """
    Loads and provides access to NovaRetail mock supply chain data.
    """

    def __init__(self, data_path="data"):
        self.data_path = data_path

        self.suppliers = []
        self.products = []
        self.warehouses = []
        self.inventory = []
        self.shipments = []
        self.orders = []
        self.incidents = []
        self.routes = []

        self.load_all_data()


    def load_json(self, filename):
        """
        Generic JSON file loader.
        """

        file_path = os.path.join(self.data_path, filename)

        try:
            with open(file_path, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            print(f"Warning: {filename} not found")
            return []

        except json.JSONDecodeError:
            print(f"Error: {filename} contains invalid JSON")
            return []


    def load_all_data(self):
        """
        Loads all supply chain datasets.
        """

        self.suppliers = self.load_json("suppliers.json")

        self.products = self.load_json("products.json")

        self.warehouses = self.load_json("warehouses.json")

        self.inventory = self.load_json("inventory.json")

        self.shipments = self.load_json("shipments.json")

        self.orders = self.load_json("orders.json")

        self.incidents = self.load_json("incidents.json")

        self.routes = self.load_json("routes.json")


    def get_suppliers(self):
        return self.suppliers


    def get_products(self):
        return self.products


    def get_warehouses(self):
        return self.warehouses


    def get_inventory(self):
        return self.inventory


    def get_shipments(self):
        return self.shipments


    def get_orders(self):
        return self.orders


    def get_incidents(self):
        return self.incidents


    def get_routes(self):
        return self.routes



# Test the loader
if __name__ == "__main__":

    loader = DataLoader()

    print("Suppliers:", len(loader.get_suppliers()))
    print("Products:", len(loader.get_products()))
    print("Warehouses:", len(loader.get_warehouses()))
    print("Inventory Records:", len(loader.get_inventory()))
    print("Shipments:", len(loader.get_shipments()))
    print("Orders:", len(loader.get_orders()))
    print("Incidents:", len(loader.get_incidents()))
    print("Routes:", len(loader.get_routes()))