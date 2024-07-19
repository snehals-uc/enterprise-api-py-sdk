# Case


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Case']
**case_id** | **str** | Unique identifier of Case. | 
**url** | **str** | URL to the case page in UniCourt Application. | 
**case_number** | **str** | Case number as provided by Court. | 
**case_name** | **str** | Case name as provided by Court. | 
**filed_date** | **datetime** | Filing date for the case provided by the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz | 
**has_only_meta_info** | **bool** | This field determines if this case object has only meta information. If the value is true and if the full information is required you would need to call the updateCase API. | 
**court_service_status_id** | **str** | Court Service Status ID of the requested case where we can use it to get the service status | 
**court_service_status_api** | **str** | API to get the service statuses of the given case. | 
**court** | [**Court**](Court.md) |  | 
**court_location** | [**CourtLocation**](CourtLocation.md) |  | 
**case_type** | [**CaseType**](CaseType.md) |  | 
**charge_array** | [**List[CaseCharge]**](CaseCharge.md) | Array of charges that are added to this case. | 
**case_status** | [**CaseStatus**](CaseStatus.md) |  | 
**cause_of_action_array** | [**List[CaseCauseOfAction]**](CaseCauseOfAction.md) | Array of cause of Actions that are added to this case. | 
**first_fetch_date** | **datetime** | The date and time when the case was first fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,. | 
**last_fetch_date** | **datetime** | The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist. | 
**last_fetch_date_with_updates** | **datetime** | The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, | 
**participants_last_fetch_date** | **datetime** | The date and time when parties/attorneys were last updated from the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: This is currently applicable for Federal PACER cases since we have an option to exclude parties and fetch only latest docket entries when updating cases to save PACER fees. | 
**source_data_status** | **str** | The status of source data of case. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Case has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site. | 
**source_case_data** | [**SourceCaseData**](SourceCaseData.md) |  | 
**has_documents_with_preview** | **bool** | This field will be set to TRUE if atleast one document has a preview. | 
**export_api** | **str** | When a case is beyond the threshold of entities we provide this link so that the user can request and get all the data of the case with one additional call. This data will be zipped and sent via a webhoook. | 
**case_stats** | [**CaseStats**](CaseStats.md) |  | 
**parties** | [**Parties**](Parties.md) |  | 
**attorneys** | [**Attorneys**](Attorneys.md) |  | 
**judges** | [**Judges**](Judges.md) |  | 
**docket_entries** | [**DocketEntries**](DocketEntries.md) |  | 
**hearings** | [**Hearings**](Hearings.md) |  | 
**case_documents** | [**CaseDocuments**](CaseDocuments.md) |  | 
**related_cases** | [**RelatedCases**](RelatedCases.md) |  | 

## Example

```python
from unicourt.models.case import Case

# TODO update the JSON string below
json = "{}"
# create an instance of Case from a JSON string
case_instance = Case.from_json(json)
# print the JSON string representation of the object
print(Case.to_json())

# convert the object into a dict
case_dict = case_instance.to_dict()
# create an instance of Case from a dict
case_from_dict = Case.from_dict(case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


