# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.norm_organization_ticker_array_inner import NormOrganizationTickerArrayInner

class TestNormOrganizationTickerArrayInner(unittest.TestCase):
    """NormOrganizationTickerArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormOrganizationTickerArrayInner:
        """Test NormOrganizationTickerArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormOrganizationTickerArrayInner`
        """
        model = NormOrganizationTickerArrayInner()
        if include_optional:
            return NormOrganizationTickerArrayInner(
                exchange = '',
                symbols = [
                    ''
                    ]
            )
        else:
            return NormOrganizationTickerArrayInner(
                exchange = '',
                symbols = [
                    ''
                    ],
        )
        """

    def testNormOrganizationTickerArrayInner(self):
        """Test NormOrganizationTickerArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
