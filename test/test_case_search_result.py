# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_search_result import CaseSearchResult

class TestCaseSearchResult(unittest.TestCase):
    """CaseSearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseSearchResult:
        """Test CaseSearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseSearchResult`
        """
        model = CaseSearchResult()
        if include_optional:
            return CaseSearchResult(
                object = 'CaseSearchResult',
                case_id = '01234567891011121314151617',
                case_name = '',
                case_number = '0',
                filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                court = unicourt.models.court.Court(
                    object = 'Court', 
                    court_id = '01234567891011121314151617', 
                    court_type_id = '01234567891011121314151617', 
                    court_system_id = '01234567891011121314151617', 
                    type = '0', 
                    system = '0', 
                    name = '0', 
                    name_aka = '0', 
                    additional_levels = unicourt.models.additional_levels.AdditionalLevels(
                        object = 'AdditionalLevels', 
                        level1 = '0', 
                        level2 = '0', 
                        level3 = '0', 
                        level4 = '0', ), 
                    container_type = '0', 
                    container = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jurisdiction_geo_for_court_api = '0', 
                    court_locations_for_court_api = '0', 
                    appeal_courts_for_court_api = '0', 
                    court_service_status_api = '0', ),
                court_location = unicourt.models.court_location.CourtLocation(
                    object = 'CourtLocation', 
                    court_location_id = '01234567891011121314151617', 
                    name = '0', 
                    street_address1 = '0', 
                    street_address2 = '', 
                    city = '', 
                    state_name = 'UNKNOWN', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    courts_for_court_location_api = '0', 
                    court_service_status_api = '0', ),
                case_type = unicourt.models.case_type.CaseType(
                    object = 'CaseType', 
                    case_type_id = '01234567891011121314151617', 
                    case_class_id = '01234567891011121314151617', 
                    area_of_law_id = '01234567891011121314151617', 
                    case_type_group_id = '01234567891011121314151617', 
                    case_class = '0', 
                    area_of_law = '0', 
                    case_type_group = '0', 
                    name = '0', 
                    sali_code = '0', 
                    case_type_tag = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                case_status = unicourt.models.case_status.CaseStatus(
                    object = 'CaseStatus', 
                    case_status_id = '01234567891011121314151617', 
                    case_status_group_id = '01234567891011121314151617', 
                    case_status_group = '0', 
                    name = '0', 
                    case_class_array = [
                        '0'
                        ], 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                participants_last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                case_api = '0',
                matched_object_array = [
                    unicourt.models.matched_object.MatchedObject(
                        object = 'MatchedObject', 
                        matched_object_id = '012345678910111213141516', 
                        matched_object_name = '0', 
                        matched_object_attribute = '0', 
                        highlight_snippet = '0', 
                        matched_object_api = '0', )
                    ]
            )
        else:
            return CaseSearchResult(
                object = 'CaseSearchResult',
                case_id = '01234567891011121314151617',
                case_name = '',
                case_number = '0',
                filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                court = unicourt.models.court.Court(
                    object = 'Court', 
                    court_id = '01234567891011121314151617', 
                    court_type_id = '01234567891011121314151617', 
                    court_system_id = '01234567891011121314151617', 
                    type = '0', 
                    system = '0', 
                    name = '0', 
                    name_aka = '0', 
                    additional_levels = unicourt.models.additional_levels.AdditionalLevels(
                        object = 'AdditionalLevels', 
                        level1 = '0', 
                        level2 = '0', 
                        level3 = '0', 
                        level4 = '0', ), 
                    container_type = '0', 
                    container = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    jurisdiction_geo_for_court_api = '0', 
                    court_locations_for_court_api = '0', 
                    appeal_courts_for_court_api = '0', 
                    court_service_status_api = '0', ),
                court_location = unicourt.models.court_location.CourtLocation(
                    object = 'CourtLocation', 
                    court_location_id = '01234567891011121314151617', 
                    name = '0', 
                    street_address1 = '0', 
                    street_address2 = '', 
                    city = '', 
                    state_name = 'UNKNOWN', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    courts_for_court_location_api = '0', 
                    court_service_status_api = '0', ),
                case_type = unicourt.models.case_type.CaseType(
                    object = 'CaseType', 
                    case_type_id = '01234567891011121314151617', 
                    case_class_id = '01234567891011121314151617', 
                    area_of_law_id = '01234567891011121314151617', 
                    case_type_group_id = '01234567891011121314151617', 
                    case_class = '0', 
                    area_of_law = '0', 
                    case_type_group = '0', 
                    name = '0', 
                    sali_code = '0', 
                    case_type_tag = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                case_status = unicourt.models.case_status.CaseStatus(
                    object = 'CaseStatus', 
                    case_status_id = '01234567891011121314151617', 
                    case_status_group_id = '01234567891011121314151617', 
                    case_status_group = '0', 
                    name = '0', 
                    case_class_array = [
                        '0'
                        ], 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                participants_last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                case_api = '0',
                matched_object_array = [
                    unicourt.models.matched_object.MatchedObject(
                        object = 'MatchedObject', 
                        matched_object_id = '012345678910111213141516', 
                        matched_object_name = '0', 
                        matched_object_attribute = '0', 
                        highlight_snippet = '0', 
                        matched_object_api = '0', )
                    ],
        )
        """

    def testCaseSearchResult(self):
        """Test CaseSearchResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
