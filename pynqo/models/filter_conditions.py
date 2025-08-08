from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class FilterType(str, Enum):
    allow_all = "allow_all"
    block_any = "block_any"

class FilterCondition(BaseModel):
    id: str
    filter_id: str
    embed_field_title: Optional[str] = None
    filter_value: str
    type: FilterType
    created_at: datetime

class FilterConditionResponse(BaseModel):
    success: bool
    data: FilterCondition

class FilterConditionListResponse(BaseModel):
    success: bool
    data: Optional[List[FilterCondition]]