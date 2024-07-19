# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.cause_of_action_group_response import CauseOfActionGroupResponse

class TestCauseOfActionGroupResponse(unittest.TestCase):
    """CauseOfActionGroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CauseOfActionGroupResponse:
        """Test CauseOfActionGroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CauseOfActionGroupResponse`
        """
        model = CauseOfActionGroupResponse()
        if include_optional:
            return CauseOfActionGroupResponse(
                object = 'CauseOfActionGroupResponse',
                cause_of_action_group_array = [
                    unicourt.models.cause_of_action_group.CauseOfActionGroup(
                        object = 'CauseOfActionGroup', 
                        cause_of_action_group_id = '01234567891011121314151617', 
                        name = '0', 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page_api = '0',
                previous_page_api = '0',
                page_number = 1,
                total_pages = 1,
                total_count = 1
            )
        else:
            return CauseOfActionGroupResponse(
                object = 'CauseOfActionGroupResponse',
                cause_of_action_group_array = [
                    unicourt.models.cause_of_action_group.CauseOfActionGroup(
                        object = 'CauseOfActionGroup', 
                        cause_of_action_group_id = '01234567891011121314151617', 
                        name = '0', 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                next_page_api = '0',
                previous_page_api = '0',
                page_number = 1,
                total_pages = 1,
                total_count = 1,
        )
        """

    def testCauseOfActionGroupResponse(self):
        """Test CauseOfActionGroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
