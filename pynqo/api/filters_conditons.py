import aiohttp
from ..exceptions import *
from ..models.filter_conditions import FilterConditionResponse, FilterConditionListResponse

class FilterConditionsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    async def get_filter_conditions(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return FilterConditionListResponse(**data)
    
    async def create_filter_condition(self, filter_id, condition_type, filter_value, field_title=None):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        body = {
            "type": condition_type,
            "value": filter_value,
        }
        if field_title is not None:
            body["field_title"] = field_title
            
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=body) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200 and resp.status != 201:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return FilterConditionResponse(data)
    
    async def delete_filter_conditions(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                return await resp.json()
    
    async def get_filter_condition(self, condition_id):
        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter condition not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return FilterConditionResponse(**data)
    
    async def update_filter_condition(self, condition_id, condition_type=None, value=None, embed_field_title=None):
        if condition_type is None and value is None and embed_field_title is None:
            raise ValueError("At least one field must be provided for update.")

        payload = {}
        if condition_type is not None:
            payload["filter_type"] = condition_type
        if value is not None:
            payload["value"] = value
        if embed_field_title is not None:
            payload["embed_field_title"] = embed_field_title

        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        async with aiohttp.ClientSession() as session:
            async with session.patch(url, json=payload, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter condition not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return FilterConditionResponse(**data)
    
    async def delete_filter_condition(self, condition_id):
        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=self.headers) as resp:
                if resp.status == 400:
                    text = await resp.text()
                    raise BadRequestError(f"Bad request: {text}")
                elif resp.status == 401:
                    raise AuthenticationError("Unauthorized")
                elif resp.status == 404:
                    raise NotFoundError("Filter condition not found")
                elif resp.status == 500:
                    raise InternalServerError("Internal server error")
                elif resp.status != 200:
                    text = await resp.text()
                    raise PynqoError(f"Unexpected error ({resp.status}): {text}")

                data = await resp.json()
                return FilterConditionResponse(**data)
