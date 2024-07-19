# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.norm_judge_public_data_education_array_inner import NormJudgePublicDataEducationArrayInner

class TestNormJudgePublicDataEducationArrayInner(unittest.TestCase):
    """NormJudgePublicDataEducationArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormJudgePublicDataEducationArrayInner:
        """Test NormJudgePublicDataEducationArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormJudgePublicDataEducationArrayInner`
        """
        model = NormJudgePublicDataEducationArrayInner()
        if include_optional:
            return NormJudgePublicDataEducationArrayInner(
                degree = '',
                year = 56,
                school = ''
            )
        else:
            return NormJudgePublicDataEducationArrayInner(
                degree = '',
                year = 56,
                school = '',
        )
        """

    def testNormJudgePublicDataEducationArrayInner(self):
        """Test NormJudgePublicDataEducationArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()