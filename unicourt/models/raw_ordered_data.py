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
from unicourt.models.raw_ordered_data_child import RawOrderedDataChild
from typing import Optional, Set
from typing_extensions import Self

class RawOrderedData(BaseModel):
    """
    RawOrderedData
    """ # noqa: E501
    child_array: List[RawOrderedDataChild] = Field(description="Any docket text that belongs to the main docket text is added in the child.", alias="childArray")
    lbl: Optional[Annotated[str, Field(strict=True, max_length=100000)]] = Field(description="Label of the docket from the source.")
    ord: StrictInt = Field(description="Structure order")
    val: Optional[Annotated[str, Field(strict=True, max_length=1000000)]] = Field(description="List of available addresses.")
    __properties: ClassVar[List[str]] = ["childArray", "lbl", "ord", "val"]

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
        """Create an instance of RawOrderedData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in child_array (list)
        _items = []
        if self.child_array:
            for _item in self.child_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['childArray'] = _items
        # set to None if lbl (nullable) is None
        # and model_fields_set contains the field
        if self.lbl is None and "lbl" in self.model_fields_set:
            _dict['lbl'] = None

        # set to None if val (nullable) is None
        # and model_fields_set contains the field
        if self.val is None and "val" in self.model_fields_set:
            _dict['val'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RawOrderedData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "childArray": [RawOrderedDataChild.from_dict(_item) for _item in obj["childArray"]] if obj.get("childArray") is not None else None,
            "lbl": obj.get("lbl"),
            "ord": obj.get("ord"),
            "val": obj.get("val")
        })
        return _obj


