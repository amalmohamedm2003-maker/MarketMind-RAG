def test_ingestion_runs():
    from backend.pipelines.ingest_all import run

    # should not crash
    run()
    assert True
