from .api import KeywordsAPI, ChannelsAPI, UserChannelsAPI, GuildsAPI, UsersAPI, CategoriesAPI, FiltersAPI, FilterConditionsAPI

class PynqoClient:
    def __init__(self, token: str, url="https://api.pynqo.com/db/v1"):
        self.token = token
        self.baseUrl = url
        self.headers = self._auth_headers()
        self.keywords = KeywordsAPI(self.baseUrl, self.headers)
        self.channels = ChannelsAPI(self.baseUrl, self.headers)
        self.user_channels = UserChannelsAPI(self.baseUrl, self.headers)
        self.guilds = GuildsAPI(self.baseUrl, self.headers)
        self.users = UsersAPI(self.baseUrl, self.headers)
        self.categories = CategoriesAPI(self.baseUrl, self.headers)
        self.filters = FiltersAPI(self.baseUrl, self.headers)
        self.filter_conditions = FilterConditionsAPI(self.baseUrl, self.headers)

    def _auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
    