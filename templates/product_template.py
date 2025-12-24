class ProductPageTemplateAgent:
    def assemble(self, product: dict) -> dict:
        return {
            "page_type": "product",
            "name": product["name"],
            "concentration": product["concentration"],
            "skin_type": product["skin_type"],
            "ingredients": product["ingredients"],
            "benefits": product["benefits"],
            "usage": product["usage"],
            "side_effects": product["side_effects"],
            "price": product["price"]
        }
