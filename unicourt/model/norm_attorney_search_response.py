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
from unicourt.model.norm_attorney_search_result import NormAttorneySearchResult
from typing import Optional, Set
from typing_extensions import Self

class NormAttorneySearchResponse(BaseModel):
    """
    NormAttorneySearchResponse
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=26, strict=True, max_length=26)]] = 'NormAttorneySearchResponse'
    norm_attorney_search_result_array: Optional[List[NormAttorneySearchResult]] = Field(default=None, alias="normAttorneySearchResultArray")
    q: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=2048)]] = Field(default=None, description="Query been sent by client")
    norm_attorney_search_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="Query been sent by client", alias="normAttorneySearchId")
    next_page_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2120)]] = Field(default=None, description="Link to next page.", alias="nextPageAPI")
    previous_page_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2119)]] = Field(default=None, description="Link to previous page.", alias="previousPageAPI")
    page_number: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="pageNumber")
    total_pages: Optional[StrictInt] = Field(default=None, description="Total pages for matches that were found in the index.", alias="totalPages")
    total_count: Optional[StrictInt] = Field(default=None, description="The number of matches that were found in the index.", alias="totalCount")
    __properties: ClassVar[List[str]] = ["object", "normAttorneySearchResultArray", "q", "normAttorneySearchId", "nextPageAPI", "previousPageAPI", "pageNumber", "totalPages", "totalCount"]

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
        """Create an instance of NormAttorneySearchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in norm_attorney_search_result_array (list)
        _items = []
        if self.norm_attorney_search_result_array:
            for _item in self.norm_attorney_search_result_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['normAttorneySearchResultArray'] = _items
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
        """Create an instance of NormAttorneySearchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'NormAttorneySearchResponse',
            "normAttorneySearchResultArray": [NormAttorneySearchResult.from_dict(_item) for _item in obj["normAttorneySearchResultArray"]] if obj.get("normAttorneySearchResultArray") is not None else None,
            "q": obj.get("q"),
            "normAttorneySearchId": obj.get("normAttorneySearchId"),
            "nextPageAPI": obj.get("nextPageAPI"),
            "previousPageAPI": obj.get("previousPageAPI"),
            "pageNumber": obj.get("pageNumber"),
            "totalPages": obj.get("totalPages"),
            "totalCount": obj.get("totalCount")
        })
        return _obj


