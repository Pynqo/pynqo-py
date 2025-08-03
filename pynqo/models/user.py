from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    source: str
    stytch_id: str
    created_at: datetime

class UserResponse(BaseModel):
    success: bool
    data: User