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
def step(data):
    return {
        "tasks": [
            {"task_id": "cpu_task", "score": 0.5},
            {"task_id": "power_task", "score": 0.7},
            {"task_id": "efficiency_task", "score": 0.4}
        ]
    }


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)



if __name__ == "__main__":
    main()
