import requests 
from ..exceptions import *
from ..models.categorie import CategorieListResponse, CategorieResponse

class CategoriesAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def list(self):
        url = f"{self.baseUrl}/categories"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Guild Not Found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return CategorieListResponse(**resp.json())
    
    def list_guild(self, guild_id):
        url = f"{self.baseUrl}/guilds/{guild_id}/categories"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Guild Not Found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return CategorieListResponse(**resp.json())
    
    def delete_categorie(self, categorie_id):
        url = f"{self.baseUrl}/categories/{categorie_id}"
        resp = requests.delete(url, headers=self.headers)

        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Categorie not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return True
    
    
    def get_categorie(self, categorie_id):
        url = f"{self.baseUrl}/categories/{categorie_id}"
        resp = requests.get(url, headers=self.headers)

        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Categorie not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return CategorieResponse(**resp.json())