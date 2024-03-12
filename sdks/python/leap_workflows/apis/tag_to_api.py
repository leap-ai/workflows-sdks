import typing_extensions

from leap_workflows.apis.tags import TagValues
from leap_workflows.apis.tags.workflow_runs_api import WorkflowRunsApi
from leap_workflows.apis.tags.bulk_workflow_runs_api import BulkWorkflowRunsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WORKFLOW_RUNS: WorkflowRunsApi,
        TagValues.BULK_WORKFLOW_RUNS: BulkWorkflowRunsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WORKFLOW_RUNS: WorkflowRunsApi,
        TagValues.BULK_WORKFLOW_RUNS: BulkWorkflowRunsApi,
    }
)
