from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# This is slow on purpose, don't change it

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@app.get("/fibonacci")
def fibonacci_endpoint(n: str | None = None):
    number = None
    if n is not None:
        try:
            number = int(n)
        except ValueError:
            pass

    if number is None or number < 0 or number > 50:
        return JSONResponse(
            status_code=400,
            content={"error": "n must be an integer between 0 and 50"},
        )

    return {"n": number, "result": fibonacci(number)}


@app.post("/api")
async def api(request: Request):
    body = json.loads(await request.body())
    return {"message": f"Hello {body['name']}!"}
