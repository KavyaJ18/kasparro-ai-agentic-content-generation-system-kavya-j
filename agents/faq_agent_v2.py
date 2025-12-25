from langchain.prompts import ChatPromptTemplate
from llm.model import get_llm
from graph.state import AgentState
import json


PROMPT = ChatPromptTemplate.from_template("""
You are an AI assistant answering user FAQs.

Product data:
{product}

Question:
{question}

Rules:
- Answer ONLY using the product data
- Do NOT add external information
- Keep answers concise and helpful
""")


def faq_agent(state: AgentState):
    llm = get_llm()
    items = []

    for question in state.questions:
        response = llm.invoke(
            PROMPT.format(
                product=state.product_data,
                question=question
            )
        )

        answer = response.content.strip()

        items.append({
            "question": question,
            "answer": answer
        })

    state.faq = {
        "page_type": "faq",
        "items": items
    }

    return state
