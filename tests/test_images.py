import os
import dotenv

dotenv.load_dotenv(".env")

from linkedin_posts.images import upload_image

author_type = "organization"
author_id = os.environ.get("LINKEDIN_ORGANIZATION_ID")
access_token = os.environ.get("LINKEDIN_ORGANIZATION_ACCESS_TOKEN")


def test_upload_image():
    response, image_urn = upload_image(
        access_token,
        file="docs/img/nicecv.jpg",
        author_type=author_type,
        author_id=author_id,
    )

    assert response.status_code == 201

    assert "urn:li" in image_urn
