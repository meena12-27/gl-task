from services.data_loader import DataLoader


class InventoryService:

    def __init__(self):

        self.loader = DataLoader()

        self.inventory = self.loader.get_inventory()
        self.products = self.loader.get_products()
        self.warehouses = self.loader.get_warehouses()



    def check_product_inventory(self, product_id):

        results = []

        for item in self.inventory:

            if item["product_id"] == product_id:

                results.append(item)


        return results



    def get_available_stock(self, product_id):

        stock = 0


        for item in self.inventory:

            if item["product_id"] == product_id:

                stock += item["available_quantity"]


        return stock



    def check_shortage(self, product_id):

        product = None

        for p in self.products:

            if p["product_id"] == product_id:
                product = p


        if not product:
            return "Product not found"



        stock = self.get_available_stock(product_id)


        if stock < product["reorder_level"]:

            return {
                "shortage": True,
                "available": stock,
                "required": product["reorder_level"]
            }


        return {
            "shortage": False,
            "available": stock
        }



    def warehouse_stock(self, warehouse_id):

        result = []

        for item in self.inventory:

            if item["warehouse_id"] == warehouse_id:

                result.append(item)


        return result