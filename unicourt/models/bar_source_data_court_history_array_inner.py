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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class BarSourceDataCourtHistoryArrayInner(BaseModel):
    """
    BarSourceDataCourtHistoryArrayInner
    """ # noqa: E501
    action: Optional[Annotated[str, Field(strict=True, max_length=250)]] = None
    action_comments: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, alias="actionComments")
    reinstated_date: Optional[datetime] = Field(default=None, alias="reinstatedDate")
    start_date: Optional[datetime] = Field(default=None, alias="startDate")
    __properties: ClassVar[List[str]] = ["action", "actionComments", "reinstatedDate", "startDate"]

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
        """Create an instance of BarSourceDataCourtHistoryArrayInner from a JSON string"""
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
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if action_comments (nullable) is None
        # and model_fields_set contains the field
        if self.action_comments is None and "action_comments" in self.model_fields_set:
            _dict['actionComments'] = None

        # set to None if reinstated_date (nullable) is None
        # and model_fields_set contains the field
        if self.reinstated_date is None and "reinstated_date" in self.model_fields_set:
            _dict['reinstatedDate'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BarSourceDataCourtHistoryArrayInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "actionComments": obj.get("actionComments"),
            "reinstatedDate": obj.get("reinstatedDate"),
            "startDate": obj.get("startDate")
        })
        return _obj

