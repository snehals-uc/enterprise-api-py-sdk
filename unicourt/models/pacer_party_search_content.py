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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.models.pacer_case_search_content import PACERCaseSearchContent
from typing import Optional, Set
from typing_extensions import Self

class PACERPartySearchContent(BaseModel):
    """
    PACERPartySearchContent
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=23, strict=True, max_length=23)]] = Field(default='PACERPartySearchContent', description="Name of the object")
    pcl_jurisdiction_type: Optional[StrictStr] = Field(default=None, description="Link to case in the case management/electronic case files (CM/ECF) system at the court.", alias="pclJurisdictionType")
    pcl_case_id: Optional[StrictInt] = Field(default=None, description="Sequentially generated number that identifies the case.", alias="pclCaseId")
    pcl_case_number_full: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Case Number.", alias="pclCaseNumberFull")
    pcl_case_title: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Title of the case.", alias="pclCaseTitle")
    pcl_case_office: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="The divisional office in which the case was filed.", alias="pclCaseOffice")
    pcl_case_number: Optional[StrictInt] = Field(default=None, description="The sequence number of the case.", alias="pclCaseNumber")
    pcl_case_type: Optional[Annotated[str, Field(strict=True, max_length=6)]] = Field(default=None, description="Code that identifies the type of case.", alias="pclCaseType")
    pcl_case_year: Optional[StrictInt] = Field(default=None, description="The year in which the case falls. Could be two or four digit.", alias="pclCaseYear")
    pcl_court_id: Optional[Annotated[str, Field(strict=True, max_length=6)]] = Field(default=None, description="The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B", alias="pclCourtId")
    pcl_date_filed: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="Filing date of the case.", alias="pclDateFiled")
    pcl_last_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="This parameter represents the last name of the case when it is present", alias="pclLastName")
    pcl_first_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="This parameter represents the first name of the case when it is present", alias="pclFirstName")
    pcl_middle_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="This parameter represents the middle name of the case when it is present", alias="pclMiddleName")
    pcl_generation: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="This parameter represents the generation of the case when it is present", alias="pclGeneration")
    pcl_party_role: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="This parameter represents the party role of the case when it is present", alias="pclPartyRole")
    pcl_party_type: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="This parameter represents the party type of the case when it is present", alias="pclPartyType")
    pcl_court_case: Optional[PACERCaseSearchContent] = Field(default=None, alias="pclCourtCase")
    __properties: ClassVar[List[str]] = ["object", "pclJurisdictionType", "pclCaseId", "pclCaseNumberFull", "pclCaseTitle", "pclCaseOffice", "pclCaseNumber", "pclCaseType", "pclCaseYear", "pclCourtId", "pclDateFiled", "pclLastName", "pclFirstName", "pclMiddleName", "pclGeneration", "pclPartyRole", "pclPartyType", "pclCourtCase"]

    @field_validator('pcl_jurisdiction_type')
    def pcl_jurisdiction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Appellate', 'Bankruptcy', 'Criminal', 'Civil', 'Multi-district Litigation', 'null']):
            raise ValueError("must be one of enum values ('Appellate', 'Bankruptcy', 'Criminal', 'Civil', 'Multi-district Litigation', 'null')")
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
        """Create an instance of PACERPartySearchContent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pcl_court_case
        if self.pcl_court_case:
            _dict['pclCourtCase'] = self.pcl_court_case.to_dict()
        # set to None if pcl_jurisdiction_type (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_jurisdiction_type is None and "pcl_jurisdiction_type" in self.model_fields_set:
            _dict['pclJurisdictionType'] = None

        # set to None if pcl_case_number_full (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_case_number_full is None and "pcl_case_number_full" in self.model_fields_set:
            _dict['pclCaseNumberFull'] = None

        # set to None if pcl_case_title (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_case_title is None and "pcl_case_title" in self.model_fields_set:
            _dict['pclCaseTitle'] = None

        # set to None if pcl_case_office (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_case_office is None and "pcl_case_office" in self.model_fields_set:
            _dict['pclCaseOffice'] = None

        # set to None if pcl_case_type (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_case_type is None and "pcl_case_type" in self.model_fields_set:
            _dict['pclCaseType'] = None

        # set to None if pcl_court_id (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_court_id is None and "pcl_court_id" in self.model_fields_set:
            _dict['pclCourtId'] = None

        # set to None if pcl_date_filed (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_date_filed is None and "pcl_date_filed" in self.model_fields_set:
            _dict['pclDateFiled'] = None

        # set to None if pcl_last_name (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_last_name is None and "pcl_last_name" in self.model_fields_set:
            _dict['pclLastName'] = None

        # set to None if pcl_first_name (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_first_name is None and "pcl_first_name" in self.model_fields_set:
            _dict['pclFirstName'] = None

        # set to None if pcl_middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_middle_name is None and "pcl_middle_name" in self.model_fields_set:
            _dict['pclMiddleName'] = None

        # set to None if pcl_generation (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_generation is None and "pcl_generation" in self.model_fields_set:
            _dict['pclGeneration'] = None

        # set to None if pcl_party_role (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_party_role is None and "pcl_party_role" in self.model_fields_set:
            _dict['pclPartyRole'] = None

        # set to None if pcl_party_type (nullable) is None
        # and model_fields_set contains the field
        if self.pcl_party_type is None and "pcl_party_type" in self.model_fields_set:
            _dict['pclPartyType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PACERPartySearchContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'PACERPartySearchContent',
            "pclJurisdictionType": obj.get("pclJurisdictionType"),
            "pclCaseId": obj.get("pclCaseId"),
            "pclCaseNumberFull": obj.get("pclCaseNumberFull"),
            "pclCaseTitle": obj.get("pclCaseTitle"),
            "pclCaseOffice": obj.get("pclCaseOffice"),
            "pclCaseNumber": obj.get("pclCaseNumber"),
            "pclCaseType": obj.get("pclCaseType"),
            "pclCaseYear": obj.get("pclCaseYear"),
            "pclCourtId": obj.get("pclCourtId"),
            "pclDateFiled": obj.get("pclDateFiled"),
            "pclLastName": obj.get("pclLastName"),
            "pclFirstName": obj.get("pclFirstName"),
            "pclMiddleName": obj.get("pclMiddleName"),
            "pclGeneration": obj.get("pclGeneration"),
            "pclPartyRole": obj.get("pclPartyRole"),
            "pclPartyType": obj.get("pclPartyType"),
            "pclCourtCase": PACERCaseSearchContent.from_dict(obj["pclCourtCase"]) if obj.get("pclCourtCase") is not None else None
        })
        return _obj


