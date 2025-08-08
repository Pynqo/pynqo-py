from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Keyword(BaseModel):
    id: str
    channel_id: Optional[str] = None
    name: Optional[str] = None
    use_pushover: Optional[bool] = None
    created_at: Optional[datetime] = None
    member_id: Optional[str] = None

class KeywordListResponse(BaseModel):
    success: bool
    data: Optional[List[Keyword]] = []

class KeywordResponse(BaseModel):
    success: bool
    data: Optional[Keyword]
