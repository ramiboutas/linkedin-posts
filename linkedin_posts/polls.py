import json
import urllib.parse
import urllib.request

from .headers import build_headers

from .posts import share_post


def share_poll(
    access_token: str,
    comment: str,
    author_type: str,
    author_id: str | int,
    visibility: str = "PUBLIC",
    feed_distribution: str = "MAIN_FEED",
    reshable_disabled: str = False,
    question: str = None,
    options: list[str] = None,
    duration: str = "THREE_DAYS",
):
    content = {
        "poll": {
            "question": question,
            "options": [{"text": option} for option in options],
            "settings": {"duration": duration},
        }
    }

    return share_post(
        access_token=access_token,
        comment=comment,
        author_type=author_type,
        author_id=author_id,
        visibility=visibility,
        feed_distribution=feed_distribution,
        reshable_disabled=reshable_disabled,
        payload_content=content,
    )
