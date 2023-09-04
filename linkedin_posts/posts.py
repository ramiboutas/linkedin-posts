import json

import urllib.parse
import urllib.request

from .formats import escape_little_text


def share_post(
    access_token: str,
    comment: str,
    author_type: str,
    author_id: str | int,
    visibility: str = "PUBLIC",
    feed_distribution: str = "MAIN_FEED",
    reshable_disabled: str = False,
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
        Value choices: "CONNECTIONS", "PUBLIC", "LOGGED_IN" or "CONTAINER"

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

    endpoint = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202308",
    }

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

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
    response = urllib.request.urlopen(req)
    return response


def delete_post(
    access_token: str,
    urn: str,
):
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

    headers = {
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202308",
        "X-RestLi-Method": "DELETE",
        "Authorization": "Bearer " + access_token,
    }

    endpoint = f"https://api.linkedin.com/rest/posts/{urllib.parse.quote(urn)}"
    req = urllib.request.Request(endpoint, headers=headers, method="DELETE")
    response = urllib.request.urlopen(req)
    return response
