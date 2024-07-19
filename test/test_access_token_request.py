# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.access_token_request import AccessTokenRequest

class TestAccessTokenRequest(unittest.TestCase):
    """AccessTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessTokenRequest:
        """Test AccessTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessTokenRequest`
        """
        model = AccessTokenRequest()
        if include_optional:
            return AccessTokenRequest(
                client_id = '012345678910111213141516171819202122232425262728293031',
                client_secret = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263'
            )
        else:
            return AccessTokenRequest(
                client_id = '012345678910111213141516171819202122232425262728293031',
                client_secret = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263',
        )
        """

    def testAccessTokenRequest(self):
        """Test AccessTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()