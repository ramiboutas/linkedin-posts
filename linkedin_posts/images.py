"""
This module takes care of Linkedin Images API
"""
import json
import urllib.parse
import urllib.request

from .headers import build_headers


def _init_upload(headers: dict, author: str):
    """Initialize Image Upload"""
    url = "https://api.linkedin.com/rest/images?action=initializeUpload"
    payload = {"initializeUploadRequest": {"owner": author}}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    response = urllib.request.urlopen(req)
    response_data = response.read().decode("utf-8")
    value_dict = json.loads(response_data)["value"]
    return (
        value_dict["uploadUrlExpiresAt"],
        value_dict["uploadUrl"],
        value_dict["image"],
    )


def upload_image(access_token, author_type, author_id, file_bytes: bytes):
    """Upload an image"""
    headers = build_headers(access_token)
    author = "urn:li:%s:%s" % (author_type, author_id)
    _, url, image_urn = _init_upload(headers, author)
    req = urllib.request.Request(url, data=file_bytes, headers=headers, method="PUT")
    response = urllib.request.urlopen(req)
    return response, image_urn


def get_image(access_token, image_urn: str):
    """Get a single image"""
    headers = build_headers(access_token)
    url = f"https://api.linkedin.com/rest/images/{urllib.parse.quote(image_urn)}"
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    response_data = response.read().decode("utf-8")
    return response, json.loads(response_data)
