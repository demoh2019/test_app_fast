from pydantic import BaseModel, Field, field_validator
from decimal import Decimal


class DivisionRequest(BaseModel):
    a: int = Field(..., description="The dividend must be an integer")
    b: int = Field(..., description="The divisor must be an integer")

    @field_validator('b')
    def check_not_zero(cls, value: int) -> int:
        if value == 0:
            raise ValueError("The divisor 'b' cannot be zero")
        return value


class DivisionResponse(BaseModel):
    a: int
    b: int
    result: Decimal

    @field_validator('result', mode='before')
    def validate_result(cls, value) -> Decimal:
        if isinstance(value, (int, float, str)):
            return Decimal(value)
        return value