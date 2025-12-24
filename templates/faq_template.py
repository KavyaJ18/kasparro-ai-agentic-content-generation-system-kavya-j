class FAQTemplateAgent:
    def assemble(self, questions: dict, product: dict) -> dict:
        faqs = []
        for category, qs in questions.items():
            for q in qs[:5]:
                faqs.append({
                    "question": q,
                    "answer": f"This information is based on {product['name']} data."
                })

        return {
            "page_type": "faq",
            "product": product["name"],
            "items": faqs
        }
