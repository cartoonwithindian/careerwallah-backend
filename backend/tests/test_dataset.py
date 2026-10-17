from app.services.dataset_loader import load_and_normalize
from pathlib import Path

def test_dataset_loads():
    data_path = Path(__file__).parent.parent / "app" / "data" / "rural_opportunity_bridge_dataset.json"
    result = load_and_normalize(str(data_path))
    assert result["schema_version"] == "1.0"
    assert len(result["opportunities"]) > 0
    for opp in result["opportunities"]:
        assert "title" in opp
