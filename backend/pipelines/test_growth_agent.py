def test_growth_agent_runs():
    """
    CI-safe GrowthAgent test.
    Validates structured business output.
    """

    from backend.rag.growth_agent import GrowthAgent

    agent = GrowthAgent()
    result = agent.analyze("How to reduce CPA?")

    assert isinstance(result, dict)

    # Required business fields
    assert "key_insights" in result
    assert "recommendations" in result
    assert "metrics_impact" in result
    assert "confidence_level" in result

    # Optional field (may or may not exist)
    if "sources" in result:
        assert isinstance(result["sources"], list)
