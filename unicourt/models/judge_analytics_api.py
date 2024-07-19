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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class JudgeAnalyticsAPI(BaseModel):
    """
    JudgeAnalyticsAPI
    """ # noqa: E501
    object: Annotated[str, Field(strict=True, max_length=17)]
    norm_judge_api: Annotated[str, Field(strict=True, max_length=255)] = Field(description="Link to Details for the Judge.", alias="normJudgeAPI")
    associated_norm_attorneys_api: Annotated[str, Field(strict=True, max_length=255)] = Field(alias="associatedNormAttorneysAPI")
    associated_norm_law_firms_api: Annotated[str, Field(strict=True, max_length=255)] = Field(alias="associatedNormLawFirmsAPI")
    associated_norm_parties_api: Annotated[str, Field(strict=True, max_length=255)] = Field(alias="associatedNormPartiesAPI")
    __properties: ClassVar[List[str]] = ["object", "normJudgeAPI", "associatedNormAttorneysAPI", "associatedNormLawFirmsAPI", "associatedNormPartiesAPI"]

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
        """Create an instance of JudgeAnalyticsAPI from a JSON string"""
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
        """Create an instance of JudgeAnalyticsAPI from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'JudgeAnalyticsAPI',
            "normJudgeAPI": obj.get("normJudgeAPI"),
            "associatedNormAttorneysAPI": obj.get("associatedNormAttorneysAPI"),
            "associatedNormLawFirmsAPI": obj.get("associatedNormLawFirmsAPI"),
            "associatedNormPartiesAPI": obj.get("associatedNormPartiesAPI")
        })
        return _obj


