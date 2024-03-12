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


class RequiredWorkflowRunSchema(TypedDict):
    id: str

    version_id: str

    status: str

    created_at: str

    started_at: typing.Optional[str]

    ended_at: typing.Optional[str]

    workflow_id: str

    error: typing.Optional[str]

    input: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    output: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class OptionalWorkflowRunSchema(TypedDict, total=False):
    pass

class WorkflowRunSchema(RequiredWorkflowRunSchema, OptionalWorkflowRunSchema):
    pass
