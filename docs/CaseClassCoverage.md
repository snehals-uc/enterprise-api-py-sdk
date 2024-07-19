# CaseClassCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CaseClassCoverage']
**case_class** | [**CaseClass**](CaseClass.md) |  | 
**court_service_status_api** | **str** | API Link to the Court Service status with filters of court and case class | 
**case_count** | **int** | Total Cases for a specific CourtLocation. | 
**cases_in_last_thirty_days_count** | **int** | Cases in last 30 days that were added to UniCourt for a specific CourtLocation | 
**free_case_document_count** | **int** | Free Case Documents for a specific CourtLocation. | 
**free_case_documents_in_last_thirty_days_count** | **int** | Free Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation. | 
**paid_case_document_count** | **int** | Paid Case Documents for a specific CourtLocation. | 
**paid_case_documents_in_last_thirty_days_count** | **int** | Paid Case Documents in last 30 days that were added to UniCourt for a specific CourtLocation. | 
**case_document_in_library_count** | **int** | Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocationy. | 
**case_document_in_library_in_last_thirty_days_count** | **int** | Case Documents that were added to UniCourt Crowd Source Library for a specific CourtLocation in last 30 days. | 

## Example

```python
from unicourt.models.case_class_coverage import CaseClassCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of CaseClassCoverage from a JSON string
case_class_coverage_instance = CaseClassCoverage.from_json(json)
# print the JSON string representation of the object
print(CaseClassCoverage.to_json())

# convert the object into a dict
case_class_coverage_dict = case_class_coverage_instance.to_dict()
# create an instance of CaseClassCoverage from a dict
case_class_coverage_from_dict = CaseClassCoverage.from_dict(case_class_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


