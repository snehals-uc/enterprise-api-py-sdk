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
from unicourt.models.additional_levels import AdditionalLevels
from typing import Optional, Set
from typing_extensions import Self

class Court(BaseModel):
    """
    Court
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=5, strict=True, max_length=5)]] = 'Court'
    court_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="courtId")
    court_type_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="courtTypeId")
    court_system_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, alias="courtSystemId")
    type: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    system: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    name_aka: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="nameAka")
    additional_levels: Optional[AdditionalLevels] = Field(default=None, alias="additionalLevels")
    container_type: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="containerType")
    container: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    created_date: Optional[datetime] = Field(default=None, description="The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.", alias="createdDate")
    jurisdiction_geo_for_court_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="jurisdictionGeoForCourtAPI")
    court_locations_for_court_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="courtLocationsForCourtAPI")
    appeal_courts_for_court_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, alias="appealCourtsForCourtAPI")
    court_service_status_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2048)]] = Field(default=None, alias="courtServiceStatusAPI")
    __properties: ClassVar[List[str]] = ["object", "courtId", "courtTypeId", "courtSystemId", "type", "system", "name", "nameAka", "additionalLevels", "containerType", "container", "createdDate", "jurisdictionGeoForCourtAPI", "courtLocationsForCourtAPI", "appealCourtsForCourtAPI", "courtServiceStatusAPI"]

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
        """Create an instance of Court from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_levels
        if self.additional_levels:
            _dict['additionalLevels'] = self.additional_levels.to_dict()
        # set to None if container_type (nullable) is None
        # and model_fields_set contains the field
        if self.container_type is None and "container_type" in self.model_fields_set:
            _dict['containerType'] = None

        # set to None if container (nullable) is None
        # and model_fields_set contains the field
        if self.container is None and "container" in self.model_fields_set:
            _dict['container'] = None

        # set to None if jurisdiction_geo_for_court_api (nullable) is None
        # and model_fields_set contains the field
        if self.jurisdiction_geo_for_court_api is None and "jurisdiction_geo_for_court_api" in self.model_fields_set:
            _dict['jurisdictionGeoForCourtAPI'] = None

        # set to None if court_locations_for_court_api (nullable) is None
        # and model_fields_set contains the field
        if self.court_locations_for_court_api is None and "court_locations_for_court_api" in self.model_fields_set:
            _dict['courtLocationsForCourtAPI'] = None

        # set to None if appeal_courts_for_court_api (nullable) is None
        # and model_fields_set contains the field
        if self.appeal_courts_for_court_api is None and "appeal_courts_for_court_api" in self.model_fields_set:
            _dict['appealCourtsForCourtAPI'] = None

        # set to None if court_service_status_api (nullable) is None
        # and model_fields_set contains the field
        if self.court_service_status_api is None and "court_service_status_api" in self.model_fields_set:
            _dict['courtServiceStatusAPI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Court from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'Court',
            "courtId": obj.get("courtId"),
            "courtTypeId": obj.get("courtTypeId"),
            "courtSystemId": obj.get("courtSystemId"),
            "type": obj.get("type"),
            "system": obj.get("system"),
            "name": obj.get("name"),
            "nameAka": obj.get("nameAka"),
            "additionalLevels": AdditionalLevels.from_dict(obj["additionalLevels"]) if obj.get("additionalLevels") is not None else None,
            "containerType": obj.get("containerType"),
            "container": obj.get("container"),
            "createdDate": obj.get("createdDate"),
            "jurisdictionGeoForCourtAPI": obj.get("jurisdictionGeoForCourtAPI"),
            "courtLocationsForCourtAPI": obj.get("courtLocationsForCourtAPI"),
            "appealCourtsForCourtAPI": obj.get("appealCourtsForCourtAPI"),
            "courtServiceStatusAPI": obj.get("courtServiceStatusAPI")
        })
        return _obj


