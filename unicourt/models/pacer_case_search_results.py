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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.models.case_search_result import CaseSearchResult
from unicourt.models.pacer_case_search_content import PACERCaseSearchContent
from typing import Optional, Set
from typing_extensions import Self

class PACERCaseSearchResults(BaseModel):
    """
    PACERCaseSearchResults
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=22, strict=True, max_length=22)]] = Field(default='PACERCaseSearchResults', description="Name of the object")
    pacer_content: Optional[PACERCaseSearchContent] = Field(default=None, alias="pacerContent")
    has_only_meta_info: Optional[StrictBool] = Field(default=None, description="This field determines if the UniCourt Content has only meta information. If the value is true and you require to get the latest updates of the case you will need to make a request to the updateCase API.", alias="hasOnlyMetaInfo")
    uni_court_content: Optional[CaseSearchResult] = Field(default=None, alias="uniCourtContent")
    __properties: ClassVar[List[str]] = ["object", "pacerContent", "hasOnlyMetaInfo", "uniCourtContent"]

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
        """Create an instance of PACERCaseSearchResults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pacer_content
        if self.pacer_content:
            _dict['pacerContent'] = self.pacer_content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uni_court_content
        if self.uni_court_content:
            _dict['uniCourtContent'] = self.uni_court_content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PACERCaseSearchResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PACERCaseSearchResults',
            "pacerContent": PACERCaseSearchContent.from_dict(obj["pacerContent"]) if obj.get("pacerContent") is not None else None,
            "hasOnlyMetaInfo": obj.get("hasOnlyMetaInfo"),
            "uniCourtContent": CaseSearchResult.from_dict(obj["uniCourtContent"]) if obj.get("uniCourtContent") is not None else None
        })
        return _obj


