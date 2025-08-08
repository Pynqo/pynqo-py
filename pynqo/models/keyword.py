from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Keyword(BaseModel):
    id: str
    channel_id: Optional[str]
    name: Optional[str]
    use_pushover: Optional[bool]
    created_at: datetime
    member_id: str

class KeywordListResponse(BaseModel):
    success: bool
    data: Optional[List[Keyword]] = []

class KeywordResponse(BaseModel):
    success: bool
    data: Optional[Keyword]
