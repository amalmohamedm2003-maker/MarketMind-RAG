import sys
import os
sys.path.append(os.getcwd())

from backend.rag.growth_agent import GrowthAgent


agent = GrowthAgent()

query = "How can I reduce CPA in paid search campaigns?"

result = agent.analyze(query)

print("\nQUESTION:\n", result["question"])
print("\nAI GROWTH INSIGHTS:\n", result["insights"])
print("\nSources Used:", result["sources_used"])
