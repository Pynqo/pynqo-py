import requests 
from ..exceptions import *
from ..models.filter_conditions import FilterConditionResponse, FilterConditionListResponse

class FilterConditionsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def get_filter_conditions(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterConditionListResponse(**resp.json())
    
    def create_filter_condition(self, filter_id, condition_type, filter_value, embed_field_title=None):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        body = {
            "type": condition_type,
            "filter_value": filter_value
        }
        if embed_field_title is not None:
            body["embed_field_title"] = embed_field_title
            
        resp = requests.post(url, headers=self.headers, json=body)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterConditionResponse(resp.json())
    
    def delete_filter_conditions(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}/conditions"
        resp = requests.delete(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return resp.json()
    
    def get_filter_condition(self, condition_id):
        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter condition not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterConditionResponse(**resp.json())
    
    def update_filter_condition(self, condition_id, condition_type=None, filter_value=None, embed_field_title=None):
        if condition_type is None and filter_value is None and embed_field_title is None:
            raise ValueError("At least one field must be provided for update.")

        payload = {}
        if condition_type is not None:
            payload["type"] = condition_type
        if filter_value is not None:
            payload["filter_value"] = filter_value
        if embed_field_title is not None:
            payload["embed_field_title"] = embed_field_title

        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        resp = requests.patch(url, json=payload, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter condition not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterConditionResponse(**resp.json())
    
    def delete_filter_condition(self, condition_id):
        url = f"{self.baseUrl}/filter-conditions/{condition_id}"
        resp = requests.delete(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Filter condition not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterConditionResponse(**resp.json())
