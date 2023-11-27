from .secrets import author_type, author_id, access_token


from linkedin_posts.polls import share_poll
from linkedin_posts.posts import delete_post


def test_share_and_delete_poll_post():
    # create a poll post
    r_create = share_poll(
        access_token,
        comment="Hello, this is just a test...",
        question="Is this is a nice poll?",
        options=["Yes", "No", "I do not care"],
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.status_code == 201

    # delete it
    r_delete = delete_post(access_token, r_create.headers["x-restli-id"])
    assert r_delete.status_code == 204
