import json
import urllib.parse
import urllib.request

from .formats import escape_little_text
from .headers import build_headers


def share_post(
    access_token: str,
    comment: str,
    author_type: str,
    author_id: str | int,
    visibility: str = "PUBLIC",
    feed_distribution: str = "MAIN_FEED",
    reshable_disabled: str = False,
    _payload_content=None,
):
    """Share a post

    Parameters
    ----------
    access_token : str
        Linkedin Access Token (OAuth 2.0).

    comment : str
        Commentary for the post.

    author_type : str
        Author type
        Value choices: "person" or "organization"

    author_id : str | int
        Indentification of the post author

    visibility : str
        Visibility restrictions on content
        Default:
        Value choices: "CONNECTIONS", "PUBLIC", "LOGGED_IN" or Container URN

    feed_distribution : str
        Specifies the feeds distributed to within LinkedIn.
        Value choices: "NONE" or "MAIN_FEED"

    reshable_disabled : bool
        Indicates whether resharing of the post has been disabled by the author.
        If this field is set to true, the post cannot be reshared in any context.
        If false, other reshare restrictions may still apply due to the post's
        visibility, container, or content type.

    Returns
    -------
    http.client.HTTPResponse object

    """

    url = "https://api.linkedin.com/rest/posts"

    headers = build_headers(access_token)

    payload = {
        "author": "urn:li:%s:%s" % (author_type, author_id),
        "commentary": escape_little_text(comment),
        "visibility": visibility,
        "distribution": {
            "feedDistribution": feed_distribution,
            "targetEntities": [],  # Not implemented
            "thirdPartyDistributionChannels": [],  # Not implemented
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": reshable_disabled,
    }

    if _payload_content:
        payload["content"] = _payload_content

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as response:
        return response


def delete_post(access_token: str, urn: str):
    """Delete a post

    Parameters
    ----------
    access_token : str
        Linkedin Access Token (OAuth 2.0).

    urn : str
        Linkedin post identification (ugcPostUrn or shareUrn)
        Example "urn:li:share:6844785523593134080"

    Returns
    -------
    http.client.HTTPResponse object

    """

    url = "https://api.linkedin.com/rest/posts/%s" % urllib.parse.quote(urn)
    headers = build_headers(access_token, extra={"X-RestLi-Method": "DELETE"})
    req = urllib.request.Request(url, headers=headers, method="DELETE")
    with urllib.request.urlopen(req) as response:
        return response


def share_post_with_media(
    access_token: str,
    comment: str,
    author_type: str,
    author_id: str | int,
    media_id: str,
    media_title: str = None,
    visibility: str = "PUBLIC",
    feed_distribution: str = "MAIN_FEED",
    reshable_disabled: str = False,
):
    """Share a post with media content"""

    content = {"media": {"id": media_id}}

    if media_title:
        content["media"]["title"] = media_title

    return share_post(
        access_token=access_token,
        comment=comment,
        author_type=author_type,
        author_id=author_id,
        visibility=visibility,
        feed_distribution=feed_distribution,
        reshable_disabled=reshable_disabled,
        _payload_content=content,
    )
