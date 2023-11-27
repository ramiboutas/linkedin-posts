from .secrets import author_type, author_id, access_token

from linkedin_posts.posts import share_post
from linkedin_posts.posts import delete_post
from linkedin_posts.posts import share_post_with_media
from linkedin_posts.images import upload_image


def test_share_and_delete_post():
    # create a post
    r_create = share_post(
        access_token,
        comment="Hello, this is just a test...",
        author_type=author_type,
        author_id=author_id,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.status_code == 201

    # delete it
    r_delete = delete_post(access_token, r_create.headers["x-restli-id"])
    assert r_delete.status_code == 204


def test_share_and_delete_post_with_media():
    # upload a image
    response, image_urn = upload_image(
        access_token,
        file="img/nicecv.jpg",
        author_type=author_type,
        author_id=author_id,
    )

    assert response.status_code == 201

    assert "urn:li" in image_urn

    # create a post
    r_create = share_post_with_media(
        access_token,
        comment="Do you like this nice cv?",
        author_type=author_type,
        author_id=author_id,
        media_id=image_urn,
        feed_distribution="NONE",
        visibility="LOGGED_IN",
    )
    assert r_create.status_code == 201

    # delete it
    r_delete = delete_post(access_token, r_create.headers["x-restli-id"])
    assert r_delete.status_code == 204
