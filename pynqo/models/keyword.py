from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Keyword(BaseModel):
    id: str
    channel_id: Optional[str]
    name: str
    use_pushover: bool
    created_at: datetime
    member_id: str

class KeywordListResponse(BaseModel):
    success: bool
    data: List[Keyword]

class KeywordResponse(BaseModel):
    success: bool
    data: Keyword
