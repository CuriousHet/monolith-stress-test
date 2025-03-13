from fastapi import FastAPI, HTTPException
import time
import requests  # type: ignore

app = FastAPI()

# **Bottleneck: Blocking Operation**
@app.get("/block/")
def blocking_task():
    time.sleep(10)  # Simulates a long computation
    return {"message": "Blocking task completed"}

# **Bottleneck: Single External API Dependency**
EXTERNAL_API = "https://jsonplaceholder.typicode.com/posts"

@app.get("/external/")
def external_request():
    response = requests.get(EXTERNAL_API, timeout=5)  # If API is slow, everything slows down
    return response.json()

# **Database Bottleneck Simulation**
@app.get("/db/")
def db_query():
    time.sleep(5)  # Simulate slow DB query
    return {"data": "Fetched from DB after delay"}

# **Failure Simulation: Random Crash**
@app.get("/crash/")
def crash_app():
    raise HTTPException(status_code=500, detail="Monolith Crashed!")

# **Memory Leak Simulation**
leak = []
@app.get("/memory-leak/")
def memory_leak():
    global leak
    leak.extend([b"x" * 10**6] * 100)  # Consumes large memory
    return {"message": "Memory increasing!"}
