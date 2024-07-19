# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_source_data_disciplinary_history_array_inner import BarSourceDataDisciplinaryHistoryArrayInner

class TestBarSourceDataDisciplinaryHistoryArrayInner(unittest.TestCase):
    """BarSourceDataDisciplinaryHistoryArrayInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarSourceDataDisciplinaryHistoryArrayInner:
        """Test BarSourceDataDisciplinaryHistoryArrayInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarSourceDataDisciplinaryHistoryArrayInner`
        """
        model = BarSourceDataDisciplinaryHistoryArrayInner()
        if include_optional:
            return BarSourceDataDisciplinaryHistoryArrayInner(
                action = '',
                case_number = '',
                complaint = '',
                contact_id = '0',
                date_of_action = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                definition = '',
                disciplinary_decision = '',
                entry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                information = '',
                link = '',
                note = '',
                probation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                rule = '',
                rule_number = '',
                section_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = '',
                stay_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                supreme_court = '',
                term = '',
                type_of_action = ''
            )
        else:
            return BarSourceDataDisciplinaryHistoryArrayInner(
                action = '',
                case_number = '',
                complaint = '',
                contact_id = '0',
                date_of_action = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                definition = '',
                disciplinary_decision = '',
                entry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                information = '',
                link = '',
                note = '',
                probation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                rule = '',
                rule_number = '',
                section_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = '',
                stay_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                supreme_court = '',
                term = '',
                type_of_action = '',
        )
        """

    def testBarSourceDataDisciplinaryHistoryArrayInner(self):
        """Test BarSourceDataDisciplinaryHistoryArrayInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
