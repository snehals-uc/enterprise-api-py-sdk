# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_source_data_committees_array_inner import BarSourceDataCommitteesArrayInner

class TestBarSourceDataCommitteesArrayInner(unittest.TestCase):
    """BarSourceDataCommitteesArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarSourceDataCommitteesArrayInner:
        """Test BarSourceDataCommitteesArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarSourceDataCommitteesArrayInner`
        """
        model = BarSourceDataCommitteesArrayInner()
        if include_optional:
            return BarSourceDataCommitteesArrayInner(
                committee = '',
                office = '',
                term = ''
            )
        else:
            return BarSourceDataCommitteesArrayInner(
                committee = '',
                office = '',
                term = '',
        )
        """

    def testBarSourceDataCommitteesArrayInner(self):
        """Test BarSourceDataCommitteesArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()