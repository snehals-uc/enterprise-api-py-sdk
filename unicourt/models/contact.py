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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.models.address import Address
from unicourt.models.email import Email
from unicourt.models.phone import Phone
from typing import Optional, Set
from typing_extensions import Self

class Contact(BaseModel):
    """
    Contact object data schema.
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=7, strict=True, max_length=7)]] = 'Contact'
    address_array: Optional[List[Address]] = Field(default=None, description="List of available addresses.", alias="addressArray")
    phone_number_array: Optional[List[Phone]] = Field(default=None, description="List of available phone numbers.", alias="phoneNumberArray")
    email_array: Optional[List[Email]] = Field(default=None, description="List of available emails.", alias="emailArray")
    __properties: ClassVar[List[str]] = ["object", "addressArray", "phoneNumberArray", "emailArray"]

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
        """Create an instance of Contact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in address_array (list)
        _items = []
        if self.address_array:
            for _item in self.address_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addressArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in phone_number_array (list)
        _items = []
        if self.phone_number_array:
            for _item in self.phone_number_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['phoneNumberArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in email_array (list)
        _items = []
        if self.email_array:
            for _item in self.email_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['emailArray'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Contact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'Contact',
            "addressArray": [Address.from_dict(_item) for _item in obj["addressArray"]] if obj.get("addressArray") is not None else None,
            "phoneNumberArray": [Phone.from_dict(_item) for _item in obj["phoneNumberArray"]] if obj.get("phoneNumberArray") is not None else None,
            "emailArray": [Email.from_dict(_item) for _item in obj["emailArray"]] if obj.get("emailArray") is not None else None
        })
        return _obj

