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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.models.case_count_analytics_by_case_type_group import CaseCountAnalyticsByCaseTypeGroup
from typing import Optional, Set
from typing_extensions import Self

class CaseCountAnalyticsByCaseTypeGroupResponse(BaseModel):
    """
    Case Counts by Case Type Group Response.
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=41)]] = 'CaseCountAnalyticsByCaseTypeGroupResponse'
    next_page_api: Optional[Annotated[str, Field(strict=True, max_length=2173)]] = Field(default=None, description="Next page of results if applicable.", alias="nextPageAPI")
    previous_page_api: Optional[Annotated[str, Field(strict=True, max_length=2172)]] = Field(default=None, description="Link to previous page of results.", alias="previousPageAPI")
    results: Optional[List[CaseCountAnalyticsByCaseTypeGroup]] = None
    total_pages: Optional[StrictInt] = Field(default=None, description="Total no. of pages.", alias="totalPages")
    total_case_count: Optional[StrictInt] = Field(default=None, description="Total no. of Cases for this criteria.", alias="totalCaseCount")
    total_case_type_group_count: Optional[StrictInt] = Field(default=None, description="Total no. of Case Type Group for this criteria.", alias="totalCaseTypeGroupCount")
    __properties: ClassVar[List[str]] = ["object", "nextPageAPI", "previousPageAPI", "results", "totalPages", "totalCaseCount", "totalCaseTypeGroupCount"]

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
        """Create an instance of CaseCountAnalyticsByCaseTypeGroupResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # set to None if next_page_api (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_api is None and "next_page_api" in self.model_fields_set:
            _dict['nextPageAPI'] = None

        # set to None if previous_page_api (nullable) is None
        # and model_fields_set contains the field
        if self.previous_page_api is None and "previous_page_api" in self.model_fields_set:
            _dict['previousPageAPI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CaseCountAnalyticsByCaseTypeGroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'CaseCountAnalyticsByCaseTypeGroupResponse',
            "nextPageAPI": obj.get("nextPageAPI"),
            "previousPageAPI": obj.get("previousPageAPI"),
            "results": [CaseCountAnalyticsByCaseTypeGroup.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "totalPages": obj.get("totalPages"),
            "totalCaseCount": obj.get("totalCaseCount"),
            "totalCaseTypeGroupCount": obj.get("totalCaseTypeGroupCount")
        })
        return _obj

