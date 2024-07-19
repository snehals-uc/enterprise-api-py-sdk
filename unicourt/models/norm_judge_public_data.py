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
from unicourt.models.contact import Contact
from unicourt.models.norm_judge_public_data_aba_ratings import NormJudgePublicDataAbaRatings
from unicourt.models.norm_judge_public_data_bio import NormJudgePublicDataBio
from unicourt.models.norm_judge_public_data_education_array_inner import NormJudgePublicDataEducationArrayInner
from unicourt.models.norm_judge_public_data_judicial_source import NormJudgePublicDataJudicialSource
from unicourt.models.norm_judge_public_data_name_history_array_inner import NormJudgePublicDataNameHistoryArrayInner
from unicourt.models.service_history import ServiceHistory
from typing import Optional, Set
from typing_extensions import Self

class NormJudgePublicData(BaseModel):
    """
    This contains the Judge Public details that is obtained from various sources.
    """ # noqa: E501
    object: Annotated[str, Field(strict=True, max_length=19)]
    judicial_status: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(description="The judicial status of the Judge", alias="judicialStatus")
    judicial_source: NormJudgePublicDataJudicialSource = Field(alias="judicialSource")
    aba_ratings: NormJudgePublicDataAbaRatings = Field(alias="abaRatings")
    alias_array: List[Annotated[str, Field(strict=True, max_length=250)]] = Field(description="Other Names of the Judge.", alias="aliasArray")
    bio: NormJudgePublicDataBio
    contact: Contact
    education_array: List[NormJudgePublicDataEducationArrayInner] = Field(description="The Education History of the judge.", alias="educationArray")
    professional_career_array: List[Annotated[str, Field(strict=True, max_length=2000)]] = Field(description="The non-judicial career history of the judge.", alias="professionalCareerArray")
    service_history_array: List[ServiceHistory] = Field(description="Judicial History of the Judge.", alias="serviceHistoryArray")
    name_history_array: List[NormJudgePublicDataNameHistoryArrayInner] = Field(description="Name changes of the Judge. Change in the official name. Other names go to Alias array.", alias="nameHistoryArray")
    first_fetch_date: Optional[datetime] = Field(alias="firstFetchDate")
    last_fetch_date: Optional[datetime] = Field(alias="lastFetchDate")
    last_fetch_date_with_updates: Optional[datetime] = Field(description="Last Fetch Date of the Judge Update.", alias="lastFetchDateWithUpdates")
    __properties: ClassVar[List[str]] = ["object", "judicialStatus", "judicialSource", "abaRatings", "aliasArray", "bio", "contact", "educationArray", "professionalCareerArray", "serviceHistoryArray", "nameHistoryArray", "firstFetchDate", "lastFetchDate", "lastFetchDateWithUpdates"]

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
        """Create an instance of NormJudgePublicData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of judicial_source
        if self.judicial_source:
            _dict['judicialSource'] = self.judicial_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aba_ratings
        if self.aba_ratings:
            _dict['abaRatings'] = self.aba_ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bio
        if self.bio:
            _dict['bio'] = self.bio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in education_array (list)
        _items = []
        if self.education_array:
            for _item in self.education_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['educationArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_history_array (list)
        _items = []
        if self.service_history_array:
            for _item in self.service_history_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceHistoryArray'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in name_history_array (list)
        _items = []
        if self.name_history_array:
            for _item in self.name_history_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nameHistoryArray'] = _items
        # set to None if judicial_status (nullable) is None
        # and model_fields_set contains the field
        if self.judicial_status is None and "judicial_status" in self.model_fields_set:
            _dict['judicialStatus'] = None

        # set to None if first_fetch_date (nullable) is None
        # and model_fields_set contains the field
        if self.first_fetch_date is None and "first_fetch_date" in self.model_fields_set:
            _dict['firstFetchDate'] = None

        # set to None if last_fetch_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_fetch_date is None and "last_fetch_date" in self.model_fields_set:
            _dict['lastFetchDate'] = None

        # set to None if last_fetch_date_with_updates (nullable) is None
        # and model_fields_set contains the field
        if self.last_fetch_date_with_updates is None and "last_fetch_date_with_updates" in self.model_fields_set:
            _dict['lastFetchDateWithUpdates'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormJudgePublicData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'NormJudgePublicData',
            "judicialStatus": obj.get("judicialStatus"),
            "judicialSource": NormJudgePublicDataJudicialSource.from_dict(obj["judicialSource"]) if obj.get("judicialSource") is not None else None,
            "abaRatings": NormJudgePublicDataAbaRatings.from_dict(obj["abaRatings"]) if obj.get("abaRatings") is not None else None,
            "aliasArray": obj.get("aliasArray"),
            "bio": NormJudgePublicDataBio.from_dict(obj["bio"]) if obj.get("bio") is not None else None,
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "educationArray": [NormJudgePublicDataEducationArrayInner.from_dict(_item) for _item in obj["educationArray"]] if obj.get("educationArray") is not None else None,
            "professionalCareerArray": obj.get("professionalCareerArray"),
            "serviceHistoryArray": [ServiceHistory.from_dict(_item) for _item in obj["serviceHistoryArray"]] if obj.get("serviceHistoryArray") is not None else None,
            "nameHistoryArray": [NormJudgePublicDataNameHistoryArrayInner.from_dict(_item) for _item in obj["nameHistoryArray"]] if obj.get("nameHistoryArray") is not None else None,
            "firstFetchDate": obj.get("firstFetchDate"),
            "lastFetchDate": obj.get("lastFetchDate"),
            "lastFetchDateWithUpdates": obj.get("lastFetchDateWithUpdates")
        })
        return _obj


