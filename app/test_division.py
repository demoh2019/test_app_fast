from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_division():
    response = client.post("/div", json={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": 3, "result": '3.333333333333333333333333333'}


def test_division_by_zero():
    response = client.post("/div", json={"a": 0, "b": 0})
    assert response.status_code == 422
    assert "The divisor 'b' cannot be zero" in response.json()["detail"][0]["msg"]


def test_division_with_negative_divisor():
    response = client.post("/div", json={"a": 10, "b": -2})
    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": -2, "result": '-5'}


def test_invalid_type_for_a():
    response = client.post("/div", json={"a": "invalid", "b": 2})
    assert response.status_code == 422
    assert "Input should be a valid integer, unable to parse string as an integer" in response.json()["detail"][0]["msg"]


def test_missing_parameter_a():
    response = client.post("/div", json={"b": 2})
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]


def test_missing_parameter_b():
    response = client.post("/div", json={"a": 10})
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
