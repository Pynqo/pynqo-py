from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class TrustedMetadata(BaseModel):
    keyword_limit: int
    delay: int
    user_role_id: str

class Organization(BaseModel):
    organization_id: str
    organization_name: Optional[str]
    organization_slug: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    trusted_metadata: Optional[TrustedMetadata]

class Guild(BaseModel):
    id: str
    stytch_id: str
    created_at: Optional[datetime]
    Organization: Optional[Organization]
