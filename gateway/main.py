# gateway/main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx
from typing import Any

app = FastAPI(title="Gym Management API Gateway", version="1.0.0")

# Service URLs - each member runs their service on their port
SERVICES = {
    "member":    "http://localhost:8001",
    "trainer":   "http://localhost:8002",
    "workout":   "http://localhost:8003",
    "equipment": "http://localhost:8004",
}

async def forward_request(service: str, path: str, method: str, **kwargs) -> Any:
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")
    url = f"{SERVICES[service]}{path}"
    async with httpx.AsyncClient() as client:
        try:
            if method == "GET":
                response = await client.get(url, **kwargs)
            elif method == "POST":
                response = await client.post(url, **kwargs)
            elif method == "PUT":
                response = await client.put(url, **kwargs)
            elif method == "DELETE":
                response = await client.delete(url, **kwargs)
            else:
                raise HTTPException(status_code=405, detail="Method not allowed")
            return JSONResponse(
                content=response.json() if response.text else None,
                status_code=response.status_code
            )
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Gym Management API Gateway is running", "services": list(SERVICES.keys())}

# ── Member Routes (Port 8001) ──────────────────────────────
@app.get("/gateway/members")
async def get_all_members():
    return await forward_request("member", "/api/members", "GET")

@app.get("/gateway/members/{member_id}")
async def get_member(member_id: int):
    return await forward_request("member", f"/api/members/{member_id}", "GET")

@app.post("/gateway/members")
async def create_member(request: Request):
    body = await request.json()
    return await forward_request("member", "/api/members", "POST", json=body)

@app.put("/gateway/members/{member_id}")
async def update_member(member_id: int, request: Request):
    body = await request.json()
    return await forward_request("member", f"/api/members/{member_id}", "PUT", json=body)

@app.delete("/gateway/members/{member_id}")
async def delete_member(member_id: int):
    return await forward_request("member", f"/api/members/{member_id}", "DELETE")

# ── Trainer Routes (Port 8002) ─────────────────────────────
@app.get("/gateway/trainers")
async def get_all_trainers():
    return await forward_request("trainer", "/api/trainers", "GET")

@app.get("/gateway/trainers/{trainer_id}")
async def get_trainer(trainer_id: int):
    return await forward_request("trainer", f"/api/trainers/{trainer_id}", "GET")

@app.post("/gateway/trainers")
async def create_trainer(request: Request):
    body = await request.json()
    return await forward_request("trainer", "/api/trainers", "POST", json=body)

@app.put("/gateway/trainers/{trainer_id}")
async def update_trainer(trainer_id: int, request: Request):
    body = await request.json()
    return await forward_request("trainer", f"/api/trainers/{trainer_id}", "PUT", json=body)

@app.delete("/gateway/trainers/{trainer_id}")
async def delete_trainer(trainer_id: int):
    return await forward_request("trainer", f"/api/trainers/{trainer_id}", "DELETE")

# ── Workout Routes (Port 8003) ─────────────────────────────
@app.get("/gateway/workouts")
async def get_all_workouts():
    return await forward_request("workout", "/api/workouts", "GET")

@app.get("/gateway/workouts/{workout_id}")
async def get_workout(workout_id: int):
    return await forward_request("workout", f"/api/workouts/{workout_id}", "GET")

@app.post("/gateway/workouts")
async def create_workout(request: Request):
    body = await request.json()
    return await forward_request("workout", "/api/workouts", "POST", json=body)

@app.put("/gateway/workouts/{workout_id}")
async def update_workout(workout_id: int, request: Request):
    body = await request.json()
    return await forward_request("workout", f"/api/workouts/{workout_id}", "PUT", json=body)

@app.delete("/gateway/workouts/{workout_id}")
async def delete_workout(workout_id: int):
    return await forward_request("workout", f"/api/workouts/{workout_id}", "DELETE")

# ── Equipment Routes (Port 8004) ───────────────────────────
@app.get("/gateway/equipment")
async def get_all_equipment():
    return await forward_request("equipment", "/api/equipment", "GET")

@app.get("/gateway/equipment/{equipment_id}")
async def get_equipment(equipment_id: int):
    return await forward_request("equipment", f"/api/equipment/{equipment_id}", "GET")

@app.post("/gateway/equipment")
async def create_equipment(request: Request):
    body = await request.json()
    return await forward_request("equipment", "/api/equipment", "POST", json=body)

@app.put("/gateway/equipment/{equipment_id}")
async def update_equipment(equipment_id: int, request: Request):
    body = await request.json()
    return await forward_request("equipment", f"/api/equipment/{equipment_id}", "PUT", json=body)

@app.delete("/gateway/equipment/{equipment_id}")
async def delete_equipment(equipment_id: int):
    return await forward_request("equipment", f"/api/equipment/{equipment_id}", "DELETE")