from .secrets import author_type, author_id, access_token

from linkedin_posts.posts import share_post, delete_post
from linkedin_posts.comments import comment_in_a_post


def test_share_a_post_and_add_a_comment():
    # create a post
    r_create = share_post(
        access_token,
        comment="Hello, this is just a test post to be commented.",
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.status_code == 201

    # Text comment
    post_urn = r_create.headers["x-restli-id"]
    r_comment = comment_in_a_post(
        access_token,
        post_urn,
        "Testing my comment",
        author_type=author_type,
        author_id=author_id,
    )
    assert r_comment.status_code == 201

    # Comment with link
    r_comment_link = comment_in_a_post(
        access_token,
        post_urn,
        "Check out my site https://ramiboutas.com/",
        author_type=author_type,
        author_id=author_id,
    )

    assert r_comment_link.status_code == 201

    # delete post
    r_delete = delete_post(access_token, post_urn)
    assert r_delete.status_code == 204
