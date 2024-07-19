# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_source_data_administrative_actions_array_inner import BarSourceDataAdministrativeActionsArrayInner

class TestBarSourceDataAdministrativeActionsArrayInner(unittest.TestCase):
    """BarSourceDataAdministrativeActionsArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarSourceDataAdministrativeActionsArrayInner:
        """Test BarSourceDataAdministrativeActionsArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarSourceDataAdministrativeActionsArrayInner`
        """
        model = BarSourceDataAdministrativeActionsArrayInner()
        if include_optional:
            return BarSourceDataAdministrativeActionsArrayInner(
                case_number = '',
                description = '',
                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                resulting_status = '',
                type = ''
            )
        else:
            return BarSourceDataAdministrativeActionsArrayInner(
                case_number = '',
                description = '',
                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                resulting_status = '',
                type = '',
        )
        """

    def testBarSourceDataAdministrativeActionsArrayInner(self):
        """Test BarSourceDataAdministrativeActionsArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()