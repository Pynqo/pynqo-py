from pydantic import BaseModel
from typing import List
from datetime import datetime

class Channel(BaseModel):
    id: str
    platform: str
    guild_id: str
    discord_id: str
    created_at: datetime
    name: str

class ChannelListResponse(BaseModel):
    success: bool
    data: List[Channel]

class ChannelResponse(BaseModel):
    success: bool
    data: Channel
