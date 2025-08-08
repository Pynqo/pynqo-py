import aiohttp
from ..exceptions import *
from ..models.categorie import CategorieListResponse, CategorieResponse

class CategoriesAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def list(self):
        url = f"{self.baseUrl}/categories"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Guild Not Found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return CategorieListResponse(**data)
    
    async def list_guild(self, guild_id):
        url = f"{self.baseUrl}/guilds/{guild_id}/categories"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Guild Not Found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return CategorieListResponse(**data)
    
    async def delete_categorie(self, categorie_id):
        url = f"{self.baseUrl}/categories/{categorie_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Categorie not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                return True
    
    
    async def get_categorie(self, categorie_id):
        url = f"{self.baseUrl}/categories/{categorie_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Categorie not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return CategorieResponse(**data)