import requests
import json

BASE_URL = "http://localhost:7860"

def reset():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()

def step(data):
    response = requests.post(f"{BASE_URL}/step", json=data)
    return response.json()

if __name__ == "__main__":
    sample_data = {
        "servers": [
            {"cpu": 70, "power": "coal"},
            {"cpu": 30, "power": "solar"}
        ]
    }

    print("[START]")
    print(json.dumps(reset()))

    print("[STEP]")
    print(json.dumps(step(sample_data)))

    print("[END]")
