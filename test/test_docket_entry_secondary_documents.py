# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.docket_entry_secondary_documents import DocketEntrySecondaryDocuments

class TestDocketEntrySecondaryDocuments(unittest.TestCase):
    """DocketEntrySecondaryDocuments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocketEntrySecondaryDocuments:
        """Test DocketEntrySecondaryDocuments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocketEntrySecondaryDocuments`
        """
        model = DocketEntrySecondaryDocuments()
        if include_optional:
            return DocketEntrySecondaryDocuments(
                object = 'DocketEntrySecondaryDocuments',
                page_number = 56,
                case_document_array = [
                    unicourt.models.case_document.CaseDocument(
                        object = 'CaseDocument', 
                        case_document_id = '01234567891011121314151617', 
                        sort_order = 56, 
                        name = '', 
                        description = '', 
                        document_filed_date = '0123456789101112131415161718192021222324', 
                        parent_document_id = '01234567891011121314151617', 
                        child_document_id_array = [
                            '01234567891011121314151617'
                            ], 
                        pages = 56, 
                        is_preview_available = True, 
                        preview_document = unicourt.models.preview_document.PreviewDocument(
                            object = 'PreviewDocument', 
                            in_library = True, 
                            added_to_library_date = '0123456789101112131415161718192021222324', 
                            download_api = '', ), 
                        price = 1.337, 
                        in_library = True, 
                        added_to_library_date = '0123456789101112131415161718192021222324', 
                        estimated_order_duration = 'estimateUnavailable', 
                        download_api = '', 
                        first_fetch_date = '0123456789101112131415161718192021222324', 
                        source_data_status = 'NO_LONGER_AVAILABLE_IN_COURT', )
                    ],
                next_page_api = '',
                total_pages = 56,
                total_count = 56
            )
        else:
            return DocketEntrySecondaryDocuments(
                object = 'DocketEntrySecondaryDocuments',
                page_number = 56,
                case_document_array = [
                    unicourt.models.case_document.CaseDocument(
                        object = 'CaseDocument', 
                        case_document_id = '01234567891011121314151617', 
                        sort_order = 56, 
                        name = '', 
                        description = '', 
                        document_filed_date = '0123456789101112131415161718192021222324', 
                        parent_document_id = '01234567891011121314151617', 
                        child_document_id_array = [
                            '01234567891011121314151617'
                            ], 
                        pages = 56, 
                        is_preview_available = True, 
                        preview_document = unicourt.models.preview_document.PreviewDocument(
                            object = 'PreviewDocument', 
                            in_library = True, 
                            added_to_library_date = '0123456789101112131415161718192021222324', 
                            download_api = '', ), 
                        price = 1.337, 
                        in_library = True, 
                        added_to_library_date = '0123456789101112131415161718192021222324', 
                        estimated_order_duration = 'estimateUnavailable', 
                        download_api = '', 
                        first_fetch_date = '0123456789101112131415161718192021222324', 
                        source_data_status = 'NO_LONGER_AVAILABLE_IN_COURT', )
                    ],
                next_page_api = '',
                total_pages = 56,
                total_count = 56,
        )
        """

    def testDocketEntrySecondaryDocuments(self):
        """Test DocketEntrySecondaryDocuments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
