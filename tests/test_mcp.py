from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_tools_endpoint():
    """
    Tests the /mcp/tools endpoint.
    It should return a 200 OK status and a list of tools.
    """
    response = client.get("/mcp/tools")
    assert response.status_code == 200
    
    response_json = response.json()
    assert isinstance(response_json, list)
    
    # Check if the tools have the required fields
    for tool in response_json:
        assert "name" in tool
        assert "description" in tool

    # Check for the specific tools we expect
    expected_tool_names = ["stock_screener", "company_profile"]
    actual_tool_names = [tool["name"] for tool in response_json]
    assert all(name in actual_tool_names for name in expected_tool_names)

def test_get_resources_endpoint():
    """
    Tests the /mcp/resources endpoint.
    It should return a 200 OK status and a list of resources.
    """
    response = client.get("/mcp/resources")
    assert response.status_code == 200
    
    response_json = response.json()
    assert isinstance(response_json, list)
    
    # Check if the resources have the required fields
    for resource in response_json:
        assert "name" in resource
        assert "description" in resource

    # Check for the specific resources we expect
    expected_resource_names = ["market_news", "economic_calendar"]
    actual_resource_names = [resource["name"] for resource in response_json]
    assert all(name in actual_resource_names for name in expected_resource_names)
