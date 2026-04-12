import os
import requests
import json

# Local server (your FastAPI app)
BASE_URL = "http://localhost:7860"

# LLM API (provided automatically by hackathon)
API_BASE = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")


def call_llm(prompt):
    # If running locally, skip LLM
    if not API_BASE or not API_KEY:
        return {"message": "LLM not available in local mode"}

    url = f"{API_BASE}/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def reset():
    response = requests.post(f"{BASE_URL}/reset")
    return response.json()


def step(data):
    # 🔥 THIS IS THE IMPORTANT PART (LLM CALL)
    llm_result = call_llm(
        "Optimize server load to reduce carbon footprint"
    )

    response = requests.post(f"{BASE_URL}/step", json=data)
    result = response.json()

    # attach LLM result (not required but useful)
    result["llm"] = llm_result

    return result


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

    print("[END]"). 
