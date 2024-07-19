# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.associated_norm_judge import AssociatedNormJudge

class TestAssociatedNormJudge(unittest.TestCase):
    """AssociatedNormJudge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssociatedNormJudge:
        """Test AssociatedNormJudge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssociatedNormJudge`
        """
        model = AssociatedNormJudge()
        if include_optional:
            return AssociatedNormJudge(
                object = 'AssociatedNormJudge',
                norm_judge_id = '01234567891011121314151617',
                norm_judge_api = '',
                case_timeline = unicourt.models.case_timeline.CaseTimeline(
                    object = 'CaseTimeline', 
                    first_case_filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_case_filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                name = '',
                first_name = '',
                middle_name = '',
                last_name = '',
                case_search_api = '',
                case_count = 56,
                version = ''
            )
        else:
            return AssociatedNormJudge(
                object = 'AssociatedNormJudge',
                norm_judge_id = '01234567891011121314151617',
                norm_judge_api = '',
                case_timeline = unicourt.models.case_timeline.CaseTimeline(
                    object = 'CaseTimeline', 
                    first_case_filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_case_filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                name = '',
                first_name = '',
                middle_name = '',
                last_name = '',
                case_search_api = '',
                case_count = 56,
                version = '',
        )
        """

    def testAssociatedNormJudge(self):
        """Test AssociatedNormJudge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
