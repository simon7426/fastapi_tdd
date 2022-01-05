import json
import pytest

def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summaries/", data=json.dumps({
        "url": "testdriven.io"
    }))
    assert response.status_code == 201
    assert response.json()["url"] == "testdriven.io"