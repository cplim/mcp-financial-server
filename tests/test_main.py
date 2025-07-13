from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_list_tools():
    response = client.get("/mcp/tools")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    for tool in response_json:
        assert "name" in tool
        assert "description" in tool
