from langchain.prompts import ChatPromptTemplate
from llm.model import get_llm
from graph.state import AgentState
import json


PROMPT = ChatPromptTemplate.from_template("""
You are an AI agent responsible for generating user FAQs.

Product data:
{product}

Rules:
- Generate at least 15 distinct user questions
- Do NOT repeat questions
- Do NOT answer the questions
- Return ONLY a JSON list of strings
""")


def question_agent(state: AgentState):
    llm = get_llm()

    response = llm.invoke(
        PROMPT.format(product=state.product_data)
    )

    content = response.content.strip()

    try:
        questions = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from LLM: {content}")

    if not isinstance(questions, list) or len(questions) < 15:
        raise ValueError("Minimum FAQ requirement not met")

    state.questions = questions
    return state
