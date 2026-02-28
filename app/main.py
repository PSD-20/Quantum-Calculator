from fastapi import FastAPI, HTTPException
import math
from app.schemas import OperationInput
from app.operations.addition import addition
from app.operations.subtraction import subtraction
from app.operations.multiplication import multiplication
from app.operations.division import division
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Quantum Calculator API")

templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
def calculate(data: OperationInput):
    try:
        if data.operation == "add":
            result = addition(data.a, data.b)
        elif data.operation == "subtract":
            result = subtraction(data.a, data.b)
        elif data.operation == "multiply":
            result = multiplication(data.a, data.b)
        elif data.operation == "divide":
            result = division(data.a, data.b)
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")

        # Convert to float (important for tensors / numpy values)
        result = float(result)

        # Check for NaN or Infinity
        if not math.isfinite(result):
            raise HTTPException(
                status_code=400,
                detail="Computation resulted in invalid value"
            )

        return {"result": result}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))