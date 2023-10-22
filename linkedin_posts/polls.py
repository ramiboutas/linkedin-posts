from .posts import share_post


def share_poll(
    access_token: str,
    comment: str,
    author_type: str,
    author_id: str | int,
    visibility: str = "PUBLIC",
    feed_distribution: str = "MAIN_FEED",
    reshable_disabled: str = False,
    poll_question: str = None,
    poll_options: list[str] = None,
    poll_duration: str = "THREE_DAYS",
    use_requests: bool = False,
):
    """Share a poll"""
    content = {
        "poll": {
            "question": poll_question,
            "options": [{"text": option} for option in poll_options],
            "settings": {"duration": poll_duration},
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
        _payload_content=content,
        use_requests=use_requests,
    )
