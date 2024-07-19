# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/developers/enterpriseapi/api/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unicourt.models.bar_record import BarRecord

class TestBarRecord(unittest.TestCase):
    """BarRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BarRecord:
        """Test BarRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BarRecord`
        """
        model = BarRecord()
        if include_optional:
            return BarRecord(
                object = 'BarRecord',
                bar_number = '',
                bar_source_type = '',
                admitted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state_code = '',
                status = 'Active',
                inactivation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                bar_source_data = unicourt.models.bar_source_data.BarSourceData(
                    object = 'BarSourceData', 
                    administrative_actions_array = [
                        unicourt.models.bar_source_data_administrative_actions_array_inner.BarSourceData_administrativeActionsArray_inner(
                            case_number = '', 
                            description = '', 
                            effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            resulting_status = '', 
                            type = '', )
                        ], 
                    admission_type = '', 
                    appellate_court_district = '', 
                    appellate_division_department = '', 
                    attorney_group = '', 
                    authorized = '', 
                    bar_service_class = '', 
                    bio = '', 
                    board_certifications_array = [
                        unicourt.models.bar_source_data_board_certifications_array_inner.BarSourceData_boardCertificationsArray_inner(
                            area = '', 
                            year = '', )
                        ], 
                    board_district = '', 
                    circuit = '', 
                    comments = '', 
                    committees_array = [
                        unicourt.models.bar_source_data_committees_array_inner.BarSourceData_committeesArray_inner(
                            committee = '', 
                            office = '', 
                            term = '', )
                        ], 
                    court_history_array = [
                        unicourt.models.bar_source_data_court_history_array_inner.BarSourceData_courtHistoryArray_inner(
                            action = '', 
                            action_comments = '', 
                            reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    court_of_admissions = unicourt.models.bar_source_data_court_of_admissions.BarSourceData_courtOfAdmissions(
                        court_state_array = [
                            ''
                            ], 
                        federal_array = [
                            ''
                            ], 
                        other_courts_array = [
                            ''
                            ], ), 
                    court_service_email = '', 
                    disciplinary_history_array = [
                        unicourt.models.bar_source_data_disciplinary_history_array_inner.BarSourceData_disciplinaryHistoryArray_inner(
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
                            type_of_action = '', )
                        ], 
                    discipline_summaries_array = [
                        unicourt.models.bar_source_data_discipline_summaries_array_inner.BarSourceData_disciplineSummariesArray_inner(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            link = '', 
                            title = '', )
                        ], 
                    dismissals_array = [
                        ''
                        ], 
                    district = '', 
                    employment_history_array = [
                        unicourt.models.bar_source_data_employment_history_array_inner.BarSourceData_employmentHistoryArray_inner(
                            employer = '', 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    fees_options_array = [
                        unicourt.models.bar_source_data_fees_options_array_inner.BarSourceData_feesOptionsArray_inner(
                            contingency_fees = '', 
                            flat_fees = '', 
                            hourly_rate = '', 
                            payment_plans = '', 
                            sliding_scale_fees = '', )
                        ], 
                    firm_size = '', 
                    firm_website = '', 
                    first_admitted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    first_admitted_year = 56, 
                    home_county = '', 
                    in_good_standing = '', 
                    insurance = '', 
                    involvements_array = [
                        unicourt.models.bar_source_data_involvements_array_inner.BarSourceData_involvementsArray_inner(
                            name = '', 
                            position = '', 
                            type = '', )
                        ], 
                    judicial_district = '', 
                    juris_type = '', 
                    languages_array = [
                        ''
                        ], 
                    last_renewal_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    law_school_array = [
                        unicourt.models.bar_source_data_law_school_array_inner.BarSourceData_lawSchoolArray_inner(
                            law_school = '', 
                            law_school_graduated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    legal_speciality_array = [
                        ''
                        ], 
                    license_type = '', 
                    name = unicourt.models.bar_source_data_name.BarSourceData_name(
                        name = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        prefix = '', 
                        suffix = '', ), 
                    next_registration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_renewal_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    open_action_status_array = [
                        unicourt.models.bar_source_data_open_action_status_array_inner.BarSourceData_openActionStatusArray_inner(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reason = '', )
                        ], 
                    other_jurisdiction_array = [
                        unicourt.models.bar_source_data_other_jurisdiction_array_inner.BarSourceData_otherJurisdictionArray_inner(
                            bar_number = '', 
                            state = '', )
                        ], 
                    other_name_array = [
                        ''
                        ], 
                    parish = '', 
                    pending_proceeding_array = [
                        ''
                        ], 
                    position = '', 
                    practice_area_array = [
                        ''
                        ], 
                    practice_location_array = [
                        ''
                        ], 
                    private_law_practice = '', 
                    profile_last_certified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    public_hearing_array = [
                        unicourt.models.bar_source_data_public_hearing_array_inner.BarSourceData_publicHearingArray_inner(
                            conduct = '', 
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            issued_by = '', 
                            order = '', 
                            respondent = '', )
                        ], 
                    reason_for_inactivation = unicourt.models.bar_source_data_reason_for_inactivation.BarSourceData_reasonForInactivation(
                        case_number = '', 
                        link = '', ), 
                    sections_array = [
                        ''
                        ], 
                    services_array = [
                        ''
                        ], 
                    source_info = unicourt.models.bar_source_data_source_info.BarSourceData_sourceInfo(
                        url = '', ), 
                    statewide_grievance_committee_history_array = [
                        unicourt.models.bar_source_data_statewide_grievance_committee_history_array_inner.BarSourceData_statewideGrievanceCommitteeHistoryArray_inner(
                            final_decision = '', 
                            final_decision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            grievance_complaint_number = '', 
                            public_comments = '', )
                        ], 
                    status = '', 
                    status_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status_history_array = [
                        unicourt.models.bar_source_data_status_history_array_inner.BarSourceData_statusHistoryArray_inner(
                            effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status_change = '', )
                        ], 
                    ten_year_discipline_array = [
                        unicourt.models.bar_source_data_ten_year_discipline_array_inner.BarSourceData_tenYearDisciplineArray_inner(
                            action_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            reference = '', )
                        ], 
                    undergraduate_school = '', 
                    bar_law_firm = '', 
                    years_of_practice = '', 
                    clients_represented_array = [
                        ''
                        ], 
                    status_hint = '', 
                    advanced_degree_array = [
                        unicourt.models.bar_source_data_advanced_degree_array_inner.BarSourceData_advancedDegreeArray_inner(
                            area = '', 
                            degree = '', )
                        ], 
                    bar_status_array = [
                        unicourt.models.bar_source_data_bar_status_array_inner.BarSourceData_barStatusArray_inner(
                            status = '', 
                            date = '', )
                        ], 
                    related_cases_array = [
                        unicourt.models.bar_source_data_related_cases_array_inner.BarSourceData_relatedCasesArray_inner(
                            case_id = '0', 
                            case_details = '', )
                        ], ),
                contact = unicourt.models.contact.Contact(
                    object = 'Contact', 
                    address_array = [
                        unicourt.models.address.Address(
                            object = 'Address', 
                            street_address1 = '0', 
                            street_address2 = '0', 
                            city = '0', 
                            state_name = 'UNKNOWN', 
                            state_code = '01', 
                            country_name = 'UNKNOWN', 
                            country_code = '01', 
                            zip = '0', 
                            zip4 = '0123', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = -90, 
                            longitude = -180, )
                        ], 
                    phone_number_array = [
                        unicourt.models.phone.Phone(
                            object = 'Phone', 
                            phone_number = '0', 
                            phone_type = 'DEFAULT', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    email_array = [
                        unicourt.models.email.Email(
                            object = 'Email', 
                            email_id = '0', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BarRecord(
                object = 'BarRecord',
                bar_number = '',
                bar_source_type = '',
                admitted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state_code = '',
                status = 'Active',
                inactivation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                bar_source_data = unicourt.models.bar_source_data.BarSourceData(
                    object = 'BarSourceData', 
                    administrative_actions_array = [
                        unicourt.models.bar_source_data_administrative_actions_array_inner.BarSourceData_administrativeActionsArray_inner(
                            case_number = '', 
                            description = '', 
                            effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            resulting_status = '', 
                            type = '', )
                        ], 
                    admission_type = '', 
                    appellate_court_district = '', 
                    appellate_division_department = '', 
                    attorney_group = '', 
                    authorized = '', 
                    bar_service_class = '', 
                    bio = '', 
                    board_certifications_array = [
                        unicourt.models.bar_source_data_board_certifications_array_inner.BarSourceData_boardCertificationsArray_inner(
                            area = '', 
                            year = '', )
                        ], 
                    board_district = '', 
                    circuit = '', 
                    comments = '', 
                    committees_array = [
                        unicourt.models.bar_source_data_committees_array_inner.BarSourceData_committeesArray_inner(
                            committee = '', 
                            office = '', 
                            term = '', )
                        ], 
                    court_history_array = [
                        unicourt.models.bar_source_data_court_history_array_inner.BarSourceData_courtHistoryArray_inner(
                            action = '', 
                            action_comments = '', 
                            reinstated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    court_of_admissions = unicourt.models.bar_source_data_court_of_admissions.BarSourceData_courtOfAdmissions(
                        court_state_array = [
                            ''
                            ], 
                        federal_array = [
                            ''
                            ], 
                        other_courts_array = [
                            ''
                            ], ), 
                    court_service_email = '', 
                    disciplinary_history_array = [
                        unicourt.models.bar_source_data_disciplinary_history_array_inner.BarSourceData_disciplinaryHistoryArray_inner(
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
                            type_of_action = '', )
                        ], 
                    discipline_summaries_array = [
                        unicourt.models.bar_source_data_discipline_summaries_array_inner.BarSourceData_disciplineSummariesArray_inner(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            link = '', 
                            title = '', )
                        ], 
                    dismissals_array = [
                        ''
                        ], 
                    district = '', 
                    employment_history_array = [
                        unicourt.models.bar_source_data_employment_history_array_inner.BarSourceData_employmentHistoryArray_inner(
                            employer = '', 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    fees_options_array = [
                        unicourt.models.bar_source_data_fees_options_array_inner.BarSourceData_feesOptionsArray_inner(
                            contingency_fees = '', 
                            flat_fees = '', 
                            hourly_rate = '', 
                            payment_plans = '', 
                            sliding_scale_fees = '', )
                        ], 
                    firm_size = '', 
                    firm_website = '', 
                    first_admitted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    first_admitted_year = 56, 
                    home_county = '', 
                    in_good_standing = '', 
                    insurance = '', 
                    involvements_array = [
                        unicourt.models.bar_source_data_involvements_array_inner.BarSourceData_involvementsArray_inner(
                            name = '', 
                            position = '', 
                            type = '', )
                        ], 
                    judicial_district = '', 
                    juris_type = '', 
                    languages_array = [
                        ''
                        ], 
                    last_renewal_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    law_school_array = [
                        unicourt.models.bar_source_data_law_school_array_inner.BarSourceData_lawSchoolArray_inner(
                            law_school = '', 
                            law_school_graduated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    legal_speciality_array = [
                        ''
                        ], 
                    license_type = '', 
                    name = unicourt.models.bar_source_data_name.BarSourceData_name(
                        name = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        prefix = '', 
                        suffix = '', ), 
                    next_registration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_renewal_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    open_action_status_array = [
                        unicourt.models.bar_source_data_open_action_status_array_inner.BarSourceData_openActionStatusArray_inner(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            reason = '', )
                        ], 
                    other_jurisdiction_array = [
                        unicourt.models.bar_source_data_other_jurisdiction_array_inner.BarSourceData_otherJurisdictionArray_inner(
                            bar_number = '', 
                            state = '', )
                        ], 
                    other_name_array = [
                        ''
                        ], 
                    parish = '', 
                    pending_proceeding_array = [
                        ''
                        ], 
                    position = '', 
                    practice_area_array = [
                        ''
                        ], 
                    practice_location_array = [
                        ''
                        ], 
                    private_law_practice = '', 
                    profile_last_certified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    public_hearing_array = [
                        unicourt.models.bar_source_data_public_hearing_array_inner.BarSourceData_publicHearingArray_inner(
                            conduct = '', 
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            issued_by = '', 
                            order = '', 
                            respondent = '', )
                        ], 
                    reason_for_inactivation = unicourt.models.bar_source_data_reason_for_inactivation.BarSourceData_reasonForInactivation(
                        case_number = '', 
                        link = '', ), 
                    sections_array = [
                        ''
                        ], 
                    services_array = [
                        ''
                        ], 
                    source_info = unicourt.models.bar_source_data_source_info.BarSourceData_sourceInfo(
                        url = '', ), 
                    statewide_grievance_committee_history_array = [
                        unicourt.models.bar_source_data_statewide_grievance_committee_history_array_inner.BarSourceData_statewideGrievanceCommitteeHistoryArray_inner(
                            final_decision = '', 
                            final_decision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            grievance_complaint_number = '', 
                            public_comments = '', )
                        ], 
                    status = '', 
                    status_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status_history_array = [
                        unicourt.models.bar_source_data_status_history_array_inner.BarSourceData_statusHistoryArray_inner(
                            effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status_change = '', )
                        ], 
                    ten_year_discipline_array = [
                        unicourt.models.bar_source_data_ten_year_discipline_array_inner.BarSourceData_tenYearDisciplineArray_inner(
                            action_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            reference = '', )
                        ], 
                    undergraduate_school = '', 
                    bar_law_firm = '', 
                    years_of_practice = '', 
                    clients_represented_array = [
                        ''
                        ], 
                    status_hint = '', 
                    advanced_degree_array = [
                        unicourt.models.bar_source_data_advanced_degree_array_inner.BarSourceData_advancedDegreeArray_inner(
                            area = '', 
                            degree = '', )
                        ], 
                    bar_status_array = [
                        unicourt.models.bar_source_data_bar_status_array_inner.BarSourceData_barStatusArray_inner(
                            status = '', 
                            date = '', )
                        ], 
                    related_cases_array = [
                        unicourt.models.bar_source_data_related_cases_array_inner.BarSourceData_relatedCasesArray_inner(
                            case_id = '0', 
                            case_details = '', )
                        ], ),
                contact = unicourt.models.contact.Contact(
                    object = 'Contact', 
                    address_array = [
                        unicourt.models.address.Address(
                            object = 'Address', 
                            street_address1 = '0', 
                            street_address2 = '0', 
                            city = '0', 
                            state_name = 'UNKNOWN', 
                            state_code = '01', 
                            country_name = 'UNKNOWN', 
                            country_code = '01', 
                            zip = '0', 
                            zip4 = '0123', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = -90, 
                            longitude = -180, )
                        ], 
                    phone_number_array = [
                        unicourt.models.phone.Phone(
                            object = 'Phone', 
                            phone_number = '0', 
                            phone_type = 'DEFAULT', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    email_array = [
                        unicourt.models.email.Email(
                            object = 'Email', 
                            email_id = '0', 
                            is_visible = True, 
                            first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                first_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_fetch_date_with_updates = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBarRecord(self):
        """Test BarRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
