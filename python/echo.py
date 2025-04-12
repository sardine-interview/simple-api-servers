from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/echo")
async def echo(request: Request):
    return await request.body()
