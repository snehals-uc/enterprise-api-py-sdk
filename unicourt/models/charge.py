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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Charge(BaseModel):
    """
    Charge
    """ # noqa: E501
    object: Annotated[str, Field(min_length=6, strict=True, max_length=6)]
    charge_id: Annotated[str, Field(min_length=18, strict=True, max_length=18)] = Field(alias="chargeId")
    charge_group_id: Annotated[str, Field(min_length=18, strict=True, max_length=18)] = Field(alias="chargeGroupId")
    charge_group: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(alias="chargeGroup")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    created_date: datetime = Field(description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.", alias="createdDate")
    __properties: ClassVar[List[str]] = ["object", "chargeId", "chargeGroupId", "chargeGroup", "name", "createdDate"]

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
        """Create an instance of Charge from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Charge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'Charge',
            "chargeId": obj.get("chargeId"),
            "chargeGroupId": obj.get("chargeGroupId"),
            "chargeGroup": obj.get("chargeGroup"),
            "name": obj.get("name"),
            "createdDate": obj.get("createdDate")
        })
        return _obj


