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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from unicourt.models.exception import Exception
from typing import Optional, Set
from typing_extensions import Self

class DocumentDownload(BaseModel):
    """
    DocumentDownload
    """ # noqa: E501
    object: Optional[Annotated[str, Field(min_length=16, strict=True, max_length=16)]] = Field(default='DocumentDownload', description="Name of the object.")
    case_document_id: Optional[Annotated[str, Field(min_length=18, strict=True, max_length=18)]] = Field(default=None, description="Requested Document ID.", alias="caseDocumentId")
    expiry_date: Optional[Annotated[str, Field(min_length=25, strict=True, max_length=25)]] = Field(default=None, description="Expiry date-time for the fileUrl provided in this object.", alias="expiryDate")
    file_url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1024)]] = Field(default=None, description="Link to download the file.", alias="fileUrl")
    case_document_download_api: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1024)]] = Field(default=None, description="API call to download the document again if the above fileUrl is expired.", alias="caseDocumentDownloadAPI")
    exception: Optional[Exception] = None
    __properties: ClassVar[List[str]] = ["object", "caseDocumentId", "expiryDate", "fileUrl", "caseDocumentDownloadAPI", "exception"]

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
        """Create an instance of DocumentDownload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of exception
        if self.exception:
            _dict['exception'] = self.exception.to_dict()
        # set to None if expiry_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_date is None and "expiry_date" in self.model_fields_set:
            _dict['expiryDate'] = None

        # set to None if file_url (nullable) is None
        # and model_fields_set contains the field
        if self.file_url is None and "file_url" in self.model_fields_set:
            _dict['fileUrl'] = None

        # set to None if case_document_download_api (nullable) is None
        # and model_fields_set contains the field
        if self.case_document_download_api is None and "case_document_download_api" in self.model_fields_set:
            _dict['caseDocumentDownloadAPI'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentDownload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'DocumentDownload',
            "caseDocumentId": obj.get("caseDocumentId"),
            "expiryDate": obj.get("expiryDate"),
            "fileUrl": obj.get("fileUrl"),
            "caseDocumentDownloadAPI": obj.get("caseDocumentDownloadAPI"),
            "exception": Exception.from_dict(obj["exception"]) if obj.get("exception") is not None else None
        })
        return _obj


