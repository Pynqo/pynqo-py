import requests 
from ..exceptions import *
from ..models.user import UserResponse, User

class UsersAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def get(self, user_id, guild_id):
        url = f"{self.baseUrl}/users/{user_id}/guilds/{guild_id}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif resp.status_code == 404:
            raise NotFoundError("member not found")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return UserResponse(**resp.json())