import requests

BASE_URL = "http://localhost:8000"

def reset():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()

def step(data):
    response = requests.post(f"{BASE_URL}/step", json=data)
    return response.json()

if __name__ == "__main__":
    print("Reset:", reset())
    
    sample_data = {
        "servers": [
            {"cpu": 70, "power": "coal"},
            {"cpu": 30, "power": "solar"}
        ]
    }
    
    print("Step:", step(sample_data))