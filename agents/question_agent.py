class QuestionGeneratorAgent:
    def generate(self, product: dict) -> dict:
        return {
            "informational": [
                f"What is {product['name']}?",
                "What does Vitamin C do for skin?"
            ],
            "usage": [
                "How often should this serum be used?",
                "Can it be used before sunscreen?"
            ],
            "safety": [
                "Is mild tingling normal?",
                "Who should avoid this serum?"
            ],
            "purchase": [
                "What is the price?",
                "Is it suitable for oily skin?"
            ]
        }
