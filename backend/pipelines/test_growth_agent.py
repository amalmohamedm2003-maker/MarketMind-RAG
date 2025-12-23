import sys
import os
sys.path.append(os.getcwd())

from backend.rag.growth_agent import GrowthAgent


agent = GrowthAgent()

query = "How can I reduce CPA in paid search campaigns?"

result = agent.analyze(query)

def test_growth_agent_runs():
    from backend.rag.growth_agent import GrowthAgent
    agent = GrowthAgent()
    result = agent.analyze("How to reduce CPA?")
    assert "answer" in result

print("\nAI GROWTH INSIGHTS:\n", result["insights"])
print("\nSources Used:", result["sources_used"])
