from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import List
from app.service import JDGenerationService
from app.utils import validate_bullet_points

router = APIRouter()
jd_service = JDGenerationService()

class JDRequest(BaseModel):
    role: str = Field(..., min_length=1, description="Job title/role")
    points: List[str] = Field(..., min_items=5, max_items=5, description="Exactly 5 bullet points about the role")
    
    @validator('points')
    def validate_points(cls, v):
        if not validate_bullet_points(v):
            raise ValueError("Exactly 5 bullet points are required")
        for point in v:
            if not point.strip():
                raise ValueError("Bullet points cannot be empty")
        return v

class BiasCheck(BaseModel):
    bias_found: bool
    suggestions: List[dict] = []

class JDResponse(BaseModel):
    job_title: str
    summary: str
    responsibilities: List[str]
    required_qualifications: List[str]
    preferred_qualifications: List[str]
    bias_check: BiasCheck

@router.post("/generate-jd", response_model=JDResponse, status_code=status.HTTP_200_OK)
async def generate_jd(request: JDRequest):
    """
    Generate a complete job description based on role and bullet points.
    
    Args:
        request: JDRequest containing role and 5 bullet points
        
    Returns:
        JDResponse with generated job description and bias check
    """
    try:
        result = jd_service.generate_jd(request.role, request.points)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate job description: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI JD Generator"}
