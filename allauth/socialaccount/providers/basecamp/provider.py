from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.basecamp.views import (
    BasecampOAuth2Adapter,
)
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class BasecampAccount(ProviderAccount):
    def get_avatar_url(self):
        return None

    def to_str(self):
        dflt = super(BasecampAccount, self).to_str()
        return self.account.extra_data.get("name", dflt)


class BasecampProvider(OAuth2Provider):
    id = "basecamp"
    name = "Basecamp"
    account_class = BasecampAccount
    oauth2_adapter_class = BasecampOAuth2Adapter

    def get_auth_params_from_request(self, request, action):
        data = super().get_auth_params_from_request(request, action)
        data["type"] = "web_server"
        return data

    def extract_uid(self, data):
        data = data["identity"]
        return str(data["id"])

    def extract_common_fields(self, data):
        data = data["identity"]
        return dict(
            email=data.get("email_address"),
            username=data.get("email_address"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            name="%s %s" % (data.get("first_name"), data.get("last_name")),
        )


provider_classes = [BasecampProvider]
