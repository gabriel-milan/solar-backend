# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from loguru import logger
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import LightIntensity

LightIntensityInPydantic = pydantic_model_creator(
    LightIntensity, name="LightIntensityIn", exclude=("id", "created_at")
)
LightIntensityListPydantic = pydantic_model_creator(
    LightIntensity, name="LightIntensityList", exclude=("id",)
)

router = APIRouter(prefix="/lux", tags=["lux"])


class Status(BaseModel):
    message: str
    success: bool


@router.get("/", response_model=Page[LightIntensityListPydantic])
async def list_items():
    return paginate(await LightIntensityListPydantic.from_queryset(LightIntensity.all()))


@router.post("/", status_code=201)
async def create_item(tenant: LightIntensityInPydantic) -> Status:
    try:
        await LightIntensity.create(**tenant.dict(exclude_unset=True))
        return Status(message="Item created", success=True)
    except Exception as exc:
        logger.error(exc)
        return Status(message="Item failed to create", success=False)
