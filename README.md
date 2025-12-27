# Kasparro Agentic Content Generation System

A LangGraph-based multi-agent system that transforms structured product data
into machine-readable content pages using live LLM reasoning.

## Features
- FAQ generation (15+ questions)
- Product page generation
- Product comparison generation
- Agent orchestration using LangGraph
- Live LLM-based reasoning via LangChain OpenAI

## Architecture
- Agents: Question, FAQ, Product, Comparison
- Orchestration: LangGraph
- LLM: OpenAI via LangChain
- Outputs: JSON

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python run_pipeline.py
