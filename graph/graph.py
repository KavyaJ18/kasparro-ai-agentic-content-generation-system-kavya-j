from langgraph.graph import StateGraph
from graph.state import AgentState

from agents.question_agent_v2 import question_agent
from agents.faq_agent_v2 import faq_agent
from agents.product_agent import product_agent
from agents.comparison_agent import comparison_agent


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("question_agent", question_agent)
    builder.add_node("faq_agent", faq_agent)
    builder.add_node("product_agent", product_agent)
    builder.add_node("comparison_agent", comparison_agent)

    builder.set_entry_point("question_agent")

    builder.add_edge("question_agent", "faq_agent")
    builder.add_edge("faq_agent", "product_agent")
    builder.add_edge("product_agent", "comparison_agent")

    return builder.compile()
