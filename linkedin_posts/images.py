"""
This module takes care of Linkedin Images API
"""
import json
import urllib.parse
import urllib.request

from .headers import build_headers


# TODO: try to remove this dependency: requests
# use alternative=True in func upload_image to test with urllib!
import requests


def _init_upload(access_token, author_type, author_id):
    """Initialize Image Upload"""
    url = "https://api.linkedin.com/rest/images?action=initializeUpload"
    headers = build_headers(access_token)
    author = "urn:li:%s:%s" % (author_type, author_id)
    payload = {"initializeUploadRequest": {"owner": author}}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    response = urllib.request.urlopen(req)
    response_data = response.read().decode("utf-8")
    value_dict = json.loads(response_data)["value"]
    return (value_dict["uploadUrl"], value_dict["image"])


def upload_image(access_token, author_type, author_id, fileb: bytes, alternative=False):
    """Upload an image

    Parameters
    ----------
    access_token : str
        Linkedin Access Token (OAuth 2.0).

    author_type : str
        Author type
        Value choices: "person" or "organization"

    author_id : str | int
        Indentification of the post author

    Returns
    -------
    A tupple:
        (requests.models.Response object, image_urn:str)

    """

    upload_url, image_urn = _init_upload(access_token, author_type, author_id)
    headers = {"Authorization": "Bearer " + access_token}

    if alternative:
        return _alternative_upload(upload_url, headers, fileb)

    response = requests.put(upload_url, headers=headers, data=fileb)
    return response, image_urn


def _alternative_upload(url, headers, data):
    ########################################
    ########################################
    ########## For testing purposes #######
    ########################################
    ########################################
    request = urllib.request.Request(url, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(request) as response:
            response_content = response.read()
            return response, response_content
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e}")
        raise e
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
        raise e


def get_image(access_token, image_urn: str):
    """Get a single image

    Parameters
    ----------
    access_token : str
        Linkedin Access Token (OAuth 2.0).

    image_urn : str
        Linkedin image identification

    Returns
    -------
    A tupple:
        (http.client.HTTPResponse object, data:dict)

    """
    headers = build_headers(access_token)
    url = f"https://api.linkedin.com/rest/images/{urllib.parse.quote(image_urn)}"
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode("utf-8"))
    return response, data
