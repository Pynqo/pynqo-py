from pydantic import BaseModel
from typing import Optional, List

class Filter(BaseModel):
    id: str
    keyword_id: str
    filter_name: Optional[str] = None

class FilterResponse(BaseModel):
    success: bool
    data: Filter

class FilterListResponse(BaseModel):
    success: bool
    data: Optional[List[Filter]] = []