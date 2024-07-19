# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.possible_norm_party_score_constituents import PossibleNormPartyScoreConstituents

class TestPossibleNormPartyScoreConstituents(unittest.TestCase):
    """PossibleNormPartyScoreConstituents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PossibleNormPartyScoreConstituents:
        """Test PossibleNormPartyScoreConstituents
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PossibleNormPartyScoreConstituents`
        """
        model = PossibleNormPartyScoreConstituents()
        if include_optional:
            return PossibleNormPartyScoreConstituents(
                name_similarity_score = 1.337,
                other_potential_norm_parties = 56,
                secretary_of_state_id = 'Matched',
                address = 'Matched',
                email = 'Matched',
                phone = 'Matched'
            )
        else:
            return PossibleNormPartyScoreConstituents(
                name_similarity_score = 1.337,
                other_potential_norm_parties = 56,
                secretary_of_state_id = 'Matched',
                address = 'Matched',
                email = 'Matched',
                phone = 'Matched',
        )
        """

    def testPossibleNormPartyScoreConstituents(self):
        """Test PossibleNormPartyScoreConstituents"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
