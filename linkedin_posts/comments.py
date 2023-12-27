# https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/comments-api?view=li-lms-2023-11&tabs=http
import json
import requests

import urllib.parse

from .headers import build_headers
from .constants import LINKEDIN_VERSION


def comment_in_a_post(
    access_token: str,
    post_urn: str,
    message_text: str,
    author_type: str,
    author_id: str | int,
    content=None,
    li_version: str = LINKEDIN_VERSION,
):
    url = f"https://api.linkedin.com/rest/socialActions/{urllib.parse.quote(post_urn)}/comments"

    headers = build_headers(access_token, li_version=li_version)

    payload = {
        "actor": f"urn:li:{author_type}:{author_id}",
        "object": post_urn,
        "message": {"text": message_text},
    }
    if content:
        # "content": [{"entity": {"image": "urn:li:image:C552CAQGu16obsGZENQ"}}],
        payload["content"] = content

    data = json.dumps(payload).encode("utf-8")

    return requests.post(url, headers=headers, data=data)
