import requests 
from ..exceptions import *
from ..models.channel import ChannelListResponse
from ..models.user_channels import UserChannelResponse

class UserChannelsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def list(self, member_id):
        url = f"{self.baseUrl}/users/{member_id}/channels"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("User Not Found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return ChannelListResponse(**resp.json())

    def insert_channel(self, member_id, channel_id):
        url = f"{self.baseUrl}/users/{member_id}/channels"
        payload = {
            "channel": channel_id
        }

        resp = requests.post(url, headers=self.headers, json=payload)

        if resp.status_code == 400:
            try:
                error_data = resp.json()
                if "already exists" in error_data.get("message", ""):
                    raise BadRequestError("This channel already exists for this user and guild")
            except ValueError:
                pass
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("User not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return UserChannelResponse(**resp.json())
    
    def delete_channel(self, channel_id):
        url = f"{self.baseUrl}/user-channels/{channel_id}"
        resp = requests.delete(url, headers=self.headers)

        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("User channel not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return True

    def get_channel(self, channel_id):
        url = f"{self.baseUrl}/user-channels/{channel_id}"
        resp = requests.get(url, headers=self.headers)

        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("User not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return UserChannelResponse(**resp.json())
