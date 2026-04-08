from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
def step(data: dict):
    return {"action": "optimize", "confidence": 0.9}


# ✅ THIS IS THE IMPORTANT PART
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


# ✅ REQUIRED for validator
if __name__ == "__main__":
    main()
