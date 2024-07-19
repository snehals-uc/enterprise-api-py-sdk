# CaseCountAnalyticsByCourtTypeResponse

Case Counts by Court Type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourtTypeResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByCourtType]**](CaseCountAnalyticsByCourtType.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_court_type_count** | **int** | Total no. of Court Type for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_court_type_response import CaseCountAnalyticsByCourtTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourtTypeResponse from a JSON string
case_count_analytics_by_court_type_response_instance = CaseCountAnalyticsByCourtTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourtTypeResponse.to_json())

# convert the object into a dict
case_count_analytics_by_court_type_response_dict = case_count_analytics_by_court_type_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourtTypeResponse from a dict
case_count_analytics_by_court_type_response_from_dict = CaseCountAnalyticsByCourtTypeResponse.from_dict(case_count_analytics_by_court_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


