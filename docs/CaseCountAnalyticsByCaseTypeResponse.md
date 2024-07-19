# CaseCountAnalyticsByCaseTypeResponse

Case Counts by Case Types Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseTypeResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByCaseType]**](CaseCountAnalyticsByCaseType.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_case_type_count** | **int** | Total no. of CaseType for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_type_response import CaseCountAnalyticsByCaseTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseTypeResponse from a JSON string
case_count_analytics_by_case_type_response_instance = CaseCountAnalyticsByCaseTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseTypeResponse.to_json())

# convert the object into a dict
case_count_analytics_by_case_type_response_dict = case_count_analytics_by_case_type_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseTypeResponse from a dict
case_count_analytics_by_case_type_response_from_dict = CaseCountAnalyticsByCaseTypeResponse.from_dict(case_count_analytics_by_case_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


