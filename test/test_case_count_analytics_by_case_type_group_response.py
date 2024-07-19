# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_count_analytics_by_case_type_group_response import CaseCountAnalyticsByCaseTypeGroupResponse

class TestCaseCountAnalyticsByCaseTypeGroupResponse(unittest.TestCase):
    """CaseCountAnalyticsByCaseTypeGroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseCountAnalyticsByCaseTypeGroupResponse:
        """Test CaseCountAnalyticsByCaseTypeGroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseCountAnalyticsByCaseTypeGroupResponse`
        """
        model = CaseCountAnalyticsByCaseTypeGroupResponse()
        if include_optional:
            return CaseCountAnalyticsByCaseTypeGroupResponse(
                object = 'CaseCountAnalyticsByCaseTypeGroupResponse',
                next_page_api = '',
                previous_page_api = '',
                results = [
                    unicourt.models.case_count_analytics_by_case_type_group.CaseCountAnalyticsByCaseTypeGroup(
                        object = 'CaseCountAnalyticsByCaseTypeGroup', 
                        case_count = 56, 
                        case_search_api = '', 
                        case_type_group = unicourt.models.case_type_group.CaseTypeGroup(
                            object = 'CaseTypeGroup', 
                            case_type_group_id = '01234567891011121314151617', 
                            case_class_id = '01234567891011121314151617', 
                            area_of_law_id = '01234567891011121314151617', 
                            case_class = '0', 
                            area_of_law = '0', 
                            name = '0', 
                            created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                total_pages = 56,
                total_case_count = 56,
                total_case_type_group_count = 56
            )
        else:
            return CaseCountAnalyticsByCaseTypeGroupResponse(
                object = 'CaseCountAnalyticsByCaseTypeGroupResponse',
                next_page_api = '',
                previous_page_api = '',
                results = [
                    unicourt.models.case_count_analytics_by_case_type_group.CaseCountAnalyticsByCaseTypeGroup(
                        object = 'CaseCountAnalyticsByCaseTypeGroup', 
                        case_count = 56, 
                        case_search_api = '', 
                        case_type_group = unicourt.models.case_type_group.CaseTypeGroup(
                            object = 'CaseTypeGroup', 
                            case_type_group_id = '01234567891011121314151617', 
                            case_class_id = '01234567891011121314151617', 
                            area_of_law_id = '01234567891011121314151617', 
                            case_class = '0', 
                            area_of_law = '0', 
                            name = '0', 
                            created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                total_pages = 56,
                total_case_count = 56,
                total_case_type_group_count = 56,
        )
        """

    def testCaseCountAnalyticsByCaseTypeGroupResponse(self):
        """Test CaseCountAnalyticsByCaseTypeGroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()