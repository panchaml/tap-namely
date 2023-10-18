"""Stream type classes for tap-namely."""
from singer_sdk import typing as th   # JSON Schema typing helpers

from tap_namely.client import NamelyStream

# Note: More Streams based on the requirement can be added by specifying the schema.


class ProfileStream(NamelyStream):

    """Define custom stream."""
    streams='profile'
    name = "profiles"
    path = "/profiles"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property('profiles', th.StringType),
        th.Property('meta', th.StringType),
    ).to_dict()



class CompanyStream(NamelyStream):

    streams='company'
    """Define custom stream."""
    name = "companies"
    path = "/companies/info"
    primary_keys = ["name"]
    replication_key = None
    # Note: You can add more fields to the schema for extraction
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("permalink", th.StringType),
    ).to_dict()
