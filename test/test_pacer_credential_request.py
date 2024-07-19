# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.pacer_credential_request import PacerCredentialRequest

class TestPacerCredentialRequest(unittest.TestCase):
    """PacerCredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PacerCredentialRequest:
        """Test PacerCredentialRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PacerCredentialRequest`
        """
        model = PacerCredentialRequest()
        if include_optional:
            return PacerCredentialRequest(
                pacer_user_id = '012345',
                default_pacer_client_code = '',
                password = '01234567'
            )
        else:
            return PacerCredentialRequest(
                pacer_user_id = '012345',
                password = '01234567',
        )
        """

    def testPacerCredentialRequest(self):
        """Test PacerCredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
