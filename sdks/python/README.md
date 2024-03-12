<div align="center">

[![Visit Leap Workflows](https://raw.githubusercontent.com/leap-ai/workflows-sdks/HEAD/sdks/python/header.png)](https://www.tryleap.ai/)

# Leap Workflows<a id="leap-workflows"></a>

The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.


[![PyPI](https://img.shields.io/badge/PyPI-v2.0.2-blue)](https://pypi.org/project/leap-workflows-python-sdk/2.0.2)
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
  * [`leap.bulk_workflow_runs.get_bulk`](#leapbulk_workflow_runsget_bulk)
  * [`leap.bulk_workflow_runs.run_bulk`](#leapbulk_workflow_runsrun_bulk)
  * [`leap.workflow_runs.get_workflow_run`](#leapworkflow_runsget_workflow_run)
  * [`leap.workflow_runs.workflow`](#leapworkflow_runsworkflow)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>

```sh
pip install leap-workflows-python-sdk==2.0.2
```

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from leap_workflows import Leap, ApiException

leap = Leap(
    api_key="YOUR_API_KEY",
)

try:
    # Get a bulk workflow run
    get_bulk_response = leap.bulk_workflow_runs.get_bulk(
        bulk_run_id="bulk_9Nmenl7rxIu2FiSsnqNyTe9G",
    )
    print(get_bulk_response)
except ApiException as e:
    print("Exception when calling BulkWorkflowRunsApi.get_bulk: %s\n" % e)
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
        # Get a bulk workflow run
        get_bulk_response = await leap.bulk_workflow_runs.aget_bulk(
            bulk_run_id="bulk_9Nmenl7rxIu2FiSsnqNyTe9G",
        )
        print(get_bulk_response)
    except ApiException as e:
        print("Exception when calling BulkWorkflowRunsApi.get_bulk: %s\n" % e)
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
    # Get a bulk workflow run
    get_bulk_response = leap.bulk_workflow_runs.raw.get_bulk(
        bulk_run_id="bulk_9Nmenl7rxIu2FiSsnqNyTe9G",
    )
    pprint(get_bulk_response.body)
    pprint(get_bulk_response.body["id"])
    pprint(get_bulk_response.body["version_id"])
    pprint(get_bulk_response.body["status"])
    pprint(get_bulk_response.body["created_at"])
    pprint(get_bulk_response.body["workflow_id"])
    pprint(get_bulk_response.body["input_csv_url"])
    pprint(get_bulk_response.body["output_csv_url"])
    pprint(get_bulk_response.body["error"])
    pprint(get_bulk_response.body["row_count"])
    pprint(get_bulk_response.headers)
    pprint(get_bulk_response.status)
    pprint(get_bulk_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BulkWorkflowRunsApi.get_bulk: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `leap.bulk_workflow_runs.get_bulk`<a id="leapbulk_workflow_runsget_bulk"></a>

This endpoint retrieves the details of a specific bulk workflow run using its `bulk_run_id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bulk_response = leap.bulk_workflow_runs.get_bulk(
    bulk_run_id="bulk_9Nmenl7rxIu2FiSsnqNyTe9G",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bulk_run_id: `str`<a id="bulk_run_id-str"></a>

The ID of the bulk run to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`BulkRunSchema`](./leap_workflows/pydantic/bulk_run_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/runs/bulk/{bulk_run_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `leap.bulk_workflow_runs.run_bulk`<a id="leapbulk_workflow_runsrun_bulk"></a>

This endpoint lets the user run a specified workflow with the provided csv in bulk.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
run_bulk_response = leap.bulk_workflow_runs.run_bulk(
    workflow_id="wkf_i3F5UjpZ2Vg",
    input_csv_url="https://myapp.com/input.csv",
    webhook_url="https://myapp.com/webhook",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workflow_id: `str`<a id="workflow_id-str"></a>

The ID of the workflow to be run in bulk.

##### input_csv_url: `str`<a id="input_csv_url-str"></a>

A CSV file containing the input data for the bulk run. Each row should contain the input data for a single run.

##### webhook_url: `str`<a id="webhook_url-str"></a>

The URL to which the bulk run results should be sent to on completion.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RunBulkWorkflowSchema`](./leap_workflows/type/run_bulk_workflow_schema.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BulkRunSchema`](./leap_workflows/pydantic/bulk_run_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/runs/bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

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

[`WorkflowRunSchema`](./leap_workflows/pydantic/workflow_run_schema.py)

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

##### input: [`RunWorkflowSchemaInput`](./leap_workflows/type/run_workflow_schema_input.py)<a id="input-runworkflowschemainputleap_workflowstyperun_workflow_schema_inputpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RunWorkflowSchema`](./leap_workflows/type/run_workflow_schema.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowRunSchema`](./leap_workflows/pydantic/workflow_run_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/runs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
