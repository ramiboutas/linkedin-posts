import re


def escape_little_text(text: str):
    """Escape Characters reserved for little elements.

    Little attributes (mentions, hashtags) are not supported.

    https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/little-text-format?view=li-lms-2023-08#text


    Parameters
    ----------
    text : str
        Text to be escaped

    """
    return re.sub(r"([,{}@[]()<>#*_~])", r"\\\1", text)
