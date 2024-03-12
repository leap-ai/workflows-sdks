/* tslint:disable */
/* eslint-disable */
/*
Leap Workflows API

The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

The version of the OpenAPI document: 1.0
Contact: help@tryleap.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction, isBrowser } from '../common';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
// @ts-ignore
import { RunWorkflowSchema } from '../models';
// @ts-ignore
import { WorkflowRunSchema } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * WorkflowRunsApi - axios parameter creator
 * @export
 */
export const WorkflowRunsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.
         * @summary Get a workflow run
         * @param {string} workflowRunId The ID of the workflow run to retrieve.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getWorkflowRun: async (workflowRunId: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'workflowRunId' is not null or undefined
            assertParamExists('getWorkflowRun', 'workflowRunId', workflowRunId)
            const localVarPath = `/v1/runs/{workflow_run_id}`
                .replace(`{${"workflow_run_id"}}`, encodeURIComponent(String(workflowRunId !== undefined ? workflowRunId : `-workflow_run_id-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication api_key required
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-Api-Key", keyParamName: "xApiKey", configuration })

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/runs/{workflow_run_id}',
                httpMethod: 'GET'
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided workflow definition.
         * @summary Run a workflow
         * @param {RunWorkflowSchema} runWorkflowSchema 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        workflow: async (runWorkflowSchema: RunWorkflowSchema, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'runWorkflowSchema' is not null or undefined
            assertParamExists('workflow', 'runWorkflowSchema', runWorkflowSchema)
            const localVarPath = `/v1/runs`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication api_key required
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-Api-Key", keyParamName: "xApiKey", configuration })

    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: runWorkflowSchema,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/runs',
                httpMethod: 'POST'
            });
            localVarRequestOptions.data = serializeDataIfNeeded(runWorkflowSchema, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * WorkflowRunsApi - functional programming interface
 * @export
 */
export const WorkflowRunsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = WorkflowRunsApiAxiosParamCreator(configuration)
    return {
        /**
         * This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.
         * @summary Get a workflow run
         * @param {WorkflowRunsApiGetWorkflowRunRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getWorkflowRun(requestParameters: WorkflowRunsApiGetWorkflowRunRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<WorkflowRunSchema>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getWorkflowRun(requestParameters.workflowRunId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided workflow definition.
         * @summary Run a workflow
         * @param {WorkflowRunsApiWorkflowRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async workflow(requestParameters: WorkflowRunsApiWorkflowRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<WorkflowRunSchema>> {
            const runWorkflowSchema: RunWorkflowSchema = {
                workflow_id: requestParameters.workflow_id,
                webhook_url: requestParameters.webhook_url,
                input: requestParameters.input
            };
            const localVarAxiosArgs = await localVarAxiosParamCreator.workflow(runWorkflowSchema, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * WorkflowRunsApi - factory interface
 * @export
 */
export const WorkflowRunsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = WorkflowRunsApiFp(configuration)
    return {
        /**
         * This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.
         * @summary Get a workflow run
         * @param {WorkflowRunsApiGetWorkflowRunRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getWorkflowRun(requestParameters: WorkflowRunsApiGetWorkflowRunRequest, options?: AxiosRequestConfig): AxiosPromise<WorkflowRunSchema> {
            return localVarFp.getWorkflowRun(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided workflow definition.
         * @summary Run a workflow
         * @param {WorkflowRunsApiWorkflowRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        workflow(requestParameters: WorkflowRunsApiWorkflowRequest, options?: AxiosRequestConfig): AxiosPromise<WorkflowRunSchema> {
            return localVarFp.workflow(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getWorkflowRun operation in WorkflowRunsApi.
 * @export
 * @interface WorkflowRunsApiGetWorkflowRunRequest
 */
export type WorkflowRunsApiGetWorkflowRunRequest = {
    
    /**
    * The ID of the workflow run to retrieve.
    * @type {string}
    * @memberof WorkflowRunsApiGetWorkflowRun
    */
    readonly workflowRunId: string
    
}

/**
 * Request parameters for workflow operation in WorkflowRunsApi.
 * @export
 * @interface WorkflowRunsApiWorkflowRequest
 */
export type WorkflowRunsApiWorkflowRequest = {
    
} & RunWorkflowSchema

/**
 * WorkflowRunsApiGenerated - object-oriented interface
 * @export
 * @class WorkflowRunsApiGenerated
 * @extends {BaseAPI}
 */
export class WorkflowRunsApiGenerated extends BaseAPI {
    /**
     * This endpoint retrieves the details of a specific workflow run using its `workflow_run_id`.
     * @summary Get a workflow run
     * @param {WorkflowRunsApiGetWorkflowRunRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WorkflowRunsApiGenerated
     */
    public getWorkflowRun(requestParameters: WorkflowRunsApiGetWorkflowRunRequest, options?: AxiosRequestConfig) {
        return WorkflowRunsApiFp(this.configuration).getWorkflowRun(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * This endpoint lets the user run a specified workflow with the provided workflow definition.
     * @summary Run a workflow
     * @param {WorkflowRunsApiWorkflowRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WorkflowRunsApiGenerated
     */
    public workflow(requestParameters: WorkflowRunsApiWorkflowRequest, options?: AxiosRequestConfig) {
        return WorkflowRunsApiFp(this.configuration).workflow(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
