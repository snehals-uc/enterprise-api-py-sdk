# CourtCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CourtCoverage']
**last_update_count_date** | **str** | Date when it was last updated. | 
**court** | [**Court**](Court.md) |  | 
**total_case_count** | **int** | Total Cases for a specific court. | 
**total_cases_in_last_thirty_days_count** | **int** | Total Cases in last 30 days that were added to UniCourt | 
**total_free_case_document_count** | **int** | Total Free Case Documents for a specific court. | 
**total_free_case_documents_in_last_thirty_days_count** | **int** | Total Free Case Documents in last 30 days that were added to UniCourt | 
**total_paid_case_document_count** | **int** | Total Paid Case Documents for a specific court. | 
**total_paid_case_documents_in_last_thirty_days_count** | **int** | Total Paid Case Documents in last 30 days that were added to UniCourt | 
**total_case_document_in_library_count** | **int** | Count of total Case Documents added in UniCourt Library. | 
**total_case_document_in_library_in_last_thirty_days_count** | **int** | Count of total Case Documents added in UniCourt Library in last 30 days | 
**case_class_coverage_array** | [**List[CaseClassCoverage]**](CaseClassCoverage.md) |  | 

## Example

```python
from unicourt.models.court_coverage import CourtCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of CourtCoverage from a JSON string
court_coverage_instance = CourtCoverage.from_json(json)
# print the JSON string representation of the object
print(CourtCoverage.to_json())

# convert the object into a dict
court_coverage_dict = court_coverage_instance.to_dict()
# create an instance of CourtCoverage from a dict
court_coverage_from_dict = CourtCoverage.from_dict(court_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


