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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PACERSearchReceipt(BaseModel):
    """
    PACERSearchReceipt
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default='PACERSearchReceipt', description="Name of the object")
    transaction_date: Optional[datetime] = Field(default=None, description="Date when the transaction was made at the pacer court site.", alias="transactionDate")
    search_fee: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=5)]] = Field(default=None, description="PACER Search Fee.", alias="searchFee")
    billable_pages: Optional[StrictInt] = Field(default=None, description="No of pages that was billed for the given PACER search.", alias="billablePages")
    login_id: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="ID which is used for PACER login.", alias="loginId")
    client_code: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="client code added if any was set.", alias="clientCode")
    firm_id: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Firm ID.", alias="firmId")
    search: Optional[Annotated[str, Field(strict=True, max_length=1000000)]] = Field(default=None, description="Details of the search made for this request.")
    description: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Description of the search made.")
    cso_id: Optional[Annotated[int, Field(strict=True)]] = Field(default=None, description="PACER Account ID.", alias="csoId")
    report_id: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Report ID for the search made.", alias="reportId")
    __properties: ClassVar[List[str]] = ["object", "transactionDate", "searchFee", "billablePages", "loginId", "clientCode", "firmId", "search", "description", "csoId", "reportId"]

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
        """Create an instance of PACERSearchReceipt from a JSON string"""
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
        # set to None if client_code (nullable) is None
        # and model_fields_set contains the field
        if self.client_code is None and "client_code" in self.model_fields_set:
            _dict['clientCode'] = None

        # set to None if firm_id (nullable) is None
        # and model_fields_set contains the field
        if self.firm_id is None and "firm_id" in self.model_fields_set:
            _dict['firmId'] = None

        # set to None if search (nullable) is None
        # and model_fields_set contains the field
        if self.search is None and "search" in self.model_fields_set:
            _dict['search'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if cso_id (nullable) is None
        # and model_fields_set contains the field
        if self.cso_id is None and "cso_id" in self.model_fields_set:
            _dict['csoId'] = None

        # set to None if report_id (nullable) is None
        # and model_fields_set contains the field
        if self.report_id is None and "report_id" in self.model_fields_set:
            _dict['reportId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PACERSearchReceipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PACERSearchReceipt',
            "transactionDate": obj.get("transactionDate"),
            "searchFee": obj.get("searchFee"),
            "billablePages": obj.get("billablePages"),
            "loginId": obj.get("loginId"),
            "clientCode": obj.get("clientCode"),
            "firmId": obj.get("firmId"),
            "search": obj.get("search"),
            "description": obj.get("description"),
            "csoId": obj.get("csoId"),
            "reportId": obj.get("reportId")
        })
        return _obj

