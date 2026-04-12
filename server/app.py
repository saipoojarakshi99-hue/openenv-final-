from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/step")
async def step(request: Request):
    data = await request.json()   

    return {
        "tasks": [
            {"task_id": "cpu_task", "score": 0.51},
            {"task_id": "power_task", "score": 0.72},
            {"task_id": "efficiency_task", "score": 0.43}
        ]
    }


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)



if __name__ == "__main__":
    main()
