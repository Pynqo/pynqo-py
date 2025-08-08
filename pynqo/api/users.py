import aiohttp
from ..exceptions import *
from ..models.user import UserResponse, User

class UsersAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def get(self, user_id, guild_id):
        url = f"{self.baseUrl}/users/{user_id}/guilds/{guild_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status == 404:
                    raise NotFoundError("member not found")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return UserResponse(**data)