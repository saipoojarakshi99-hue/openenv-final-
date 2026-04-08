from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Green Ops API running"}

@app.post("/reset")
def reset():
    return {"status": "environment reset"}

@app.post("/step")
def step(data: dict):
    servers = data.get("servers", [])
    
    # Simple RL-like logic
    action = "optimize_power"
    confidence = 0.9
    
    return {
        "action": action,
        "confidence": confidence
    }