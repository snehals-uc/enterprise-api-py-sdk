# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from unicourt.models.callback_list_response_case_document_order_callbacks import CallbackListResponseCaseDocumentOrderCallbacks
from typing import Optional, Set
from typing_extensions import Self

class CallbackListResponse(BaseModel):
    """
    CallbackListResponse
    """ # noqa: E501
    object: Annotated[str, Field(min_length=20, strict=True, max_length=20)] = Field(description="Name of the object.")
    case_document_order_callbacks: CallbackListResponseCaseDocumentOrderCallbacks = Field(alias="caseDocumentOrderCallbacks")
    case_export_callbacks: CallbackListResponseCaseDocumentOrderCallbacks = Field(alias="caseExportCallbacks")
    __properties: ClassVar[List[str]] = ["object", "caseDocumentOrderCallbacks", "caseExportCallbacks"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CallbackListResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of case_document_order_callbacks
        if self.case_document_order_callbacks:
            _dict['caseDocumentOrderCallbacks'] = self.case_document_order_callbacks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of case_export_callbacks
        if self.case_export_callbacks:
            _dict['caseExportCallbacks'] = self.case_export_callbacks.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallbackListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'CallbackListResponse',
            "caseDocumentOrderCallbacks": CallbackListResponseCaseDocumentOrderCallbacks.from_dict(obj["caseDocumentOrderCallbacks"]) if obj.get("caseDocumentOrderCallbacks") is not None else None,
            "caseExportCallbacks": CallbackListResponseCaseDocumentOrderCallbacks.from_dict(obj["caseExportCallbacks"]) if obj.get("caseExportCallbacks") is not None else None
        })
        return _obj


