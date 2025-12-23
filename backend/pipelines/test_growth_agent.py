def test_growth_agent_runs():
    """
    CI-safe GrowthAgent test.
    Validates structured business output.
    """

    from backend.rag.growth_agent import GrowthAgent

    agent = GrowthAgent()
    result = agent.analyze("How to reduce CPA?")

    assert isinstance(result, dict)

    # Business-grade structured assertions
    assert "key_insights" in result
    assert "recommendations" in result
    assert "metrics_impact" in result
    assert "confidence_level" in result
    assert "sources" in result
