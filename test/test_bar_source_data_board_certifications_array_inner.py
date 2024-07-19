# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_source_data_board_certifications_array_inner import BarSourceDataBoardCertificationsArrayInner

class TestBarSourceDataBoardCertificationsArrayInner(unittest.TestCase):
    """BarSourceDataBoardCertificationsArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarSourceDataBoardCertificationsArrayInner:
        """Test BarSourceDataBoardCertificationsArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarSourceDataBoardCertificationsArrayInner`
        """
        model = BarSourceDataBoardCertificationsArrayInner()
        if include_optional:
            return BarSourceDataBoardCertificationsArrayInner(
                area = '',
                year = ''
            )
        else:
            return BarSourceDataBoardCertificationsArrayInner(
                area = '',
                year = '',
        )
        """

    def testBarSourceDataBoardCertificationsArrayInner(self):
        """Test BarSourceDataBoardCertificationsArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
