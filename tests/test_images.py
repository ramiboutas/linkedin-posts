from .secrets import author_type, author_id, access_token

from linkedin_posts.images import upload_image


def test_upload_image():
    response, image_urn = upload_image(
        access_token,
        file="img/nicecv.jpg",
        author_type=author_type,
        author_id=author_id,
    )

    assert response.status_code == 201

    assert "urn:li" in image_urn
