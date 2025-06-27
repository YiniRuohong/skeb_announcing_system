import os


class Config:
    """Basic configuration for the monitor."""

    # Cookie used for authenticated Skeb requests. Example:
    # request_key=xxxxxxxx:yyyyyyyy
    SKB_COOKIE = os.getenv("SKEB_COOKIE", "")
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_FROM = 'noreply@example.com'
    EMAIL_TO = 'user@example.com'
