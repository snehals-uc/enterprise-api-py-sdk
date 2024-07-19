# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_update_list_response import CaseUpdateListResponse

class TestCaseUpdateListResponse(unittest.TestCase):
    """CaseUpdateListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseUpdateListResponse:
        """Test CaseUpdateListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseUpdateListResponse`
        """
        model = CaseUpdateListResponse()
        if include_optional:
            return CaseUpdateListResponse(
                object = 'CaseUpdateListResponse',
                total_pages = 56,
                total_count = 56,
                page_number = 56,
                next_page_api = '0',
                previous_page_api = '0',
                case_update_preview_array = [
                    unicourt.models.case_update_preview.CaseUpdatePreview(
                        object = 'CaseUpdatePreview', 
                        case_id = '01234567891011121314151617', 
                        status = 'COMPLETE', 
                        requested_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        case_api = '0', 
                        pacer_options = unicourt.models.case_update_pacer_options_response.CaseUpdatePacerOptionsResponse(
                            object = 'CaseUpdatePacerOptionsResponse', 
                            pacer_user_id = '012345', 
                            pacer_client_code = '', 
                            fetch_participants_if_older_than_days = 0, 
                            refresh_type = 'fetchNewDocketEntries', 
                            additional_page_array = [
                                unicourt.models.case_update_pacer_options_additional_page_array_inner.CaseUpdatePacerOptions_additionalPageArray_inner(
                                    page = 'associatedCases', 
                                    fetch_if_older_than_days = 0, )
                                ], ), 
                        exception = unicourt.models.exception.Exception(
                            object = 'Exception', 
                            code = '0', 
                            message = '0', 
                            details = '0', ), )
                    ]
            )
        else:
            return CaseUpdateListResponse(
                object = 'CaseUpdateListResponse',
                total_pages = 56,
                total_count = 56,
                page_number = 56,
                next_page_api = '0',
                previous_page_api = '0',
                case_update_preview_array = [
                    unicourt.models.case_update_preview.CaseUpdatePreview(
                        object = 'CaseUpdatePreview', 
                        case_id = '01234567891011121314151617', 
                        status = 'COMPLETE', 
                        requested_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        case_api = '0', 
                        pacer_options = unicourt.models.case_update_pacer_options_response.CaseUpdatePacerOptionsResponse(
                            object = 'CaseUpdatePacerOptionsResponse', 
                            pacer_user_id = '012345', 
                            pacer_client_code = '', 
                            fetch_participants_if_older_than_days = 0, 
                            refresh_type = 'fetchNewDocketEntries', 
                            additional_page_array = [
                                unicourt.models.case_update_pacer_options_additional_page_array_inner.CaseUpdatePacerOptions_additionalPageArray_inner(
                                    page = 'associatedCases', 
                                    fetch_if_older_than_days = 0, )
                                ], ), 
                        exception = unicourt.models.exception.Exception(
                            object = 'Exception', 
                            code = '0', 
                            message = '0', 
                            details = '0', ), )
                    ],
        )
        """

    def testCaseUpdateListResponse(self):
        """Test CaseUpdateListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()