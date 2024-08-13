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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.case_analytics_api import CaseAnalyticsAPI
from unicourt.model.individual import Individual
from unicourt.model.norm_organization import NormOrganization
from unicourt.model.party_analytics_api import PartyAnalyticsAPI
from unicourt.model.related_norm_party import RelatedNormParty
from typing import Optional, Set
from typing_extensions import Self

class NormParty(BaseModel):
    """
    Norm Party
    """ # noqa: E501
    object: Optional[Annotated[str, Field(strict=True, max_length=9)]] = 'NormParty'
    norm_party_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="normPartyId")
    name: Optional[Annotated[str, Field(strict=True, max_length=500)]] = None
    party_classification_type: Optional[Annotated[str, Field(strict=True, max_length=12)]] = Field(default=None, alias="partyClassificationType")
    case_search_api: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="caseSearchAPI")
    case_analytics_api: Optional[CaseAnalyticsAPI] = Field(default=None, alias="caseAnalyticsAPI")
    individual_data: Optional[Individual] = Field(default=None, alias="individualData")
    norm_organization_data: Optional[NormOrganization] = Field(default=None, alias="normOrganizationData")
    party_analytics_api: Optional[PartyAnalyticsAPI] = Field(default=None, alias="partyAnalyticsAPI")
    related_norm_party_array: Optional[List[RelatedNormParty]] = Field(default=None, alias="relatedNormPartyArray")
    __properties: ClassVar[List[str]] = ["object", "normPartyId", "name", "partyClassificationType", "caseSearchAPI", "caseAnalyticsAPI", "individualData", "normOrganizationData", "partyAnalyticsAPI", "relatedNormPartyArray"]

    @field_validator('party_classification_type')
    def party_classification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Individual', 'Organization']):
            raise ValueError("must be one of enum values ('Individual', 'Organization')")
        return value

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
        """Create an instance of NormParty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of case_analytics_api
        if self.case_analytics_api:
            _dict['caseAnalyticsAPI'] = self.case_analytics_api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of individual_data
        if self.individual_data:
            _dict['individualData'] = self.individual_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of norm_organization_data
        if self.norm_organization_data:
            _dict['normOrganizationData'] = self.norm_organization_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of party_analytics_api
        if self.party_analytics_api:
            _dict['partyAnalyticsAPI'] = self.party_analytics_api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_norm_party_array (list)
        _items = []
        if self.related_norm_party_array:
            for _item in self.related_norm_party_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedNormPartyArray'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormParty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'NormParty',
            "normPartyId": obj.get("normPartyId"),
            "name": obj.get("name"),
            "partyClassificationType": obj.get("partyClassificationType"),
            "caseSearchAPI": obj.get("caseSearchAPI"),
            "caseAnalyticsAPI": CaseAnalyticsAPI.from_dict(obj["caseAnalyticsAPI"]) if obj.get("caseAnalyticsAPI") is not None else None,
            "individualData": Individual.from_dict(obj["individualData"]) if obj.get("individualData") is not None else None,
            "normOrganizationData": NormOrganization.from_dict(obj["normOrganizationData"]) if obj.get("normOrganizationData") is not None else None,
            "partyAnalyticsAPI": PartyAnalyticsAPI.from_dict(obj["partyAnalyticsAPI"]) if obj.get("partyAnalyticsAPI") is not None else None,
            "relatedNormPartyArray": [RelatedNormParty.from_dict(_item) for _item in obj["relatedNormPartyArray"]] if obj.get("relatedNormPartyArray") is not None else None
        })
        return _obj


