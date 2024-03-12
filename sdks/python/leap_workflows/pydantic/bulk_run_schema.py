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


class BulkRunSchema(BaseModel):
    id: str = Field(alias='id')

    version_id: str = Field(alias='version_id')

    status: Literal["completed", "running", "failed"] = Field(alias='status')

    created_at: str = Field(alias='created_at')

    workflow_id: str = Field(alias='workflow_id')

    input_csv_url: str = Field(alias='input_csv_url')

    output_csv_url: typing.Optional[str] = Field(alias='output_csv_url')

    error: typing.Optional[str] = Field(alias='error')

    row_count: typing.Union[int, float] = Field(alias='row_count')
    class Config:
        arbitrary_types_allowed = True
