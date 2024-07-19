# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.charge_group import ChargeGroup

class TestChargeGroup(unittest.TestCase):
    """ChargeGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChargeGroup:
        """Test ChargeGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChargeGroup`
        """
        model = ChargeGroup()
        if include_optional:
            return ChargeGroup(
                object = 'ChargeGroup',
                charge_group_id = '01234567891011121314151617',
                name = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ChargeGroup(
                object = 'ChargeGroup',
                charge_group_id = '01234567891011121314151617',
                name = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testChargeGroup(self):
        """Test ChargeGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()