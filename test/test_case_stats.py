# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.case_stats import CaseStats

class TestCaseStats(unittest.TestCase):
    """CaseStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaseStats:
        """Test CaseStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaseStats`
        """
        model = CaseStats()
        if include_optional:
            return CaseStats(
                object = 'CaseStats',
                party_count = 56,
                attorney_count = 56,
                judge_count = 56,
                docket_entry_count = 56,
                free_case_document_count = 56,
                paid_case_document_count = 56,
                all_case_document_count = 56,
                case_document_in_library_count = 56,
                hearing_count = 56,
                related_case_count = 56
            )
        else:
            return CaseStats(
                object = 'CaseStats',
                party_count = 56,
                attorney_count = 56,
                judge_count = 56,
                docket_entry_count = 56,
                free_case_document_count = 56,
                paid_case_document_count = 56,
                all_case_document_count = 56,
                case_document_in_library_count = 56,
                hearing_count = 56,
                related_case_count = 56,
        )
        """

    def testCaseStats(self):
        """Test CaseStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()