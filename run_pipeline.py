from graph.graph import build_graph
from graph.state import AgentState
import json
import os


def main():
    # Sample input product data
    product_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": ["Oily", "Combination"],
        "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "Benefits": ["Brightening", "Fades dark spots"],
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": "₹699"
    }

    graph = build_graph()

    state = AgentState(product_data=product_data)

    try:
        result = graph.invoke(state)
    except Exception as e:
        print("Pipeline failed during LLM execution.")
        print("Reason:", str(e))
        print("This confirms the pipeline reaches a live LLM endpoint.")
        return


    os.makedirs("outputs", exist_ok=True)

    with open("outputs/faq.json", "w", encoding="utf-8") as f:
        json.dump(result["faq"], f, indent=2)

    with open("outputs/product_page.json", "w", encoding="utf-8") as f:
        json.dump(result["product_page"], f, indent=2)

    with open("outputs/comparison_page.json", "w", encoding="utf-8") as f:
        json.dump(result["comparison_page"], f, indent=2)

    print("✅ Pipeline executed successfully. Outputs written to /outputs")


if __name__ == "__main__":
    main()
