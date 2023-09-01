import urllib.parse
import urllib.request
import requests

import json


def get_access_token(client_id, client_secret, redirect_uri, authorization_code):
    """ """
    endpoint = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, method="POST")
    response = urllib.request.urlopen(req)
    response_data = response.read().decode("utf-8")
    access_token = json.loads(response_data)["access_token"]
    return access_token


def get_profile(access_token):
    """
    Fetches the profile of a LinkedIn user who has given you their permission to view their profile
    """
    LI_PROFILE_API_ENDPOINT = "https://api.linkedin.com/v2/me"
    r = requests.get(
        LI_PROFILE_API_ENDPOINT, headers={"Authorization": "Bearer " + access_token}
    )
    return r.json()
