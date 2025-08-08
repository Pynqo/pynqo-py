from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class FilterScope(str, Enum):
    keyword = "keyword"
    embed = "embed"

class Filter(BaseModel):
    id: str
    keyword_id: str
    scope: FilterScope

class FilterResponse(BaseModel):
    success: bool
    data: Filter

class FilterListResponse(BaseModel):
    success: bool
    data: Optional[List[Filter]] = []