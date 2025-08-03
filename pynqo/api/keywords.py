import requests 
from ..exceptions import *
from ..models.keyword import *

class KeywordsAPI:
    def __init__(self, base_url, headers):
        self.baseUrl = base_url
        self.headers = headers

    def list(self):
        url = f"{self.baseUrl}/keywords"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 400:
            raise BadRequestError(f"Bad request: {resp.text}")
        elif resp.status_code == 401:
            raise AuthenticationError("Unauthorized")
        elif resp.status_code == 500:
            raise InternalServerError("Internal server error")
        elif not resp.ok:
            raise PynqoError(f"Unexpected error ({resp.status_code}): {resp.text}")

        return KeywordListResponse(**resp.json())
    
    def list_user(self, member_id):
        url = f"{self.baseUrl}/users/{member_id}/keywords"
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

        return KeywordListResponse(**resp.json())
    
    def add_keyword(self, member_id, keyword):
        url = f"{self.baseUrl}/users/{member_id}/keywords"
        body = {
            "keyword": keyword,
            "excludes": [],
            "sizes": [],
            "use_pushover": False
        }
        resp = requests.post(url, headers=self.headers, json=body)

        if resp.status_code == 400:
            try:
                error_data = resp.json()
                if "already exists" in error_data.get("message", ""):
                    raise BadRequestError("Keyword already exists for this user and guild")
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

        return KeywordResponse(**resp.json())
    
    def delete_keyword(self, keyword_id):
        url = f"{self.baseUrl}/keywords/{keyword_id}"
        resp = requests.delete(url, headers=self.headers)

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

        return True
    
    def edit_keyword(self, keyword_id, keyword=None, use_pushover=None):
        if keyword is None and use_pushover is None:
            raise ValueError("At least 'keyword' or 'use_pushover' must be provided.")

        payload = {}
        if keyword is not None:
            payload["keyword"] = keyword
        if use_pushover is not None:
            payload["use_pushover"] = use_pushover

        url = f"{self.baseUrl}/keywords/{keyword_id}"
        resp = requests.patch(url, json=payload, headers=self.headers)
        if resp.status_code == 400:
            try:
                error_data = resp.json()
                if "already exists" in error_data.get("message", ""):
                    raise BadRequestError("Keyword already exists for this user and guild")
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

        return KeywordResponse(**resp.json())
    