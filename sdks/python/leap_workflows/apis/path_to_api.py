import typing_extensions

from leap_workflows.paths import PathValues
from leap_workflows.apis.paths.v1_runs import V1Runs
from leap_workflows.apis.paths.v1_runs_workflow_run_id import V1RunsWorkflowRunId
from leap_workflows.apis.paths.v1_runs_bulk import V1RunsBulk
from leap_workflows.apis.paths.v1_runs_bulk_bulk_run_id import V1RunsBulkBulkRunId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_RUNS: V1Runs,
        PathValues.V1_RUNS_WORKFLOW_RUN_ID: V1RunsWorkflowRunId,
        PathValues.V1_RUNS_BULK: V1RunsBulk,
        PathValues.V1_RUNS_BULK_BULK_RUN_ID: V1RunsBulkBulkRunId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_RUNS: V1Runs,
        PathValues.V1_RUNS_WORKFLOW_RUN_ID: V1RunsWorkflowRunId,
        PathValues.V1_RUNS_BULK: V1RunsBulk,
        PathValues.V1_RUNS_BULK_BULK_RUN_ID: V1RunsBulkBulkRunId,
    }
)
