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
from unicourt.models.pacer_party_search_results import PACERPartySearchResults
from unicourt.models.pacer_search_page_info import PACERSearchPageInfo
from unicourt.models.pacer_search_receipt import PACERSearchReceipt
from typing import Optional, Set
from typing_extensions import Self

class PCLParty(BaseModel):
    """
    PCLParty
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=8, strict=True, max_length=8)]] = Field(default='PCLParty', description="Name of the object")
    page_number: Optional[StrictInt] = Field(default=None, description="Page number for which results where obtained.", alias="pageNumber")
    pacer_receipt: Optional[PACERSearchReceipt] = Field(default=None, alias="pacerReceipt")
    pacer_page_info: Optional[PACERSearchPageInfo] = Field(default=None, alias="pacerPageInfo")
    pacer_search_results_array: Optional[List[PACERPartySearchResults]] = Field(default=None, alias="pacerSearchResultsArray")
    next_page_api: Optional[Annotated[str, Field(strict=True, max_length=1000000)]] = Field(default=None, description="Link to next page of the PCL Search Results.", alias="nextPageAPI")
    total_pages: Optional[StrictInt] = Field(default=None, description="Total number of pages to obtain all the objects the current PCL Search.", alias="totalPages")
    total_count: Optional[StrictInt] = Field(default=None, description="Total number of records available for this Search.", alias="totalCount")
    __properties: ClassVar[List[str]] = ["object", "pageNumber", "pacerReceipt", "pacerPageInfo", "pacerSearchResultsArray", "nextPageAPI", "totalPages", "totalCount"]

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
        """Create an instance of PCLParty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pacer_receipt
        if self.pacer_receipt:
            _dict['pacerReceipt'] = self.pacer_receipt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pacer_page_info
        if self.pacer_page_info:
            _dict['pacerPageInfo'] = self.pacer_page_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pacer_search_results_array (list)
        _items = []
        if self.pacer_search_results_array:
            for _item in self.pacer_search_results_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pacerSearchResultsArray'] = _items
        # set to None if next_page_api (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_api is None and "next_page_api" in self.model_fields_set:
            _dict['nextPageAPI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PCLParty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PCLParty',
            "pageNumber": obj.get("pageNumber"),
            "pacerReceipt": PACERSearchReceipt.from_dict(obj["pacerReceipt"]) if obj.get("pacerReceipt") is not None else None,
            "pacerPageInfo": PACERSearchPageInfo.from_dict(obj["pacerPageInfo"]) if obj.get("pacerPageInfo") is not None else None,
            "pacerSearchResultsArray": [PACERPartySearchResults.from_dict(_item) for _item in obj["pacerSearchResultsArray"]] if obj.get("pacerSearchResultsArray") is not None else None,
            "nextPageAPI": obj.get("nextPageAPI"),
            "totalPages": obj.get("totalPages"),
            "totalCount": obj.get("totalCount")
        })
        return _obj


