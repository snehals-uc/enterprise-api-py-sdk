# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.norm_law_firm_search_response import NormLawFirmSearchResponse

class TestNormLawFirmSearchResponse(unittest.TestCase):
    """NormLawFirmSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormLawFirmSearchResponse:
        """Test NormLawFirmSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormLawFirmSearchResponse`
        """
        model = NormLawFirmSearchResponse()
        if include_optional:
            return NormLawFirmSearchResponse(
                object = 'NormLawFirmSearchResponse',
                norm_law_firm_search_result_array = [
                    unicourt.models.norm_law_firm_search_result.NormLawFirmSearchResult(
                        object = 'NormLawFirmSearchResult', 
                        norm_law_firm_id = '012345678910111213141516', 
                        name = '0', 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        norm_law_firm_details_api = '0', 
                        matched_object_array = [
                            unicourt.models.matched_object.MatchedObject(
                                object = 'MatchedObject', 
                                matched_object_id = '012345678910111213141516', 
                                matched_object_name = '0', 
                                matched_object_attribute = '0', 
                                highlight_snippet = '0', 
                                matched_object_api = '0', )
                            ], )
                    ],
                q = '012',
                norm_law_firm_search_id = '01234567891011121314151617',
                next_page_api = '0',
                previous_page_api = '0',
                page_number = 1,
                total_pages = 1,
                total_count = 1
            )
        else:
            return NormLawFirmSearchResponse(
                object = 'NormLawFirmSearchResponse',
                norm_law_firm_search_result_array = [
                    unicourt.models.norm_law_firm_search_result.NormLawFirmSearchResult(
                        object = 'NormLawFirmSearchResult', 
                        norm_law_firm_id = '012345678910111213141516', 
                        name = '0', 
                        first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        norm_law_firm_details_api = '0', 
                        matched_object_array = [
                            unicourt.models.matched_object.MatchedObject(
                                object = 'MatchedObject', 
                                matched_object_id = '012345678910111213141516', 
                                matched_object_name = '0', 
                                matched_object_attribute = '0', 
                                highlight_snippet = '0', 
                                matched_object_api = '0', )
                            ], )
                    ],
                q = '012',
                norm_law_firm_search_id = '01234567891011121314151617',
                next_page_api = '0',
                previous_page_api = '0',
                page_number = 1,
                total_pages = 1,
                total_count = 1,
        )
        """

    def testNormLawFirmSearchResponse(self):
        """Test NormLawFirmSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
