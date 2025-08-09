import aiohttp
from ..exceptions import *
from ..models.channel import ChannelListResponse, ChannelResponse

class ChannelsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def list(self):
        url = f"{self.baseUrl}/channels"
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
                return ChannelListResponse(**data)
    
    async def list_guild(self, guild_id):
        url = f"{self.baseUrl}/guilds/{guild_id}/channels"
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
                return ChannelListResponse(**data)
    
    async def delete_channel(self, channel_id):
        url = f"{self.baseUrl}/channels/{channel_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Channel not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                return True
    
    
    async def get_channel(self, channel_id):
        url = f"{self.baseUrl}/channels/{channel_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Channel not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return ChannelResponse(**data)

    async def bulk_fetch_channels(self, channel_ids):
        """Bulk fetch channels by IDs"""
        url = f"{self.baseUrl}/channels/bulk"
        body = {"ids": channel_ids}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=body) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Channels not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return ChannelListResponse(**data)

    async def bulk_fetch_guild_channels(self, guild_id, channel_ids):
        """Bulk fetch guild channels by IDs"""
        url = f"{self.baseUrl}/guilds/{guild_id}/channels/bulk"
        body = {"ids": channel_ids}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=body) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Guild or channels not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return ChannelListResponse(**data)

    async def bulk_fetch_user_channels(self, member_id, channel_ids):
        """Bulk fetch user channels by IDs"""
        url = f"{self.baseUrl}/users/{member_id}/channels/bulk"
        body = {"ids": channel_ids}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=body) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("User or channels not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return ChannelListResponse(**data)