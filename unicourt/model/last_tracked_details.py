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
from unicourt.model.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from unicourt.model.exception import Exception
from typing import Optional, Set
from typing_extensions import Self

class LastTrackedDetails(BaseModel):
    """
    LastTrackedDetails
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default='LastTrackedDetails', description="Name of the object.")
    pacer_options: Optional[CaseUpdatePacerOptionsResponse] = Field(default=None, alias="pacerOptions")
    last_track_date: Optional[datetime] = Field(default=None, description="The date and time when the case was tracked for this account.", alias="lastTrackDate")
    last_track_exception: Optional[Exception] = Field(default=None, alias="lastTrackException")
    __properties: ClassVar[List[str]] = ["object", "pacerOptions", "lastTrackDate", "lastTrackException"]

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
        """Create an instance of LastTrackedDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pacer_options
        if self.pacer_options:
            _dict['pacerOptions'] = self.pacer_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_track_exception
        if self.last_track_exception:
            _dict['lastTrackException'] = self.last_track_exception.to_dict()
        # set to None if last_track_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_track_date is None and "last_track_date" in self.model_fields_set:
            _dict['lastTrackDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LastTrackedDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'LastTrackedDetails',
            "pacerOptions": CaseUpdatePacerOptionsResponse.from_dict(obj["pacerOptions"]) if obj.get("pacerOptions") is not None else None,
            "lastTrackDate": obj.get("lastTrackDate"),
            "lastTrackException": Exception.from_dict(obj["lastTrackException"]) if obj.get("lastTrackException") is not None else None
        })
        return _obj

