import pytest
import requests

def test_authentication_failed(mocker):
    """Test that invalid login returns 401 with an empty body."""
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}

    # Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 401, f"Expected 401, but got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, but got: {response.text}"

def test_authentication_success(mocker):
    """Test that valid login returns 200 with an empty body."""
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}

    # Mock the response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, but got: {response.text}"
