# coding: utf-8

"""
    Leap Workflows API

    The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

    The version of the OpenAPI document: 1.0
    Contact: help@tryleap.ai
    Created by: https://tryleap.ai/
"""

from leap_workflows.paths.v1_runs_bulk_bulk_run_id.get import GetBulk
from leap_workflows.paths.v1_runs_bulk.post import RunBulk
from leap_workflows.apis.tags.bulk_workflow_runs_api_raw import BulkWorkflowRunsApiRaw


class BulkWorkflowRunsApi(
    GetBulk,
    RunBulk,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BulkWorkflowRunsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BulkWorkflowRunsApiRaw(api_client)
