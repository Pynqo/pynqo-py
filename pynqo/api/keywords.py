import aiohttp
from ..exceptions import *
from ..models.keyword import *

class KeywordsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def list(self):
        url = f"{self.baseUrl}/keywords"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return KeywordListResponse(**data)
    
    async def list_user(self, member_id):
        url = f"{self.baseUrl}/users/{member_id}/keywords"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return KeywordListResponse(**data)
    
    async def add_keyword(self, member_id, name):
        url = f"{self.baseUrl}/users/{member_id}/keywords"
        body = {
            "name": name,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=body) as resp:
                if resp.status == 400:
                    try:
                        error_data = await resp.json()
                        if "already exists" in error_data.get("message", ""):
                            raise BadRequestError("Keyword already exists for this user and guild")
                    except ValueError:
                        pass
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return KeywordResponse(**data)
    
    async def delete_keyword(self, keyword_id):
        url = f"{self.baseUrl}/keywords/{keyword_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                return True
    
    async def edit_keyword(self, keyword_id, name=None, use_pushover=None):
        if name is None and use_pushover is None:
            raise ValueError("At least 'name' or 'use_pushover' must be provided.")

        payload = {}
        if name is not None:
            payload["name"] = name
        if use_pushover is not None:
            payload["use_pushover"] = use_pushover

        url = f"{self.baseUrl}/keywords/{keyword_id}"
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, json=payload, headers=self.headers) as resp:
                if resp.status == 400:
                    try:
                        error_data = await resp.json()
                        if "already exists" in error_data.get("message", ""):
                            raise BadRequestError("Keyword already exists for this user and guild")
                    except ValueError:
                        pass
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return KeywordResponse(**data)
    