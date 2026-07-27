from services.data_loader import DataLoader


class SupplierService:


    def __init__(self):

        self.loader = DataLoader()

        self.suppliers = self.loader.get_suppliers()
        self.products = self.loader.get_products()



    def find_supplier(self, supplier_id):

        for supplier in self.suppliers:

            if supplier["supplier_id"] == supplier_id:
                return supplier


        return None



    def supplier_details(self, supplier_id):

        supplier = self.find_supplier(supplier_id)

        if supplier:
            return supplier


        return "Supplier not found"



    def check_supplier_availability(self, supplier_id):

        supplier = self.find_supplier(supplier_id)


        if not supplier:
            return "Supplier not found"


        return {
            "supplier": supplier["name"],
            "availability": supplier["availability"]
        }



    def find_alternative_suppliers(self, product_id):

        alternatives = []


        for product in self.products:

            if product["product_id"] == product_id:

                original_supplier = product["supplier_id"]



                for supplier in self.suppliers:

                    if (
                        supplier["supplier_id"] != original_supplier
                        and supplier["availability"] == "Available"
                    ):

                        alternatives.append(supplier)



        return alternatives