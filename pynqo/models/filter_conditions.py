from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class FilterType(str, Enum):
    must_be_included = "must_be_included"
    must_be_excluded = "must_be_excluded"

class FilterCondition(BaseModel):
    id: str
    filter_id: str
    embed_field_title: Optional[str] = None
    filter_value: str
    type: FilterType

class FilterConditionResponse(BaseModel):
    success: bool
    data: FilterCondition

class FilterConditionListResponse(BaseModel):
    success: bool
    data: Optional[List[FilterCondition]] = []