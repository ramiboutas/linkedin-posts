import os
import dotenv

dotenv.load_dotenv(".env")

from linkedin_posts.polls import share_poll
from linkedin_posts.posts import delete_post

author_type = "organization"
author_id = os.environ.get("LINKEDIN_ORGANIZATION_ID")
access_token = os.environ.get("LINKEDIN_ORGANIZATION_ACCESS_TOKEN")


def test_share_and_delete_poll_post():
    # create a poll post
    r_create = share_poll(
        access_token,
        comment="Hello, this is just a test...",
        poll_question="Is this is a nice poll?",
        poll_options=["Yes", "No", "I do not care"],
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.getcode() == 201

    # delete it
    r_delete = delete_post(access_token, r_create.getheader("x-restli-id"))
    assert r_delete.getcode() == 204
