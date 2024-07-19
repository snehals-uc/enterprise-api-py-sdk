# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.party_role import PartyRole

class TestPartyRole(unittest.TestCase):
    """PartyRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartyRole:
        """Test PartyRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartyRole`
        """
        model = PartyRole()
        if include_optional:
            return PartyRole(
                object = 'PartyRole',
                party_role_id = '01234567891011121314151617',
                party_role_group_id = '01234567891011121314151617',
                party_role_group = '0',
                name = '0',
                description = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PartyRole(
                object = 'PartyRole',
                party_role_id = '01234567891011121314151617',
                party_role_group_id = '01234567891011121314151617',
                party_role_group = '0',
                name = '0',
                description = '0',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testPartyRole(self):
        """Test PartyRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()