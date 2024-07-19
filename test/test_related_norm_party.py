# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.related_norm_party import RelatedNormParty

class TestRelatedNormParty(unittest.TestCase):
    """RelatedNormParty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelatedNormParty:
        """Test RelatedNormParty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedNormParty`
        """
        model = RelatedNormParty()
        if include_optional:
            return RelatedNormParty(
                object = 'RelatedNormParty',
                norm_party_id = '01234567891011121314151617',
                relationship_type = 'Parent'
            )
        else:
            return RelatedNormParty(
                object = 'RelatedNormParty',
                norm_party_id = '01234567891011121314151617',
                relationship_type = 'Parent',
        )
        """

    def testRelatedNormParty(self):
        """Test RelatedNormParty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()