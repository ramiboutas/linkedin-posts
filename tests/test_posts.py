import os
import dotenv

dotenv.load_dotenv(".env")

from linkedin_posts.posts import share_post
from linkedin_posts.posts import delete_post

author_type = "organization"
author_id = os.environ.get("LINKEDIN_ORGANIZATION_ID")
access_token = os.environ.get("LINKEDIN_ORGANIZATION_ACCESS_TOKEN")


def test_share_and_delete_post():
    # create a post
    r_create = share_post(
        access_token=access_token,
        comment="Hello, this is just a test...",
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.getcode() == 201

    # delete it
    r_delete = delete_post(access_token, r_create.getheader("x-restli-id"))
    assert r_delete.getcode() == 204


# 'urn:li:share:7104319981684674560'
