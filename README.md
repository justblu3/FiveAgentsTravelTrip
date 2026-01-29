# 🌍 AI Travel Agency - Multi-Agent System

A Python-based multi-agent system where **5 AI agents collaborate** to plan travel itineraries and audit budgets. This project demonstrates modular AI architecture using local LLMs (Llama 3 via Ollama).

## 🧠 Project Architecture

The system uses a **Hub & Spoke** architecture where a central controller manages data flow between specialized agents:

1.  **Travel Manager:** Analyzes user requests to determine destination, duration, and budget.
2.  **Hotel Broker:** Finds accommodation options fitting the plan;
3.  **Restaurant Broker:** Suggests dining options.
4.  **Activity Planner:** Recommends local attractions.
5.  **Budget Auditor:** Reviews the total estimated cost against the user's budget and issues an APPROVED/REJECTED verdict.

## 📂 Project Structure

```text
ai_travel_agency/
├── agents/             # Individual Agent personalities
│   ├── manager.py
│   ├── hotel.py
│   ├── restaurant.py
│   ├── activity.py
│   └── auditor.py
├── core.py             # Base Agent class & LLM connection logic
├── main.py             # Main controller script
├── pyproject.toml      # Dependency management (uv)
└── README.md


🛠️ Prerequisites
Python 3.10+

uv (Fast Python package installer)

Ollama (For running the Llama model locally)

Setup the environment (using uv):

Bash
uv init
uv add openai
Prepare the Local LLM: Make sure Ollama is running and download the Llama 3 model:

Bash
ollama pull llama3
Run the Project:

Bash
uv run main.py
