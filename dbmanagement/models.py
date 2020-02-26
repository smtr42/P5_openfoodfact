class Product:
    def __init__(self, barcode, product_name, nutriscore, url, *args, **kwargs):
        self.barcode = barcode
        self.product_name = product_name
        self.nutriscore = nutriscore
        self.url = url