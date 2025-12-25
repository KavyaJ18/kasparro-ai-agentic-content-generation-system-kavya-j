from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from typing import List, Optional
import json


class MockChatModel(BaseChatModel):
    """
    Mock LLM used for local testing without API calls.
    Correctly simulates outputs for all agent types.
    """

    def _generate(
        self,
        messages: List,
        stop: Optional[List[str]] = None,
        run_manager=None,
        **kwargs
    ) -> ChatResult:

        last_message = messages[-1].content.lower()

        # ---- QUESTION GENERATION AGENT ----
        if "generate at least 15" in last_message:
            content = json.dumps([
                f"What is question {i + 1} about this product?"
                for i in range(15)
            ])

        # ---- PRODUCT PAGE AGENT ----
        elif "structured product page" in last_message:
            content = json.dumps({
                "name": "GlowBoost Vitamin C Serum",
                "concentration": "10% Vitamin C",
                "skin_type": ["Oily", "Combination"],
                "ingredients": ["Vitamin C", "Hyaluronic Acid"],
                "benefits": ["Brightening", "Fades dark spots"],
                "usage": "Apply 2–3 drops in the morning before sunscreen",
                "side_effects": "Mild tingling for sensitive skin",
                "price": "₹699"
            })

        # ---- COMPARISON AGENT ----
        elif "product comparison" in last_message:
            content = json.dumps({
                "product_a": {
                    "name": "GlowBoost Vitamin C Serum",
                    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
                    "benefits": ["Brightening", "Fades dark spots"],
                    "price": "₹699"
                },
                "product_b": {
                    "name": "Radiant C Serum",
                    "ingredients": ["Vitamin C"],
                    "benefits": ["Brightening"],
                    "price": "₹799"
                }
            })

        # ---- FAQ ANSWER AGENT ----
        else:
            content = "This answer is generated based on the provided product data."

        message = AIMessage(content=content)
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock-chat-model"


def get_llm():
    return MockChatModel()
