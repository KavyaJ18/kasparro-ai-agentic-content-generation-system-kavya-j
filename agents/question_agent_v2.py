from langchain_core.prompts import ChatPromptTemplate
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

    max_retries = 3
    last_error = None

    for attempt in range(max_retries):
        response = llm.invoke(
            PROMPT.format(product=state.product_data)
        )

        content = response.content.strip()

        try:
            questions = json.loads(content)

            if not isinstance(questions, list):
                raise ValueError("Output is not a list")

            if len(questions) < 15:
                raise ValueError("Less than 15 questions generated")

            # Success
            state.questions = questions
            return state

        except Exception as e:
            last_error = str(e)

    raise RuntimeError(
        f"Failed to generate valid FAQs after {max_retries} attempts. "
        f"Last error: {last_error}"
    )
