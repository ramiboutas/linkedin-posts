import requests

import urllib.parse
import urllib.request

import json

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
    """Share a post in Linkedin

    Detailed parameters:

    https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/posts-api?view=li-lms-2023-08&tabs=http#post-schema


    Parameters
    ----------
    access_token : str
        Linkedin Access Token (OAuth 2.0).
        https://learn.microsoft.com/en-us/linkedin/learning/getting-started/authentication#generating-an-access-token

    comment : str
        Commentary for the post.

    author_type : str
        Author type
        Value choices: "person" or "organization"

    author_id : str | int
        Indentification of the post author

    visibility : str
        Visibility restrictions on content
        Value choices: "CONNECTIONS", "PUBLIC", "LOGGED_IN" or "CONTAINER"

    feed_distribution : str
        Specifies the feeds distributed to within LinkedIn.
        Value choices: "NONE" or "MAIN_FEED"

    reshable_disabled : bool
        Indicates whether resharing of the post has been disabled by the author.
        If this field is set to true, the post cannot be reshared in any context.
        If false, other reshare restrictions may still apply due to the post's
        visibility, container, or content type.

    """

    url = "https://api.linkedin.com/rest/posts"

    headers = {
        "Authorization": "Bearer %s" % access_token,
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

    response = requests.post(url, headers=headers, json=payload)
    return response


def delete_post(
    access_token: str,
    linkedin_id,
):
    headers = {
        "Authorization": "Bearer %s" % access_token,
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202308",
        "X-RestLi-Method": "DELETE",
    }


# Usage
# access_token = "dummycode"
# post_comment = "Check out my latest post!"

# data = json.dumps(payload).encode("utf-8")
# req = urllib.request.Request(url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# response_data = response.read().decode("utf-8")
# response = share_post(access_token, post_comment)
# print(response)
