from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/api")
async def api(request: Request):
    body = json.loads(await request.body())
    return {"message": f"Hello {body['name']}!"}
