# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.api.case_export_api import CaseExportApi


class TestCaseExportApi(unittest.TestCase):
    """CaseExportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CaseExportApi()

    def tearDown(self) -> None:
        pass

    def test_export_case(self) -> None:
        """Test case for export_case

        Gets case exported for a requested Case ID.
        """
        pass

    def test_get_case_export_callback_by_id(self) -> None:
        """Test case for get_case_export_callback_by_id

        Get Case Export Callback for a requested Case Export Callback Id.
        """
        pass

    def test_get_case_export_callbacks(self) -> None:
        """Test case for get_case_export_callbacks

        Get Case Export Callback list for a requested Date.
        """
        pass


if __name__ == '__main__':
    unittest.main()
