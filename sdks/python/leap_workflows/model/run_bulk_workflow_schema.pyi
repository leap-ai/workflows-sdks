# coding: utf-8

"""
    Leap Workflows API

    The Leap Workflows API allows developers to run workflows, fetch workflow runs, and provide other utility functions related to workflow runs. Please use the X-Api-Key for authenticated requests.

    The version of the OpenAPI document: 1.0
    Contact: help@tryleap.ai
    Created by: https://tryleap.ai/
"""

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


class RunBulkWorkflowSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "workflow_id",
            "input_csv_url",
        }
        
        class properties:
            workflow_id = schemas.StrSchema
            input_csv_url = schemas.StrSchema
            webhook_url = schemas.StrSchema
            __annotations__ = {
                "workflow_id": workflow_id,
                "input_csv_url": input_csv_url,
                "webhook_url": webhook_url,
            }
    
    workflow_id: MetaOapg.properties.workflow_id
    input_csv_url: MetaOapg.properties.input_csv_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflow_id"]) -> MetaOapg.properties.workflow_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_csv_url"]) -> MetaOapg.properties.input_csv_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook_url"]) -> MetaOapg.properties.webhook_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["workflow_id", "input_csv_url", "webhook_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflow_id"]) -> MetaOapg.properties.workflow_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_csv_url"]) -> MetaOapg.properties.input_csv_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook_url"]) -> typing.Union[MetaOapg.properties.webhook_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["workflow_id", "input_csv_url", "webhook_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workflow_id: typing.Union[MetaOapg.properties.workflow_id, str, ],
        input_csv_url: typing.Union[MetaOapg.properties.input_csv_url, str, ],
        webhook_url: typing.Union[MetaOapg.properties.webhook_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RunBulkWorkflowSchema':
        return super().__new__(
            cls,
            *args,
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            webhook_url=webhook_url,
            _configuration=_configuration,
            **kwargs,
        )