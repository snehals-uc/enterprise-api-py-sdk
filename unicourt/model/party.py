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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.model.attorney_representation_type import AttorneyRepresentationType
from unicourt.model.contact import Contact
from unicourt.model.party_attorney_associations import PartyAttorneyAssociations
from unicourt.model.party_role import PartyRole
from unicourt.model.possible_norm_party import PossibleNormParty
from typing import Optional, Set
from typing_extensions import Self

class Party(BaseModel):
    """
    Party
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=5, strict=True, max_length=5)]] = Field(default='Party', description="Name of the object")
    party_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="ID for the party in this case. This ID is unique within a case and NOT across cases. If the same party were to appear in another case this ID would be different.", alias="partyId")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=250)]] = Field(default=None, description="Name of the party as provided by Court.")
    name_prefix: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, alias="namePrefix")
    first_name: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="First name of the party. This is normalized by UniCourt.", alias="firstName")
    middle_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Middle name of the party. This is normalized by UniCourt.", alias="middleName")
    last_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Last name of the party. This is normalized by UniCourt.", alias="lastName")
    name_suffix: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, alias="nameSuffix")
    contact: Optional[Contact] = None
    party_classification_type: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved.", alias="partyClassificationType")
    party_role: Optional[PartyRole] = Field(default=None, alias="partyRole")
    source_party_role: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Party Type as provided by Court.", alias="sourcePartyRole")
    is_visible: Optional[StrictBool] = Field(default=None, description="Signifies if the party as this party type is currently isVisible or not for the case.", alias="isVisible")
    first_fetch_date: Optional[datetime] = Field(default=None, description="When was the party first fetched from the court site.", alias="firstFetchDate")
    last_fetch_date: Optional[datetime] = Field(default=None, description="When was the party last fetched from the court site.", alias="lastFetchDate")
    attorney_representation_type: Optional[AttorneyRepresentationType] = Field(default=None, alias="attorneyRepresentationType")
    party_attorney_associations: Optional[PartyAttorneyAssociations] = Field(default=None, alias="partyAttorneyAssociations")
    possible_norm_party_array: Optional[List[PossibleNormParty]] = Field(default=None, alias="possibleNormPartyArray")
    __properties: ClassVar[List[str]] = ["object", "partyId", "name", "namePrefix", "firstName", "middleName", "lastName", "nameSuffix", "contact", "partyClassificationType", "partyRole", "sourcePartyRole", "isVisible", "firstFetchDate", "lastFetchDate", "attorneyRepresentationType", "partyAttorneyAssociations", "possibleNormPartyArray"]

    @field_validator('party_classification_type')
    def party_classification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INDIVIDUAL', 'COMPANY', 'OTHER']):
            raise ValueError("must be one of enum values ('INDIVIDUAL', 'COMPANY', 'OTHER')")
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
        """Create an instance of Party from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of party_role
        if self.party_role:
            _dict['partyRole'] = self.party_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attorney_representation_type
        if self.attorney_representation_type:
            _dict['attorneyRepresentationType'] = self.attorney_representation_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of party_attorney_associations
        if self.party_attorney_associations:
            _dict['partyAttorneyAssociations'] = self.party_attorney_associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in possible_norm_party_array (list)
        _items = []
        if self.possible_norm_party_array:
            for _item in self.possible_norm_party_array:
                if _item:
                    _items.append(_item.to_dict())
            _dict['possibleNormPartyArray'] = _items
        # set to None if name_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.name_prefix is None and "name_prefix" in self.model_fields_set:
            _dict['namePrefix'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.middle_name is None and "middle_name" in self.model_fields_set:
            _dict['middleName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if name_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.name_suffix is None and "name_suffix" in self.model_fields_set:
            _dict['nameSuffix'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Party from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'Party',
            "partyId": obj.get("partyId"),
            "name": obj.get("name"),
            "namePrefix": obj.get("namePrefix"),
            "firstName": obj.get("firstName"),
            "middleName": obj.get("middleName"),
            "lastName": obj.get("lastName"),
            "nameSuffix": obj.get("nameSuffix"),
            "contact": Contact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "partyClassificationType": obj.get("partyClassificationType"),
            "partyRole": PartyRole.from_dict(obj["partyRole"]) if obj.get("partyRole") is not None else None,
            "sourcePartyRole": obj.get("sourcePartyRole"),
            "isVisible": obj.get("isVisible"),
            "firstFetchDate": obj.get("firstFetchDate"),
            "lastFetchDate": obj.get("lastFetchDate"),
            "attorneyRepresentationType": AttorneyRepresentationType.from_dict(obj["attorneyRepresentationType"]) if obj.get("attorneyRepresentationType") is not None else None,
            "partyAttorneyAssociations": PartyAttorneyAssociations.from_dict(obj["partyAttorneyAssociations"]) if obj.get("partyAttorneyAssociations") is not None else None,
            "possibleNormPartyArray": [PossibleNormParty.from_dict(_item) for _item in obj["possibleNormPartyArray"]] if obj.get("possibleNormPartyArray") is not None else None
        })
        return _obj

