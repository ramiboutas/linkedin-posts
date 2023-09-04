import re


def escape_little_text(text: str):
    """Escape Characters reserved for little elements.

    Little attributes (mentions, hashtags) are not supported.

    Parameters
    ----------
    text : str
        Text to be escaped

    """
    return re.sub(r"([,{}@[]()<>#*_~])", r"\\\1", text)
