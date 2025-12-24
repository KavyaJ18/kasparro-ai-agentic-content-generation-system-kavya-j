class ComparisonAgent:
    def build_comparison(self, product: dict) -> dict:
        fictional_product = {
            "name": "Radiant C Serum",
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "price": "₹799"
        }

        return {
            "product_a": {
                "name": product["name"],
                "ingredients": product["ingredients"],
                "benefits": product["benefits"],
                "price": product["price"]
            },
            "product_b": fictional_product
        }
