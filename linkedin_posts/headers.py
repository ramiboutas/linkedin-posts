def build_headers(access_token: str, extra: dict = {}):
    """Builds the headers for all APIs"""

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202308",
    } | extra

    return headers
