# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_update_request import CaseUpdateRequest

class TestCaseUpdateRequest(unittest.TestCase):
    """CaseUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseUpdateRequest:
        """Test CaseUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseUpdateRequest`
        """
        model = CaseUpdateRequest()
        if include_optional:
            return CaseUpdateRequest(
                case_id = '01234567891011121314151617',
                pacer_options = unicourt.models.case_update_pacer_options.CaseUpdatePacerOptions(
                    pacer_user_id = '012345', 
                    pacer_client_code = '', 
                    fetch_participants_if_older_than_days = 0, 
                    refresh_type = 'fetchNewDocketEntries', 
                    additional_page_array = [
                        unicourt.models.case_update_pacer_options_additional_page_array_inner.CaseUpdatePacerOptions_additionalPageArray_inner(
                            page = 'associatedCases', 
                            fetch_if_older_than_days = 0, )
                        ], )
            )
        else:
            return CaseUpdateRequest(
                case_id = '01234567891011121314151617',
        )
        """

    def testCaseUpdateRequest(self):
        """Test CaseUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
