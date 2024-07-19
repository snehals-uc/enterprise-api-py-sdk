# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.individual import Individual

class TestIndividual(unittest.TestCase):
    """Individual unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Individual:
        """Test Individual
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Individual`
        """
        model = Individual()
        if include_optional:
            return Individual(
                name = '',
                first_name = '',
                middle_name = '',
                last_name = ''
            )
        else:
            return Individual(
                name = '',
                first_name = '',
                middle_name = '',
                last_name = '',
        )
        """

    def testIndividual(self):
        """Test Individual"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()