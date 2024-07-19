# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_source_data_court_history_array_inner import BarSourceDataCourtHistoryArrayInner

class TestBarSourceDataCourtHistoryArrayInner(unittest.TestCase):
    """BarSourceDataCourtHistoryArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarSourceDataCourtHistoryArrayInner:
        """Test BarSourceDataCourtHistoryArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarSourceDataCourtHistoryArrayInner`
        """
        model = BarSourceDataCourtHistoryArrayInner()
        if include_optional:
            return BarSourceDataCourtHistoryArrayInner(
                action = '',
                action_comments = '',
                reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BarSourceDataCourtHistoryArrayInner(
                action = '',
                action_comments = '',
                reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBarSourceDataCourtHistoryArrayInner(self):
        """Test BarSourceDataCourtHistoryArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
