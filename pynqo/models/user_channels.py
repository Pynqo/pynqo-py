from pydantic import BaseModel

class UserChannel(BaseModel):
    id: str
    channel_id: str
    member_id: str

class UserChannelResponse(BaseModel):
    success: bool
    data: UserChannel
