import urllib.parse
import urllib.request

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
