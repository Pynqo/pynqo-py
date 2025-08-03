import requests 
from ..exceptions import *
from ..models.filters import FilterResponse, FilterListResponse

class FiltersAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def get_keyword_filters(self, keyword_id):
        url = f"{self.baseUrl}/keywords/{keyword_id}/filters"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Keyword not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterListResponse(**resp.json())
    
    def create_keyword_filter(self, keyword_id, filter_name):
        url = f"{self.baseUrl}/keywords/{keyword_id}/filters"
        body = {
            "filter_name": filter_name
        }
        resp = requests.post(url, headers=self.headers, json=body)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Keyword not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterResponse(**resp.json())
    
    def delete_keyword_filters(self, keyword_id):
        url = f"{self.baseUrl}/keywords/{keyword_id}/filters"
        resp = requests.delete(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 404:
            raise NotFoundError("Keyword not found")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return FilterListResponse(**resp.json())
    
    def get_filter(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}"
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

        return FilterResponse(**resp.json())
    
    def update_filter(self, filter_id, filter_name):
        url = f"{self.baseUrl}/filters/{filter_id}"
        body = {
            "filter_name": filter_name
        }
        resp = requests.patch(url, headers=self.headers, json=body)
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

        return FilterResponse(**resp.json())
    
    def delete_filter(self, filter_id):
        url = f"{self.baseUrl}/filters/{filter_id}"
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

        return FilterResponse(**resp.json())

