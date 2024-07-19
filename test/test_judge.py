# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.judge import Judge

class TestJudge(unittest.TestCase):
    """Judge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Judge:
        """Test Judge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Judge`
        """
        model = Judge()
        if include_optional:
            return Judge(
                object = 'Judge',
                judge_id = '01234567891011121314151617',
                name = '0',
                name_prefix = '',
                first_name = '',
                middle_name = '',
                last_name = '',
                name_suffix = '',
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
                judge_type = unicourt.models.judge_type.JudgeType(
                    object = 'JudgeType', 
                    judge_type_id = '01234567891011121314151617', 
                    name = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                source_judge_type = '',
                is_visible = True,
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                possible_norm_judge_array = [
                    unicourt.models.possible_norm_judge.PossibleNormJudge(
                        object = 'PossibleNormJudge', 
                        norm_judge_id = '01234567891011121314151617', 
                        norm_judge_name = '', 
                        best_match = True, 
                        confidence_score = 1.337, 
                        score_constituents = unicourt.models.possible_norm_judge_score_constituents.PossibleNormJudge_scoreConstituents(
                            name_similarity_score = 1.337, 
                            other_potential_norm_judges = 56, 
                            address = 'Matched', 
                            email = 'Matched', 
                            phone = 'Matched', ), 
                        norm_judge_api = '', 
                        associated_norm_attorneys_api = '', 
                        associated_norm_law_firms_api = '', 
                        associated_norm_parties_api = '', 
                        case_count_analytics_by_norm_judge_api = '', )
                    ]
            )
        else:
            return Judge(
                object = 'Judge',
                judge_id = '01234567891011121314151617',
                name = '0',
                name_prefix = '',
                first_name = '',
                middle_name = '',
                last_name = '',
                name_suffix = '',
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
                judge_type = unicourt.models.judge_type.JudgeType(
                    object = 'JudgeType', 
                    judge_type_id = '01234567891011121314151617', 
                    name = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                source_judge_type = '',
                is_visible = True,
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                possible_norm_judge_array = [
                    unicourt.models.possible_norm_judge.PossibleNormJudge(
                        object = 'PossibleNormJudge', 
                        norm_judge_id = '01234567891011121314151617', 
                        norm_judge_name = '', 
                        best_match = True, 
                        confidence_score = 1.337, 
                        score_constituents = unicourt.models.possible_norm_judge_score_constituents.PossibleNormJudge_scoreConstituents(
                            name_similarity_score = 1.337, 
                            other_potential_norm_judges = 56, 
                            address = 'Matched', 
                            email = 'Matched', 
                            phone = 'Matched', ), 
                        norm_judge_api = '', 
                        associated_norm_attorneys_api = '', 
                        associated_norm_law_firms_api = '', 
                        associated_norm_parties_api = '', 
                        case_count_analytics_by_norm_judge_api = '', )
                    ],
        )
        """

    def testJudge(self):
        """Test Judge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
