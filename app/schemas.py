from pydantic import BaseModel
from typing import Literal

class OperationInput(BaseModel):
    a: float
    b: float
    operation: Literal["add", "subtract", "multiply", "divide"]