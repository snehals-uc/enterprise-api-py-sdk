import os
import pickle
import unicourt
from unicourt.sdk import Authentication, CaseDocket, CaseSearch

unicourt.CLIENT_ID = os.getenv("CLIENT_ID")
unicourt.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
auth_obj, http_status_code = Authentication.generate_new_token()

try:
    business = "john"

    # Execute Case-Search Request
    cases, _ = CaseSearch.search_cases(q=f'caseName:({business})', order='desc', sort='filedDate', page_number=1)

    case, status = CaseDocket.get_case(cases.case_search_result_array[0].case_id) # cases['case_search_result_array'][0]['case_id'] will not be supported
    print("The case object:")
    print(case)

    # To pickle the case object or to store the object in file and re-load
    with open('testpickle.pkl', 'wb') as file:
        pickle.dump(case, file)

    with open('testpickle.pkl', 'rb') as file:
        loaded_object = pickle.load(file)

except Exception as e:
    print(e)

# # Invalidate the generated access token
Authentication.invalidate_token()

# <class 'unicourt.models.case.Case'>
# Object for the above print is a python object not json
# object='Case' case_id='CASEgk55bf73b161a3' url='https://unicourt.com/case/urc-CASEgk55bf73b161a3' case_number='24-1509' case_name='William Gooch v. John Hickenlooper' filed_date=datetime.datetime(2024, 6, 5, 0, 0, tzinfo=TzInfo(UTC)) has_only_meta_info=True court_service_status_id='CTSSbfcab0d9ce90bd' court_service_status_api='https://enterpriseapi.staging.unicourt.com/masterData/courtServiceStatus/CTSSbfcab0d9ce90bd' court=Court(object='Court', court_id='CORTLMDMgPhsoGonRj', court_type_id='COTPLurdwRD5jyKSYb', court_system_id='COSYKbTM5W3zTCNN6j', type='Federal', system='U.S. Courts of Appeals', name='Court of Appeals for the Fourth Circuit', name_aka='U.S. Court of Appeals for the Fourth Circuit', additional_levels=None, container_type='Circuit', container='4', created_date=datetime.datetime(2022, 7, 8, 5, 49, 49, tzinfo=TzInfo(UTC)), jurisdiction_geo_for_court_api='https://enterpriseapi.staging.unicourt.com/masterData/court/CORTLMDMgPhsoGonRj/jurisdictionGeo', court_locations_for_court_api='https://enterpriseapi.staging.unicourt.com/masterData/court/CORTLMDMgPhsoGonRj/courtLocations', appeal_courts_for_court_api='https://enterpriseapi.staging.unicourt.com/masterData/court/CORTLMDMgPhsoGonRj/appealCourts', court_service_status_api='https://enterpriseapi.staging.unicourt.com/masterData/courtServiceStatus?q=Court%3A%28courtId%3A%22CORTLMDMgPhsoGonRj%22%29') court_location=CourtLocation(object='CourtLocation', court_location_id='COLOC5ePxrputwDbyC', name='Lewis F. Powell, Jr. U.S. Courthouse Annex', street_address1='1100 E Main St', street_address2=None, city='Richmond', state_name='Virginia', created_date=datetime.datetime(2022, 7, 8, 5, 49, 56, tzinfo=TzInfo(UTC)), courts_for_court_location_api='https://enterpriseapi.staging.unicourt.com/masterData/courtLocation/COLOC5ePxrputwDbyC/courts', court_service_status_api='https://enterpriseapi.staging.unicourt.com/masterData/courtServiceStatus?q=CourtLocation%3A%28courtLocationId%3A%22COLOC5ePxrputwDbyC%22%29') case_type=CaseType(object='CaseType', case_type_id='CTYPWfxVDrHw4JiiQ3', case_class_id='CSCLNjbKTN7Yfo2wdb', area_of_law_id='AOFLWfxVDrHw4JiiQ3', case_type_group_id=None, case_class='Civil', area_of_law='Constitutional and Civil Rights', case_type_group=None, name=None, sali_code='CIVR', case_type_tag=None, created_date=datetime.datetime(2022, 3, 28, 4, 58, 36, tzinfo=TzInfo(UTC))) charge_array=[] case_status=CaseStatus(object='CaseStatus', case_status_id='CSSTVnE3shD3CGtkcZ', case_status_group_id='CSSGCYoBCJ3A8j4MX4', case_status_group='Open', name='Open', case_class_array=['Civil', 'Criminal'], created_date=datetime.datetime(2022, 3, 28, 4, 58, 47, tzinfo=TzInfo(UTC))) cause_of_action_array=[] first_fetch_date=datetime.datetime(2024, 6, 24, 7, 23, 33, tzinfo=TzInfo(UTC)) last_fetch_date=datetime.datetime(2024, 6, 24, 7, 23, 33, tzinfo=TzInfo(UTC)) last_fetch_date_with_updates=datetime.datetime(2024, 6, 24, 7, 23, 33, tzinfo=TzInfo(UTC)) participants_last_fetch_date=None source_data_status=None source_case_data=SourceCaseData(object='SourceCaseData', source_court='04CAE', source_case_type='3440', source_charge_array=[], nature_of_suit_array=[], source_cause_of_action_array=[], source_case_status='PENDING', source_page_data=[]) has_documents_with_preview=False export_api='https://enterpriseapi.staging.unicourt.com/caseExport/CASEgk55bf73b161a3' case_stats=CaseStats(object='CaseStats', party_count=0, attorney_count=0, judge_count=0, docket_entry_count=0, free_case_document_count=0, paid_case_document_count=0, all_case_document_count=0, case_document_in_library_count=0, hearing_count=0, related_case_count=0) parties=Parties(object='Parties', page_number=1, party_array=[], next_page_api=None, total_pages=0, total_count=0) attorneys=Attorneys(object='Attorneys', page_number=1, attorney_array=[], next_page_api=None, total_pages=0, total_count=0) judges=Judges(object='Judges', page_number=1, judge_array=[], next_page_api=None, total_pages=0, total_count=0) docket_entries=DocketEntries(object='DocketEntries', page_number=1, docket_entry_array=[], next_page_api=None, total_pages=0, total_count=0) hearings=Hearings(object='Hearings', page_number=1, hearing_array=[], next_page_api=None, total_pages=0, total_count=0) case_documents=CaseDocuments(object='CaseDocuments', page_number=1, case_document_array=[], next_page_api=None, total_pages=0, total_count=0) related_cases=RelatedCases(object='RelatedCases', page_number=1, related_case_array=[], next_page_api=None, total_pages=0, total_count=0)