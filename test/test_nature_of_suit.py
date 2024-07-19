# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.nature_of_suit import NatureOfSuit

class TestNatureOfSuit(unittest.TestCase):
    """NatureOfSuit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NatureOfSuit:
        """Test NatureOfSuit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NatureOfSuit`
        """
        model = NatureOfSuit()
        if include_optional:
            return NatureOfSuit(
                object = 'NatureOfSuit',
                source_text = '',
                code = 56,
                name = '',
                section = ''
            )
        else:
            return NatureOfSuit(
                object = 'NatureOfSuit',
                source_text = '',
                code = 56,
                name = '',
                section = '',
        )
        """

    def testNatureOfSuit(self):
        """Test NatureOfSuit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()