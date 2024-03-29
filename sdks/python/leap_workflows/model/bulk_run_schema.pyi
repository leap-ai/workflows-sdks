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


class BulkRunSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "workflow_id",
            "input_csv_url",
            "output_csv_url",
            "created_at",
            "id",
            "version_id",
            "error",
            "row_count",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            version_id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("completed")
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("running")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
                
                @schemas.classproperty
                def QUEUED(cls):
                    return cls("queued")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("cancelled")
            created_at = schemas.StrSchema
            workflow_id = schemas.StrSchema
            input_csv_url = schemas.StrSchema
            
            
            class output_csv_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'output_csv_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class error(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            row_count = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "version_id": version_id,
                "status": status,
                "created_at": created_at,
                "workflow_id": workflow_id,
                "input_csv_url": input_csv_url,
                "output_csv_url": output_csv_url,
                "error": error,
                "row_count": row_count,
            }
    
    workflow_id: MetaOapg.properties.workflow_id
    input_csv_url: MetaOapg.properties.input_csv_url
    output_csv_url: MetaOapg.properties.output_csv_url
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    version_id: MetaOapg.properties.version_id
    error: MetaOapg.properties.error
    row_count: MetaOapg.properties.row_count
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_id"]) -> MetaOapg.properties.version_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflow_id"]) -> MetaOapg.properties.workflow_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_csv_url"]) -> MetaOapg.properties.input_csv_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_csv_url"]) -> MetaOapg.properties.output_csv_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["row_count"]) -> MetaOapg.properties.row_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "version_id", "status", "created_at", "workflow_id", "input_csv_url", "output_csv_url", "error", "row_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_id"]) -> MetaOapg.properties.version_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflow_id"]) -> MetaOapg.properties.workflow_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_csv_url"]) -> MetaOapg.properties.input_csv_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_csv_url"]) -> MetaOapg.properties.output_csv_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["row_count"]) -> MetaOapg.properties.row_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "version_id", "status", "created_at", "workflow_id", "input_csv_url", "output_csv_url", "error", "row_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workflow_id: typing.Union[MetaOapg.properties.workflow_id, str, ],
        input_csv_url: typing.Union[MetaOapg.properties.input_csv_url, str, ],
        output_csv_url: typing.Union[MetaOapg.properties.output_csv_url, None, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        version_id: typing.Union[MetaOapg.properties.version_id, str, ],
        error: typing.Union[MetaOapg.properties.error, None, str, ],
        row_count: typing.Union[MetaOapg.properties.row_count, decimal.Decimal, int, float, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BulkRunSchema':
        return super().__new__(
            cls,
            *args,
            workflow_id=workflow_id,
            input_csv_url=input_csv_url,
            output_csv_url=output_csv_url,
            created_at=created_at,
            id=id,
            version_id=version_id,
            error=error,
            row_count=row_count,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
