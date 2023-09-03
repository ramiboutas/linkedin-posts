import os
import dotenv

dotenv.load_dotenv(".env")

from linkedin_posts.posts import share_post
from linkedin_posts.posts import delete_post

author_type = "organization"
author_id = os.environ.get("LINKEDIN_ORGANIZATION_ID")
access_token = os.environ.get("LINKEDIN_ORGANIZATION_ACCESS_TOKEN")


def test_share_and_delete_post():
    r = share_post(
        access_token=access_token,
        comment="Hello, this is just a test...",
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )

    assert r.status_code == 201

    delete_post(access_token=access_token, linkedin_id=r.headers["x-restli-id"])
