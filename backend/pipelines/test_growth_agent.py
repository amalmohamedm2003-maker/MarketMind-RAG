def test_growth_agent_runs():
    """
    CI-safe GrowthAgent test.
    Ensures pipeline executes end-to-end.
    """

    from backend.rag.growth_agent import GrowthAgent

    agent = GrowthAgent()
    result = agent.analyze("How to reduce CPA?")

    assert isinstance(result, dict)
    assert "answer" in result
