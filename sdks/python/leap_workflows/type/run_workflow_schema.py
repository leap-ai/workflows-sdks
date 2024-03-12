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

from leap_workflows.type.run_workflow_schema_input import RunWorkflowSchemaInput

class RequiredRunWorkflowSchema(TypedDict):
    # The ID of the workflow to be run.
    workflow_id: str

class OptionalRunWorkflowSchema(TypedDict, total=False):
    # The URL to which the workflow results should be sent to on completion.
    webhook_url: str

    input: RunWorkflowSchemaInput

class RunWorkflowSchema(RequiredRunWorkflowSchema, OptionalRunWorkflowSchema):
    pass
