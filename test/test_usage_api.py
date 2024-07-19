# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.api.usage_api import UsageApi


class TestUsageApi(unittest.TestCase):
    """UsageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsageApi()

    def tearDown(self) -> None:
        pass

    def test_get_billing_cycles(self) -> None:
        """Test case for get_billing_cycles

        Get all the previous 12 billing cycles.
        """
        pass

    def test_get_billing_usage_by_billing_cycle(self) -> None:
        """Test case for get_billing_usage_by_billing_cycle

        Specify the billing cycle to know the API usage.
        """
        pass

    def test_get_daily_usage_by_date(self) -> None:
        """Test case for get_daily_usage_by_date

        Get API usage for a requested Date.
        """
        pass


if __name__ == '__main__':
    unittest.main()
