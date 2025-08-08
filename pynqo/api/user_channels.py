import aiohttp
from ..exceptions import *
from ..models.channel import ChannelListResponse
from ..models.user_channels import UserChannelResponse

class UserChannelsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def list(self, member_id):
        url = f"{self.baseUrl}/users/{member_id}/channels"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User Not Found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return ChannelListResponse(**data)

    async def insert_channel(self, member_id, channel_id):
        url = f"{self.baseUrl}/users/{member_id}/channels"
        payload = {
            "channel": channel_id
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=payload) as resp:
                if resp.status == 400:
                    try:
                        error_data = await resp.json()
                        if "already exists" in error_data.get("message", ""):
                            raise BadRequestError("This channel already exists for this user and guild")
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
                return UserChannelResponse(**data)
    
    async def delete_channel(self, channel_id):
        url = f"{self.baseUrl}/user-channels/{channel_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User channel not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                return True

    async def get_channel(self, channel_id):
        url = f"{self.baseUrl}/user-channels/{channel_id}"
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
                return UserChannelResponse(**data)
