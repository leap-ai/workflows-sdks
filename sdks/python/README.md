<div align="center">

[![Visit Leap Workflows](https://raw.githubusercontent.com/leap-ai/workflows-sdks/HEAD/sdks/python/header.png)](https://www.tryleap.ai/)

# Leap Workflows<a id="leap-workflows"></a>

The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.


[![PyPI](https://img.shields.io/badge/PyPI-v2.0.1-blue)](https://pypi.org/project/leap-workflows-python-sdk/2.0.1)
[![README.md](https://img.shields.io/badge/README-Click%20Here-green)](https://github.com/leap-ai/workflows-sdks/tree/main/sdks/python#readme)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://tryleap.ai/)

</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`leap.workflow_runs.get_workflow_run`](#leapworkflow_runsget_workflow_run)
  * [`leap.workflow_runs.workflow`](#leapworkflow_runsworkflow)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>

```sh
pip install leap-workflows-python-sdk==2.0.1
```

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from leap_workflows import Leap, ApiException

leap = Leap(
    api_key="YOUR_API_KEY",
)

try:
    # Get a workflow run
    get_workflow_run_response = leap.workflow_runs.get_workflow_run(
        workflow_run_id="rnp_x3p27VQk6MyJfLe",
    )
    print(get_workflow_run_response)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi.get_workflow_run: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from leap_workflows import Leap, ApiException

leap = Leap(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Get a workflow run
        get_workflow_run_response = await leap.workflow_runs.aget_workflow_run(
            workflow_run_id="rnp_x3p27VQk6MyJfLe",
        )
        print(get_workflow_run_response)
    except ApiException as e:
        print("Exception when calling WorkflowRunsApi.get_workflow_run: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from leap_workflows import Leap, ApiException

leap = Leap(
    api_key="YOUR_API_KEY",
)

try:
    # Get a workflow run
    get_workflow_run_response = leap.workflow_runs.raw.get_workflow_run(
        workflow_run_id="rnp_x3p27VQk6MyJfLe",
    )
    pprint(get_workflow_run_response.body)
    pprint(get_workflow_run_response.body["id"])
    pprint(get_workflow_run_response.body["version_id"])
    pprint(get_workflow_run_response.body["status"])
    pprint(get_workflow_run_response.body["created_at"])
    pprint(get_workflow_run_response.body["started_at"])
    pprint(get_workflow_run_response.body["ended_at"])
    pprint(get_workflow_run_response.body["workflow_id"])
    pprint(get_workflow_run_response.body["error"])
    pprint(get_workflow_run_response.body["input"])
    pprint(get_workflow_run_response.body["output"])
    pprint(get_workflow_run_response.headers)
    pprint(get_workflow_run_response.status)
    pprint(get_workflow_run_response.round_trip_time)
except ApiException as e:
    print("Exception when calling WorkflowRunsApi.get_workflow_run: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `leap.workflow_runs.get_workflow_run`<a id="leapworkflow_runsget_workflow_run"></a>

This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workflow_run_response = leap.workflow_runs.get_workflow_run(
    workflow_run_id="rnp_x3p27VQk6MyJfLe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_run_id: `str`<a id="workflow_run_id-str"></a>

The ID of the workflow run to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowRunEntity`](./leap_workflows/pydantic/workflow_run_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/runs/{workflow_run_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `leap.workflow_runs.workflow`<a id="leapworkflow_runsworkflow"></a>

This endpoint lets the user run a specified workflow with the provided workflow definition.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workflow_response = leap.workflow_runs.workflow(
    workflow_id="wkf_i3F5UjpZ2Vg",
    webhook_url="https://myapp.com/webhook",
    input={
        "first_name": "Sam",
        "last_name": "Altman",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_id: `str`<a id="workflow_id-str"></a>

The ID of the workflow to be run.

##### webhook_url: `str`<a id="webhook_url-str"></a>

The URL to which the workflow results should be sent to on completion.

##### input: [`RunWorkflowDtoInput`](./leap_workflows/type/run_workflow_dto_input.py)<a id="input-runworkflowdtoinputleap_workflowstyperun_workflow_dto_inputpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RunWorkflowDto`](./leap_workflows/type/run_workflow_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowRunEntity`](./leap_workflows/pydantic/workflow_run_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/runs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
