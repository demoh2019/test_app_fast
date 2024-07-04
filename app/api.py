from fastapi import APIRouter, HTTPException
from decimal import Decimal
from .models import DivisionRequest, DivisionResponse

router = APIRouter()


@router.post("/div", response_model=DivisionResponse)
def divide(request: DivisionRequest) -> DivisionResponse:
    result = Decimal(request.a) / Decimal(request.b)
    response = DivisionResponse(a=request.a, b=request.b, result=result)
    return response