# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from leap_workflows.paths.v1_runs_bulk import Api

from leap_workflows.paths import PathValues

path = PathValues.V1_RUNS_BULK