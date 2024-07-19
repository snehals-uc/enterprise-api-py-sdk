# CaseStats

Count of each entitiy of a case is mentioned here so that you can calculate the number of requests needs to be done to obtain each entity results completely.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CaseStats']
**party_count** | **int** | Count of number of parties available in the case being requested for. | 
**attorney_count** | **int** | Count of number of attornies available in the case being requested for. | 
**judge_count** | **int** | Count of number of judges available in the case being requested for. | 
**docket_entry_count** | **int** | Count of number of docket entries available in the case being requested for. | 
**free_case_document_count** | **int** | Count of number of free documents available in the case being requested for. | 
**paid_case_document_count** | **int** | Count of number of paid documents available in the case being requested for. | 
**all_case_document_count** | **int** | Count which includes the freeCaseDocumentCount and paidCaseDocumentCount. | 
**case_document_in_library_count** | **int** | Count of number of documents that are available in the UniCourt CrowdSourced Library for the case being requested for. | 
**hearing_count** | **int** | Count of number of hearings available in the case being requested for. | 
**related_case_count** | **int** | Count of related cases that are available in the case being requested. | 

## Example

```python
from unicourt.models.case_stats import CaseStats

# TODO update the JSON string below
json = "{}"
# create an instance of CaseStats from a JSON string
case_stats_instance = CaseStats.from_json(json)
# print the JSON string representation of the object
print(CaseStats.to_json())

# convert the object into a dict
case_stats_dict = case_stats_instance.to_dict()
# create an instance of CaseStats from a dict
case_stats_from_dict = CaseStats.from_dict(case_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


