# BarSourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'BarSourceData']
**administrative_actions_array** | [**List[BarSourceDataAdministrativeActionsArrayInner]**](BarSourceDataAdministrativeActionsArrayInner.md) |  | 
**admission_type** | **str** |  | 
**appellate_court_district** | **str** |  | 
**appellate_division_department** | **str** |  | 
**attorney_group** | **str** |  | 
**authorized** | **str** |  | 
**bar_service_class** | **str** |  | 
**bio** | **str** |  | 
**board_certifications_array** | [**List[BarSourceDataBoardCertificationsArrayInner]**](BarSourceDataBoardCertificationsArrayInner.md) |  | 
**board_district** | **str** |  | 
**circuit** | **str** |  | 
**comments** | **str** |  | 
**committees_array** | [**List[BarSourceDataCommitteesArrayInner]**](BarSourceDataCommitteesArrayInner.md) |  | 
**court_history_array** | [**List[BarSourceDataCourtHistoryArrayInner]**](BarSourceDataCourtHistoryArrayInner.md) |  | 
**court_of_admissions** | [**BarSourceDataCourtOfAdmissions**](BarSourceDataCourtOfAdmissions.md) |  | 
**court_service_email** | **str** |  | 
**disciplinary_history_array** | [**List[BarSourceDataDisciplinaryHistoryArrayInner]**](BarSourceDataDisciplinaryHistoryArrayInner.md) |  | 
**discipline_summaries_array** | [**List[BarSourceDataDisciplineSummariesArrayInner]**](BarSourceDataDisciplineSummariesArrayInner.md) |  | 
**dismissals_array** | **List[str]** |  | 
**district** | **str** |  | 
**employment_history_array** | [**List[BarSourceDataEmploymentHistoryArrayInner]**](BarSourceDataEmploymentHistoryArrayInner.md) |  | 
**expiration_date** | **datetime** |  | 
**fees_options_array** | [**List[BarSourceDataFeesOptionsArrayInner]**](BarSourceDataFeesOptionsArrayInner.md) |  | 
**firm_size** | **str** |  | 
**firm_website** | **str** |  | 
**first_admitted_date** | **datetime** | The firstAdmittedDate is the date when an attorney was admitted to the bar for the very first time regardless of which U.S state. | 
**first_admitted_year** | **int** |  | 
**home_county** | **str** |  | 
**in_good_standing** | **str** |  | 
**insurance** | **str** |  | 
**involvements_array** | [**List[BarSourceDataInvolvementsArrayInner]**](BarSourceDataInvolvementsArrayInner.md) |  | 
**judicial_district** | **str** |  | 
**juris_type** | **str** |  | 
**languages_array** | **List[str]** |  | 
**last_renewal_date** | **datetime** |  | 
**law_school_array** | [**List[BarSourceDataLawSchoolArrayInner]**](BarSourceDataLawSchoolArrayInner.md) |  | 
**legal_speciality_array** | **List[str]** |  | 
**license_type** | **str** |  | 
**name** | [**BarSourceDataName**](BarSourceDataName.md) |  | 
**next_registration** | **datetime** |  | 
**next_renewal_date** | **datetime** |  | 
**open_action_status_array** | [**List[BarSourceDataOpenActionStatusArrayInner]**](BarSourceDataOpenActionStatusArrayInner.md) |  | 
**other_jurisdiction_array** | [**List[BarSourceDataOtherJurisdictionArrayInner]**](BarSourceDataOtherJurisdictionArrayInner.md) |  | 
**other_name_array** | **List[str]** |  | 
**parish** | **str** |  | 
**pending_proceeding_array** | **List[str]** |  | 
**position** | **str** |  | 
**practice_area_array** | **List[str]** |  | 
**practice_location_array** | **List[str]** |  | 
**private_law_practice** | **str** |  | 
**profile_last_certified** | **datetime** |  | 
**public_hearing_array** | [**List[BarSourceDataPublicHearingArrayInner]**](BarSourceDataPublicHearingArrayInner.md) |  | 
**reason_for_inactivation** | [**BarSourceDataReasonForInactivation**](BarSourceDataReasonForInactivation.md) |  | 
**sections_array** | **List[str]** |  | 
**services_array** | **List[str]** |  | 
**source_info** | [**BarSourceDataSourceInfo**](BarSourceDataSourceInfo.md) |  | 
**statewide_grievance_committee_history_array** | [**List[BarSourceDataStatewideGrievanceCommitteeHistoryArrayInner]**](BarSourceDataStatewideGrievanceCommitteeHistoryArrayInner.md) |  | 
**status** | **str** |  | 
**status_date** | **datetime** |  | 
**status_history_array** | [**List[BarSourceDataStatusHistoryArrayInner]**](BarSourceDataStatusHistoryArrayInner.md) |  | 
**ten_year_discipline_array** | [**List[BarSourceDataTenYearDisciplineArrayInner]**](BarSourceDataTenYearDisciplineArrayInner.md) |  | 
**undergraduate_school** | **str** |  | 
**bar_law_firm** | **str** |  | 
**years_of_practice** | **str** |  | 
**clients_represented_array** | **List[str]** |  | 
**status_hint** | **str** |  | 
**advanced_degree_array** | [**List[BarSourceDataAdvancedDegreeArrayInner]**](BarSourceDataAdvancedDegreeArrayInner.md) |  | 
**bar_status_array** | [**List[BarSourceDataBarStatusArrayInner]**](BarSourceDataBarStatusArrayInner.md) |  | 
**related_cases_array** | [**List[BarSourceDataRelatedCasesArrayInner]**](BarSourceDataRelatedCasesArrayInner.md) |  | 

## Example

```python
from unicourt.models.bar_source_data import BarSourceData

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceData from a JSON string
bar_source_data_instance = BarSourceData.from_json(json)
# print the JSON string representation of the object
print(BarSourceData.to_json())

# convert the object into a dict
bar_source_data_dict = bar_source_data_instance.to_dict()
# create an instance of BarSourceData from a dict
bar_source_data_from_dict = BarSourceData.from_dict(bar_source_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


