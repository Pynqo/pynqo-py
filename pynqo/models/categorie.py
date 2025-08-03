from pydantic import BaseModel
from typing import List
from datetime import datetime

class Categorie(BaseModel):
    id: str
    name: str
    guild_id: str
    discord_id: str
    created_at: datetime

class CategorieListResponse(BaseModel):
    success: bool
    data: List[Categorie]

class CategorieResponse(BaseModel):
    success: bool
    data: Categorie
