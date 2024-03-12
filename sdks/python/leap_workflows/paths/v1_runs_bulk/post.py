# coding: utf-8

"""
    Leap Workflows API

    The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

    The version of the OpenAPI document: 1.0
    Contact: help@tryleap.ai
    Created by: https://tryleap.ai/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from leap_workflows.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from leap_workflows.api_response import AsyncGeneratorResponse
from leap_workflows import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from leap_workflows import schemas  # noqa: F401

from leap_workflows.model.run_bulk_workflow_schema import RunBulkWorkflowSchema as RunBulkWorkflowSchemaSchema
from leap_workflows.model.bulk_run_schema import BulkRunSchema as BulkRunSchemaSchema

from leap_workflows.type.bulk_run_schema import BulkRunSchema
from leap_workflows.type.run_bulk_workflow_schema import RunBulkWorkflowSchema

from ...api_client import Dictionary
from leap_workflows.pydantic.bulk_run_schema import BulkRunSchema as BulkRunSchemaPydantic
from leap_workflows.pydantic.run_bulk_workflow_schema import RunBulkWorkflowSchema as RunBulkWorkflowSchemaPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = RunBulkWorkflowSchemaSchema


request_body_run_bulk_workflow_schema = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = BulkRunSchemaSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BulkRunSchema


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BulkRunSchema


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _run_bulk_mapped_args(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if workflow_id is not None:
            _body["workflow_id"] = workflow_id
        if input_csv_url is not None:
            _body["input_csv_url"] = input_csv_url
        if webhook_url is not None:
            _body["webhook_url"] = webhook_url
        args.body = _body
        return args

    async def _arun_bulk_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Run a workflow in bulk
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/runs/bulk',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_run_bulk_workflow_schema.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _run_bulk_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Run a workflow in bulk
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/runs/bulk',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_run_bulk_workflow_schema.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RunBulkRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arun_bulk(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._run_bulk_mapped_args(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
        )
        return await self._arun_bulk_oapg(
            body=args.body,
            **kwargs,
        )
    
    def run_bulk(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._run_bulk_mapped_args(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
        )
        return self._run_bulk_oapg(
            body=args.body,
        )

class RunBulk(BaseApi):

    async def arun_bulk(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> BulkRunSchemaPydantic:
        raw_response = await self.raw.arun_bulk(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
            **kwargs,
        )
        if validate:
            return BulkRunSchemaPydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkRunSchemaPydantic, raw_response.body)
    
    
    def run_bulk(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
        validate: bool = False,
    ) -> BulkRunSchemaPydantic:
        raw_response = self.raw.run_bulk(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
        )
        if validate:
            return BulkRunSchemaPydantic(**raw_response.body)
        return api_client.construct_model_instance(BulkRunSchemaPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._run_bulk_mapped_args(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
        )
        return await self._arun_bulk_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        workflow_id: str,
        input_csv_url: str,
        webhook_url: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._run_bulk_mapped_args(
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
        )
        return self._run_bulk_oapg(
            body=args.body,
        )

