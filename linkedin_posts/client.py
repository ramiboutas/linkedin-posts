"""
TODO: Future work
"""

from . import posts


class Client:
    def __init__(self, access_token, author_type, author_id) -> None:
        self.access_token = access_token
        self.author_type = author_type
        self.author_id = author_id

    def share_post(self, text="", visibility="PUBLIC", feed_distribution="MAIN"):
        return posts.share_post(
            self.access_token,
            comment=text,
            author_type=self.author_type,
            author_id=self.author_id,
            visibility=visibility,
            feed_distribution=feed_distribution,
        )

    def __str__(self) -> str:
        return "%s %s", self.author_type, self.author_id
