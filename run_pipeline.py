import json
from orchestrator import Orchestrator


def main():
    raw_product_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": ["Oily", "Combination"],
        "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "Benefits": ["Brightening", "Fades dark spots"],
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": "₹699"
    }

    orchestrator = Orchestrator()
    output = orchestrator.run(raw_product_data)

    with open("faq.json", "w", encoding="utf-8") as f:
        json.dump(output["faq"], f, indent=2)

    with open("product_page.json", "w", encoding="utf-8") as f:
        json.dump(output["product_page"], f, indent=2)

    with open("comparison_page.json", "w", encoding="utf-8") as f:
        json.dump(output["comparison_page"], f, indent=2)


if __name__ == "__main__":
    main()
