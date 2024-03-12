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
from pydantic import BaseModel, Field, RootModel


class RunBulkWorkflowSchema(BaseModel):
    # The ID of the workflow to be run in bulk.
    workflow_id: str = Field(alias='workflow_id')

    # A CSV file containing the input data for the bulk run. Each row should contain the input data for a single run.
    input_csv_url: str = Field(alias='input_csv_url')

    # The URL to which the bulk run results should be sent to on completion.
    webhook_url: typing.Optional[str] = Field(None, alias='webhook_url')
    class Config:
        arbitrary_types_allowed = True
