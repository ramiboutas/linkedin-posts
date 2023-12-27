"""
This module takes care of Linkedin Images API and Upload Assets
"""
import json
import requests
import urllib.parse
import urllib.request
from pathlib import Path

from .headers import build_headers
from .exceptions import FileInputNotSupported
from .constants import LINKEDIN_VERSION


def _init_upload(
    access_token,
    author_type,
    author_id,
    li_version: str = LINKEDIN_VERSION,
):
    """Initialize Image Upload"""
    url = "https://api.linkedin.com/rest/images?action=initializeUpload"
    headers = build_headers(access_token, li_version=li_version)
    author = f"urn:li:{author_type}:{author_id}"
    payload = {"initializeUploadRequest": {"owner": author}}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode("utf-8")
    value_dict = json.loads(response_data)["value"]
    return (value_dict["uploadUrl"], value_dict["image"])


def upload_image(
    access_token,
    author_type,
    author_id,
    file: bytes | Path | str,
    li_version: str = LINKEDIN_VERSION,
):
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

    file : bytes | Path | str
        file input either in bytes or as pathlib.Path object or as string to the local path

    Returns
    -------
    A tupple:
        (requests.models.Response object, image_urn:str)

    """

    if isinstance(file, bytes):
        fileb = file
    elif isinstance(file, Path) or isinstance(file, str):
        with open(file, "rb") as f:
            fileb = f.read()
    else:
        raise FileInputNotSupported

    upload_url, image_urn = _init_upload(
        access_token,
        author_type,
        author_id,
        li_version=li_version,
    )
    headers = {"Authorization": "Bearer " + access_token}

    response = requests.put(upload_url, headers=headers, data=fileb)
    return response, image_urn


def get_image(
    access_token,
    image_urn: str,
    li_version: str = LINKEDIN_VERSION,
):
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
    headers = build_headers(access_token, li_version=li_version)
    url = f"https://api.linkedin.com/rest/images/{urllib.parse.quote(image_urn)}"
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode("utf-8"))
    return response, data
