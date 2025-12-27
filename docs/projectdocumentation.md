# Problem Statement

The goal of this project is to design and implement a modular, agent-based
automation system that transforms a fixed product dataset into structured,
machine-readable content pages using an orchestrated multi-agent workflow.

The system automatically generates:
- a FAQ page
- a product description page
- a comparison page

The assignment emphasizes agent orchestration, validation, and automation
rather than manual content creation.

---

# Solution Overview

This project implements a LangGraph-based multi-agent content generation
pipeline. Each agent is responsible for a single, well-defined task and
communicates through a shared state object.

Agents are executed as nodes in a StateGraph, ensuring deterministic
execution flow, clear separation of concerns, and extensibility.

---

# Scope & Assumptions

## Scope
- The system operates strictly on the provided product dataset.
- All outputs are generated dynamically at runtime.
- Outputs are structured and machine-readable.
- Deterministic execution is supported for local testing.

## Assumptions
- A fictional product is generated for comparison purposes.
- The system can be extended to support additional product schemas.
- This implementation focuses on backend automation and orchestration.

---

# System Design

The system is implemented using LangGraph and follows a graph-based agentic
architecture.

- Each agent is represented as a graph node.
- A shared state object is passed and updated between agents.
- Execution flow is controlled by a StateGraph rather than procedural code.
- Validation logic ensures minimum output requirements and schema correctness.

This design avoids monolithic scripts and tightly coupled components while
improving testability and robustness.

---

# Agent Responsibilities

- **QuestionAgent**
  Generates and validates a minimum of 15 user FAQs.

- **FAQAgent**
  Generates concise answers for each FAQ using product data.

- **ProductAgent**
  Produces a structured product description page in JSON format.

- **ComparisonAgent**
  Generates a structured comparison between two products.

Each agent updates the shared state and passes it forward in the graph.

---

# LLM Integration

This system uses a live Large Language Model (LLM) via LangChain and OpenAI.

- All agents generate content exclusively through live LLM calls.
- No mock, stub, or hardcoded LLM logic exists in the execution path.
- The pipeline intentionally fails if an API key is not provided.

LangGraph is used to orchestrate agent execution, while LangChain provides
the chat model abstraction used by each agent.

This design ensures:
- Real reasoning-based content generation
- No deterministic or precomputed outputs
- Full compliance with agentic AI constraints
---

# Automation Flow

1. Initial product data is loaded into the graph state.
2. The QuestionAgent generates and validates FAQs.
3. The FAQAgent generates answers for each question.
4. The ProductAgent generates a structured product page.
5. The ComparisonAgent generates a structured comparison page.
6. The LangGraph runner executes the graph and returns final outputs.

---

# Output Structure

The system produces the following machine-readable JSON outputs:

- **faq.json**
  Contains structured question-answer pairs (15+ enforced).

- **product_page.json**
  Contains structured product information such as ingredients, usage, and price.

- **comparison_page.json**
  Contains structured comparison data between two products.

All outputs are generated at runtime and validated before use.
