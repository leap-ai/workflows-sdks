# coding: utf-8

"""
    Leap Workflows API

    The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

    The version of the OpenAPI document: 1.0
    Contact: help@tryleap.ai
    Created by: https://tryleap.ai/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredBulkRunSchema(TypedDict):
    id: str

    version_id: str

    status: str

    created_at: str

    workflow_id: str

    input_csv_url: str

    output_csv_url: typing.Optional[str]

    error: typing.Optional[str]

    row_count: typing.Union[int, float]

class OptionalBulkRunSchema(TypedDict, total=False):
    pass

class BulkRunSchema(RequiredBulkRunSchema, OptionalBulkRunSchema):
    pass
