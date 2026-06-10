#!/usr/bin/env python
"""Test script to verify test generation API endpoint."""
import requests
import json

BASE_URL = "http://localhost:8000"

# Test health endpoint
print("=" * 60)
print("Testing Health Endpoint")
print("=" * 60)
try:
    response = requests.get(f"{BASE_URL}/api/v1/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

# Test test generation endpoint
print("\n" + "=" * 60)
print("Testing Test Generation Endpoint")
print("=" * 60)

test_payload = {
    "repo_context": {
        "name": "sample-repo",
        "description": "A sample Python repository",
        "language": "python",
        "frameworks": ["pytest"],
        "structure": ["src/", "tests/"],
        "technologies": ["FastAPI", "SQLAlchemy"]
    },
    "user_story": "As a user, I want to log in with my email and password so that I can access my account",
    "language": "python"
}

try:
    response = requests.post(
        f"{BASE_URL}/api/v1/tests/generate",
        json=test_payload,
        headers={"Content-Type": "application/json"},
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    
    try:
        response_json = response.json()
        print(f"\nResponse JSON:")
        print(json.dumps(response_json, indent=2))
        
        # Check for fallback mode
        if response_json.get("mode") == "fallback":
            print("\n✓ Fallback mode activated (Gemini API unavailable)")
        else:
            print("\n✓ Normal mode (Gemini API working)")
            
    except json.JSONDecodeError:
        print(f"Response Text: {response.text}")
        
except requests.exceptions.Timeout:
    print("Error: Request timed out (30 seconds)")
except requests.exceptions.ConnectionError:
    print("Error: Failed to connect to server at http://localhost:8000")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("Test Complete")
print("=" * 60)
