from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Categorie(BaseModel):
    id: str
    name: str
    guild_id: str
    discord_id: str
    created_at: datetime

class CategorieListResponse(BaseModel):
    success: bool
    data: Optional[List[Categorie]] = []

class CategorieResponse(BaseModel):
    success: bool
    data: Categorie
