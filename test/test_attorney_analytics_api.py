# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.attorney_analytics_api import AttorneyAnalyticsAPI

class TestAttorneyAnalyticsAPI(unittest.TestCase):
    """AttorneyAnalyticsAPI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttorneyAnalyticsAPI:
        """Test AttorneyAnalyticsAPI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttorneyAnalyticsAPI`
        """
        model = AttorneyAnalyticsAPI()
        if include_optional:
            return AttorneyAnalyticsAPI(
                object = 'AttorneyAnalyticsAPI',
                norm_attorney_api = '',
                associated_norm_judges_api = '',
                associated_norm_law_firms_api = '',
                associated_norm_parties_api = '',
                case_count_analytics_by_opposing_norm_attorney_api = '',
                case_count_analytics_by_opposing_norm_law_firm_api = '',
                case_count_analytics_by_opposing_norm_party_api = ''
            )
        else:
            return AttorneyAnalyticsAPI(
                object = 'AttorneyAnalyticsAPI',
                norm_attorney_api = '',
                associated_norm_judges_api = '',
                associated_norm_law_firms_api = '',
                associated_norm_parties_api = '',
                case_count_analytics_by_opposing_norm_attorney_api = '',
                case_count_analytics_by_opposing_norm_law_firm_api = '',
                case_count_analytics_by_opposing_norm_party_api = '',
        )
        """

    def testAttorneyAnalyticsAPI(self):
        """Test AttorneyAnalyticsAPI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
