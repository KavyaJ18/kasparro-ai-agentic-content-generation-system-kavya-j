from langchain_core.prompts import ChatPromptTemplate
from llm.model import get_llm
from graph.state import AgentState
import json


PROMPT = ChatPromptTemplate.from_template("""
You are an AI agent generating a structured product page.

Product data:
{product}

Rules:
- Use ONLY the provided product data
- Return a VALID JSON object
- Do not add new information
- Keys: name, concentration, skin_type, ingredients, benefits, usage, side_effects, price
""")


def product_agent(state: AgentState):
    llm = get_llm()

    response = llm.invoke(
        PROMPT.format(product=state.product_data)
    )

    content = response.content.strip()

    try:
        product_page = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from product agent: {content}")

    product_page["page_type"] = "product"
    state.product_page = product_page
    return state
