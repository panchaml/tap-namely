"""Namely tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_namely.streams import (
    ProfileStream,
    CompanyStream,
)

STREAM_TYPES = [
    ProfileStream,
    CompanyStream,
]


class TapNamely(Tap):
    """Namely tap class."""
    name = "tap-namely"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "authorization",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://{subdomain}.namely.com/api/v1",
            required=False,
            description="The url for the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
