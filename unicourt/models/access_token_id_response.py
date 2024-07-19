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

class AccessTokenIdResponse(BaseModel):
    """
    AccessTokenIdResponse
    """ # noqa: E501
    object: Annotated[str, Field(min_length=21, strict=True, max_length=21)] = Field(description="Name of the object.")
    token_id: Annotated[str, Field(min_length=18, strict=True, max_length=18)] = Field(description="Unique Id for the access token.", alias="tokenId")
    issued_date: datetime = Field(description="Date when access token was created.", alias="issuedDate")
    issue_address: Annotated[str, Field(min_length=7, strict=True, max_length=15)] = Field(description="Ip address.", alias="issueAddress")
    __properties: ClassVar[List[str]] = ["object", "tokenId", "issuedDate", "issueAddress"]

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
        """Create an instance of AccessTokenIdResponse from a JSON string"""
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
        """Create an instance of AccessTokenIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'AccessTokenIdResponse',
            "tokenId": obj.get("tokenId"),
            "issuedDate": obj.get("issuedDate"),
            "issueAddress": obj.get("issueAddress")
        })
        return _obj


