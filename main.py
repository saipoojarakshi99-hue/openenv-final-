from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
def step(data: dict):
    return {
        "action": "optimize",
        "confidence": 0.9
    }    