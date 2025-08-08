from pydantic import BaseModel
from typing import List, Optional

class UserChannel(BaseModel):
    id: str
    channel_id: str
    member_id: str

class UserChannelResponse(BaseModel):
    success: bool
    data: Optional[UserChannel] = []
