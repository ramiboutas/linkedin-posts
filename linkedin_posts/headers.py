from linkedin_posts.constants import LINKEDIN_VERSION


def build_headers(
    access_token: str,
    extra: dict = {},
    li_version: str = LINKEDIN_VERSION,
):
    """Builds the headers for all APIs"""

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": li_version,
    } | extra

    return headers
