# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_type_group import CaseTypeGroup

class TestCaseTypeGroup(unittest.TestCase):
    """CaseTypeGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseTypeGroup:
        """Test CaseTypeGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseTypeGroup`
        """
        model = CaseTypeGroup()
        if include_optional:
            return CaseTypeGroup(
                object = 'CaseTypeGroup',
                case_type_group_id = '01234567891011121314151617',
                case_class_id = '01234567891011121314151617',
                area_of_law_id = '01234567891011121314151617',
                case_class = '0',
                area_of_law = '0',
                name = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CaseTypeGroup(
                object = 'CaseTypeGroup',
                case_type_group_id = '01234567891011121314151617',
                case_class_id = '01234567891011121314151617',
                area_of_law_id = '01234567891011121314151617',
                case_class = '0',
                area_of_law = '0',
                name = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCaseTypeGroup(self):
        """Test CaseTypeGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
