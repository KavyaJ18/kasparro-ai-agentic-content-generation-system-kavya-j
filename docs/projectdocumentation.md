# Problem Statement
The goal of this project is to design and implement a modular, agent-based automation system that transforms a fixed product dataset into structured, machine-readable content pages.

The system must automatically generate:
- a FAQ page
- a product description page
- a comparison page

The assignment focuses on system design, agent orchestration, and automation rather than content creativity or domain expertise.

# Solution Overview
This project implements a multi-agent content generation pipeline where each component has a single, well-defined responsibility.

The system is composed of independent agents, reusable logic blocks, and structured templates, all coordinated by a central orchestrator. The pipeline takes raw product data as input and produces multiple structured JSON outputs without shared global state.

# Scope & Assumptions
Scope:
- The system operates strictly on the provided product dataset.
- No external APIs or external knowledge sources are used.
- All generated content is deterministic.

Assumptions:
- A fictional product is used for comparison purposes.
- The system can be extended to support additional products with similar schemas.
- This implementation focuses only on backend automation and content generation.

# System Design
The system follows a layered agentic architecture with clear separation of concerns.

Agents are responsible for preparing or transforming data. Templates are responsible only for assembling structured outputs. Reusable logic blocks encapsulate transformation rules. A central orchestrator controls execution flow and ensures agents remain decoupled.

This design improves modularity, testability, and extensibility while avoiding monolithic scripts or tightly coupled components.

# Agent Responsibilities
- DataParserAgent: Normalizes raw input data into an internal representation.
- QuestionGeneratorAgent: Generates categorized user questions based on product data.
- ComparisonAgent: Prepares structured comparison data between two products.
- FAQTemplateAgent: Assembles FAQ content into structured JSON.
- ProductPageTemplateAgent: Formats product data into a product page structure.
- ComparisonTemplateAgent: Formats comparison data into a comparison page structure.

# Automation Flow
1. Raw product data is passed to the orchestrator.
2. The orchestrator invokes the data parser agent.
3. Parsed data is sent to the question generation agent.
4. Template agents assemble structured content pages.
5. The runner executes the pipeline and writes JSON outputs to disk.


# Output Structure
The system generates the following machine-readable outputs:

- faq.json: Contains structured question and answer pairs.
- product_page.json: Contains structured product information such as ingredients, usage, and price.
- comparison_page.json: Contains structured comparison data between two products.

All outputs are formatted as clean JSON for downstream consumption.

