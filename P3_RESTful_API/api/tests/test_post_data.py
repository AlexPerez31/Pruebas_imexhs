import json
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_upload_valid_data():
    client = APIClient()

    payload = {
        "1": {
            "id": "pytest-id-1",
            "data": [
                "10 20 30",
                "40 50 60"
            ],
            "deviceName": "CT SCAN"
        }
    }

    response = client.post("/api/data/upload/", data=json.dumps(payload), content_type="application/json")

    assert response.status_code == 201 or response.status_code == 207
    assert "success_ids" in response.data
    assert "pytest-id-1" in response.data["success_ids"]


@pytest.mark.django_db
def test_upload_duplicate_id():
    client = APIClient()

    payload = {
        "1": {
            "id": "pytest-duplicate-id",
            "data": [
                "5 5 5",
                "5 5 5"
            ],
            "deviceName": "MRI"
        }
    }

    # Primer intento: para qeu funcione
    response1 = client.post("/api/data/upload/", data=json.dumps(payload), content_type="application/json")
    assert response1.status_code == 201 or response1.status_code == 207

    # Segundo intento con la misma ID: debe fallar
    response2 = client.post("/api/data/upload/", data=json.dumps(payload), content_type="application/json")
    assert response2.status_code == 207
    assert "errors" in response2.data
    assert "1" in response2.data["errors"]
    assert "id" in response2.data["errors"]["1"]


@pytest.mark.django_db
def test_get_all_data():
    client = APIClient()
    url = reverse('data-read') 
    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.data, list) 
