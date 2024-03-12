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
import { BulkRunSchema } from '../models';
// @ts-ignore
import { RunBulkWorkflowSchema } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * BulkWorkflowRunsApi - axios parameter creator
 * @export
 */
export const BulkWorkflowRunsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * This endpoint retrieves the details of a specific bulk workflow run using its `bulk_run_id`.
         * @summary Get a bulk workflow run
         * @param {string} bulkRunId The ID of the bulk run to retrieve.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getBulk: async (bulkRunId: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'bulkRunId' is not null or undefined
            assertParamExists('getBulk', 'bulkRunId', bulkRunId)
            const localVarPath = `/v1/runs/bulk/{bulk_run_id}`
                .replace(`{${"bulk_run_id"}}`, encodeURIComponent(String(bulkRunId !== undefined ? bulkRunId : `-bulk_run_id-`)));
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
                pathTemplate: '/v1/runs/bulk/{bulk_run_id}',
                httpMethod: 'GET'
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided csv in bulk.
         * @summary Run a workflow in bulk
         * @param {RunBulkWorkflowSchema} runBulkWorkflowSchema 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        runBulk: async (runBulkWorkflowSchema: RunBulkWorkflowSchema, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'runBulkWorkflowSchema' is not null or undefined
            assertParamExists('runBulk', 'runBulkWorkflowSchema', runBulkWorkflowSchema)
            const localVarPath = `/v1/runs/bulk`;
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
                requestBody: runBulkWorkflowSchema,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/runs/bulk',
                httpMethod: 'POST'
            });
            localVarRequestOptions.data = serializeDataIfNeeded(runBulkWorkflowSchema, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * BulkWorkflowRunsApi - functional programming interface
 * @export
 */
export const BulkWorkflowRunsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = BulkWorkflowRunsApiAxiosParamCreator(configuration)
    return {
        /**
         * This endpoint retrieves the details of a specific bulk workflow run using its `bulk_run_id`.
         * @summary Get a bulk workflow run
         * @param {BulkWorkflowRunsApiGetBulkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getBulk(requestParameters: BulkWorkflowRunsApiGetBulkRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BulkRunSchema>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getBulk(requestParameters.bulkRunId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided csv in bulk.
         * @summary Run a workflow in bulk
         * @param {BulkWorkflowRunsApiRunBulkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async runBulk(requestParameters: BulkWorkflowRunsApiRunBulkRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BulkRunSchema>> {
            const runBulkWorkflowSchema: RunBulkWorkflowSchema = {
                workflow_id: requestParameters.workflow_id,
                input_csv_url: requestParameters.input_csv_url,
                webhook_url: requestParameters.webhook_url
            };
            const localVarAxiosArgs = await localVarAxiosParamCreator.runBulk(runBulkWorkflowSchema, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * BulkWorkflowRunsApi - factory interface
 * @export
 */
export const BulkWorkflowRunsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = BulkWorkflowRunsApiFp(configuration)
    return {
        /**
         * This endpoint retrieves the details of a specific bulk workflow run using its `bulk_run_id`.
         * @summary Get a bulk workflow run
         * @param {BulkWorkflowRunsApiGetBulkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getBulk(requestParameters: BulkWorkflowRunsApiGetBulkRequest, options?: AxiosRequestConfig): AxiosPromise<BulkRunSchema> {
            return localVarFp.getBulk(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * This endpoint lets the user run a specified workflow with the provided csv in bulk.
         * @summary Run a workflow in bulk
         * @param {BulkWorkflowRunsApiRunBulkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        runBulk(requestParameters: BulkWorkflowRunsApiRunBulkRequest, options?: AxiosRequestConfig): AxiosPromise<BulkRunSchema> {
            return localVarFp.runBulk(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getBulk operation in BulkWorkflowRunsApi.
 * @export
 * @interface BulkWorkflowRunsApiGetBulkRequest
 */
export type BulkWorkflowRunsApiGetBulkRequest = {
    
    /**
    * The ID of the bulk run to retrieve.
    * @type {string}
    * @memberof BulkWorkflowRunsApiGetBulk
    */
    readonly bulkRunId: string
    
}

/**
 * Request parameters for runBulk operation in BulkWorkflowRunsApi.
 * @export
 * @interface BulkWorkflowRunsApiRunBulkRequest
 */
export type BulkWorkflowRunsApiRunBulkRequest = {
    
} & RunBulkWorkflowSchema

/**
 * BulkWorkflowRunsApiGenerated - object-oriented interface
 * @export
 * @class BulkWorkflowRunsApiGenerated
 * @extends {BaseAPI}
 */
export class BulkWorkflowRunsApiGenerated extends BaseAPI {
    /**
     * This endpoint retrieves the details of a specific bulk workflow run using its `bulk_run_id`.
     * @summary Get a bulk workflow run
     * @param {BulkWorkflowRunsApiGetBulkRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BulkWorkflowRunsApiGenerated
     */
    public getBulk(requestParameters: BulkWorkflowRunsApiGetBulkRequest, options?: AxiosRequestConfig) {
        return BulkWorkflowRunsApiFp(this.configuration).getBulk(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * This endpoint lets the user run a specified workflow with the provided csv in bulk.
     * @summary Run a workflow in bulk
     * @param {BulkWorkflowRunsApiRunBulkRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BulkWorkflowRunsApiGenerated
     */
    public runBulk(requestParameters: BulkWorkflowRunsApiRunBulkRequest, options?: AxiosRequestConfig) {
        return BulkWorkflowRunsApiFp(this.configuration).runBulk(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
