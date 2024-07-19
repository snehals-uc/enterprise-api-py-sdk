# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.norm_judge_public_data import NormJudgePublicData

class TestNormJudgePublicData(unittest.TestCase):
    """NormJudgePublicData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormJudgePublicData:
        """Test NormJudgePublicData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormJudgePublicData`
        """
        model = NormJudgePublicData()
        if include_optional:
            return NormJudgePublicData(
                object = 'NormJudgePublicData',
                judicial_status = '',
                judicial_source = unicourt.models.norm_judge_public_data_judicial_source.NormJudgePublicData_judicialSource(
                    name = '', 
                    type = 'Website', 
                    url = '', ),
                aba_ratings = unicourt.models.norm_judge_public_data_aba_ratings.NormJudgePublicData_abaRatings(
                    rating = '', 
                    year = 56, ),
                alias_array = [
                    ''
                    ],
                bio = unicourt.models.norm_judge_public_data_bio.NormJudgePublicData_bio(
                    ethnicity = '', 
                    birth_city = '', 
                    birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    birth_state = '', 
                    death_city = '', 
                    death_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    death_state = '', 
                    political_affiliation = '', ),
                contact = unicourt.models.contact.Contact(
                    object = 'Contact', 
                    address_array = [
                        unicourt.models.address.Address(
                            object = 'Address', 
                            street_address1 = '0', 
                            street_address2 = '0', 
                            city = '0', 
                            state_name = 'UNKNOWN', 
                            state_code = '01', 
                            country_name = 'UNKNOWN', 
                            country_code = '01', 
                            zip = '0', 
                            zip4 = '0123', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = -90, 
                            longitude = -180, )
                        ], 
                    phone_number_array = [
                        unicourt.models.phone.Phone(
                            object = 'Phone', 
                            phone_number = '0', 
                            phone_type = 'DEFAULT', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    email_array = [
                        unicourt.models.email.Email(
                            object = 'Email', 
                            email_id = '0', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                education_array = [
                    unicourt.models.norm_judge_public_data_education_array_inner.NormJudgePublicData_educationArray_inner(
                        degree = '', 
                        year = 56, 
                        school = '', )
                    ],
                professional_career_array = [
                    ''
                    ],
                service_history_array = [
                    unicourt.models.service_history.ServiceHistory(
                        object = 'ServiceHistory', 
                        appointed_by = '', 
                        reason_for_termination = '', 
                        source_court = '', 
                        title = '', 
                        from_year = 56, 
                        to_year = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_visible = True, )
                    ],
                name_history_array = [
                    unicourt.models.norm_judge_public_data_name_history_array_inner.NormJudgePublicData_nameHistoryArray_inner(
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        prefix = '', 
                        suffix = '', 
                        is_visible = True, )
                    ],
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return NormJudgePublicData(
                object = 'NormJudgePublicData',
                judicial_status = '',
                judicial_source = unicourt.models.norm_judge_public_data_judicial_source.NormJudgePublicData_judicialSource(
                    name = '', 
                    type = 'Website', 
                    url = '', ),
                aba_ratings = unicourt.models.norm_judge_public_data_aba_ratings.NormJudgePublicData_abaRatings(
                    rating = '', 
                    year = 56, ),
                alias_array = [
                    ''
                    ],
                bio = unicourt.models.norm_judge_public_data_bio.NormJudgePublicData_bio(
                    ethnicity = '', 
                    birth_city = '', 
                    birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    birth_state = '', 
                    death_city = '', 
                    death_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    death_state = '', 
                    political_affiliation = '', ),
                contact = unicourt.models.contact.Contact(
                    object = 'Contact', 
                    address_array = [
                        unicourt.models.address.Address(
                            object = 'Address', 
                            street_address1 = '0', 
                            street_address2 = '0', 
                            city = '0', 
                            state_name = 'UNKNOWN', 
                            state_code = '01', 
                            country_name = 'UNKNOWN', 
                            country_code = '01', 
                            zip = '0', 
                            zip4 = '0123', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = -90, 
                            longitude = -180, )
                        ], 
                    phone_number_array = [
                        unicourt.models.phone.Phone(
                            object = 'Phone', 
                            phone_number = '0', 
                            phone_type = 'DEFAULT', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    email_array = [
                        unicourt.models.email.Email(
                            object = 'Email', 
                            email_id = '0', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                education_array = [
                    unicourt.models.norm_judge_public_data_education_array_inner.NormJudgePublicData_educationArray_inner(
                        degree = '', 
                        year = 56, 
                        school = '', )
                    ],
                professional_career_array = [
                    ''
                    ],
                service_history_array = [
                    unicourt.models.service_history.ServiceHistory(
                        object = 'ServiceHistory', 
                        appointed_by = '', 
                        reason_for_termination = '', 
                        source_court = '', 
                        title = '', 
                        from_year = 56, 
                        to_year = 56, 
                        from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_visible = True, )
                    ],
                name_history_array = [
                    unicourt.models.norm_judge_public_data_name_history_array_inner.NormJudgePublicData_nameHistoryArray_inner(
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        prefix = '', 
                        suffix = '', 
                        is_visible = True, )
                    ],
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testNormJudgePublicData(self):
        """Test NormJudgePublicData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()