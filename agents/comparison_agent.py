from langchain.prompts import ChatPromptTemplate
from llm.model import get_llm
from graph.state import AgentState
import json


PROMPT = ChatPromptTemplate.from_template("""
You are an AI agent generating a product comparison.

Product A:
{product}

Rules:
- Generate a fictional Product B
- Use similar structure as Product A
- Return a VALID JSON object
- Do not add external facts
""")


def comparison_agent(state: AgentState):
    llm = get_llm()

    response = llm.invoke(
        PROMPT.format(product=state.product_data)
    )

    content = response.content.strip()

    try:
        comparison = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from comparison agent: {content}")

    state.comparison_page = {
        "page_type": "comparison",
        "data": comparison
    }

    return state
