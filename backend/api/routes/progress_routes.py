from fastapi import APIRouter, Depends
from backend.api.schemas import ResponseEnvelope
from backend.api.dependencies.auth import get_admin_user, get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("", response_model=ResponseEnvelope)
async def get_progress():
    return ResponseEnvelope(data={"completed_lessons": [1]})

@router.get("/report", response_model=ResponseEnvelope, dependencies=[Depends(get_admin_user)])
async def get_progress_report():
    return ResponseEnvelope(data={"aggregate_metrics": "admin_view_data"})
