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

    servers = data.get("servers", [])

    tasks = []

    for i, server in enumerate(servers):
        cpu = server.get("cpu", 50)

        # score between (0,1)
        score = max(0.01, min(cpu / 100, 0.99))

        tasks.append({
            "id": f"task_{i+1}",   
            "score": float(score)
        })

    # ensure minimum 3 tasks
    while len(tasks) < 3:
        tasks.append({
            "id": f"extra_{len(tasks)+1}",
            "score": 0.5
        })

    return {"tasks": tasks}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)



if __name__ == "__main__":
    main()
