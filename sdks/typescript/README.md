# @leap-ai/workflows

The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

[![npm](https://img.shields.io/badge/npm-v1.0.1-blue)](https://www.npmjs.com/package/@leap-ai/workflows/v/1.0.1)
[![GitHub last commit](https://img.shields.io/github/last-commit/leap-ai/workflows-sdks/tree/main/sdks/typescript.svg)](https://github.com/leap-ai/workflows-sdks/tree/main/sdks/typescript/commits)
[![More Info](https://img.shields.io/badge/More%20Info-Click%20Here-orange)](https://tryleap.ai/)

## Table of Contents

<!-- toc -->

- [Installing](#installing)
  * [npm](#npm)
  * [yarn](#yarn)
- [Getting Started](#getting-started)
- [Reference](#reference)
  * [`leap.workflowRuns.getWorkflowRun`](#leapworkflowrunsgetworkflowrun)
  * [`leap.workflowRuns.workflow`](#leapworkflowrunsworkflow)

<!-- tocstop -->

## Installing

### npm
```
npm install @leap-ai/workflows --save
```

### yarn
```
yarn add @leap-ai/workflows
```

## Getting Started

```typescript
import { Leap } from "@leap-ai/workflows";

const leap = new Leap({
  // Defining the base path is optional and defaults to https://api.workflows.tryleap.ai
  // basePath: "https://api.workflows.tryleap.ai",
  apiKey: "API_KEY",
});

const getWorkflowRunResponse = await leap.workflowRuns.getWorkflowRun({
  workflowRunId: "workflowRunId_example",
});

console.log(getWorkflowRunResponse);
```

## Reference


### `leap.workflowRuns.getWorkflowRun`

This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.

#### 🛠️ Usage

```typescript
const getWorkflowRunResponse = await leap.workflowRuns.getWorkflowRun({
  workflowRunId: "workflowRunId_example",
});
```

#### ⚙️ Parameters

##### workflowRunId: `string`

The ID of the workflow run to retrieve.

#### 🔄 Return

[WorkflowRunEntity](./models/workflow-run-entity.ts)

#### 🌐 Endpoint

`/v1/runs/{workflow_run_id}` `GET`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


### `leap.workflowRuns.workflow`

This endpoint lets the user run a specified workflow with the provided workflow definition.

#### 🛠️ Usage

```typescript
const workflowResponse = await leap.workflowRuns.workflow({
  workflow_id: "wkf_i3F5UjpZ2Vg",
  webhook_url: "https://myapp.com/webhook",
});
```

#### ⚙️ Parameters

##### workflow_id: `string`

The ID of the workflow to be run.

##### webhook_url: `string`

The URL to which the workflow results should be sent to on completion.

##### input: `{ [key: string]: any; }`

Variables that the workflow can use globally and their values.

#### 🔄 Return

[WorkflowRunEntity](./models/workflow-run-entity.ts)

#### 🌐 Endpoint

`/v1/runs` `POST`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author
This TypeScript package is automatically generated by [Konfig](https://konfigthis.com)
