# Workflows API

This document outlines how to call the new Leap workflows API.

## Authenticating Your Account

To access workflows, you first need to set up an account at `https://alpha.tryleap.ai` and generate an API key. This API key must be included in your request header under the `X-Api-Key` key to authenticate your account.

## Initiating a Workflow

Workflows can be initiated by calling the run method in the SDK, or sending a `POST` request to the following endpoint:

```text copy
https://api.workflows.tryleap.ai/v1/workflows
```

Your request body must include the following;

```json copy
{
  "workflowId": "123", // Unique ID of the workflow you want to run
  "webhookUrl": "", // Optional: The URL to receive notifications of workflow completion or failure
  "inputs": {
    "foo": "bar" // Inputs you want to pass to the workflow
  }
}
```

## Understanding the Workflow Run Object

Once a workflow is initiated, the API will immediately respond with a Workflow Run object. If you've specified a Webhook URL, this object will also be sent in the body of a `POST` request once the workflow has completed or failed.

```ts copy
{
  "id": string; // Unique ID of the workflow run
  "versionId": string; // Version of the workflow being run
  "status": "completed" | "running" | "failed"; // Current status of the workflow
  "created_at": string; // Date and time when the workflow was initiated
  "started_at": string | null; // Date and time when the workflow actually started, if applicable
  "ended_at": string | null; // Date and time when the workflow ended, if applicable
  "workflowId": string; // ID of the workflow
  "error": string | null; // Any error that occurred during the workflow, or null if the workflow completed successfully
  "input": { // Inputs used in the workflow
   [key: string]: any;
 },
  "output": unknown | null; // Output of the workflow, or null if the workflow failed
}
```

This document should help you navigate and access Leap's new workflows. Feel free to contact us if you encounter issues or have additional questions.

## Understanding Actions

When building a workflow on Leap you can create different types of actions, actions are essentially integrations on top of services which allow you to call each service with full flexibility while still benefiting.

Currently Leap supports OpenAi, Astria, and Replicate.

The schema for each of the services follows the following structure:

``` json copy
{
  "pathParams": {
    "key": "string"
  },
  "queryParams": {
    "key": "string"
  },
  "body": {
    "key": "string/number/array/object"
  }
}
```

Most services only require passing `body` into the object, and Leap handles setting the rest.

Depending on the service you choose, you may also need or want to provide `pathParams` or `queryParams`.

We purposefully keep this interface low-level to give you flexibility when interacting with services as these are constantly updated.

## The Http Utility

If you want to call a service outside of the ones that Leap provides, you will likely resort to the `HTTP Utility` action. This action enables you to call any HTTP endpoint you wish.

The interface is very similar to actions, but with the addition of the `url` and `method` and `headers` options.

``` json copy
{
  "url": "someapp.com/api",
  "method": "POST",
  "headers": {
    "key": "string"
  },
  "pathParams": {
    "key": "string"
  },
  "queryParams": {
    "key": "string"
  },
  "body": {
    "key": "string/number/array/object"
  }
}
```

## On Service Webhooks

Its important to note that if a service accepts a webhook in the aciton body (e.g. Replicate), Leap workflows makes use of this value. And will ignore your value override it regardless of what you pass in the `body`.

This is because webhooks need for the Leap engine to be aware of job completions. If you'd like to retrieve results, simply provide your `webhook url` when calling the Leap SDK or API, and not as part of step configurations.
