# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_count_analytics_by_norm_party_response import CaseCountAnalyticsByNormPartyResponse

class TestCaseCountAnalyticsByNormPartyResponse(unittest.TestCase):
    """CaseCountAnalyticsByNormPartyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseCountAnalyticsByNormPartyResponse:
        """Test CaseCountAnalyticsByNormPartyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseCountAnalyticsByNormPartyResponse`
        """
        model = CaseCountAnalyticsByNormPartyResponse()
        if include_optional:
            return CaseCountAnalyticsByNormPartyResponse(
                object = 'CaseCountAnalyticsByNormPartyResponse',
                results = [
                    unicourt.models.case_count_analytics_by_norm_party.CaseCountAnalyticsByNormParty(
                        object = 'CaseCountAnalyticsByNormParty', 
                        norm_party_id = '01234567891011121314151617', 
                        norm_party_name = '', 
                        case_search_api = '', 
                        case_count = 56, )
                    ],
                next_page_api = '',
                previous_page_api = '',
                total_pages = 56,
                total_case_count = 56,
                total_norm_party_count = 56
            )
        else:
            return CaseCountAnalyticsByNormPartyResponse(
                object = 'CaseCountAnalyticsByNormPartyResponse',
                results = [
                    unicourt.models.case_count_analytics_by_norm_party.CaseCountAnalyticsByNormParty(
                        object = 'CaseCountAnalyticsByNormParty', 
                        norm_party_id = '01234567891011121314151617', 
                        norm_party_name = '', 
                        case_search_api = '', 
                        case_count = 56, )
                    ],
                next_page_api = '',
                previous_page_api = '',
                total_pages = 56,
                total_case_count = 56,
                total_norm_party_count = 56,
        )
        """

    def testCaseCountAnalyticsByNormPartyResponse(self):
        """Test CaseCountAnalyticsByNormPartyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()