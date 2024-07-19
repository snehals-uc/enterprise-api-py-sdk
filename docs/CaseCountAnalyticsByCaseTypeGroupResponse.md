# CaseCountAnalyticsByCaseTypeGroupResponse

Case Counts by Case Type Group Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseTypeGroupResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByCaseTypeGroup]**](CaseCountAnalyticsByCaseTypeGroup.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_case_type_group_count** | **int** | Total no. of Case Type Group for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_type_group_response import CaseCountAnalyticsByCaseTypeGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseTypeGroupResponse from a JSON string
case_count_analytics_by_case_type_group_response_instance = CaseCountAnalyticsByCaseTypeGroupResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseTypeGroupResponse.to_json())

# convert the object into a dict
case_count_analytics_by_case_type_group_response_dict = case_count_analytics_by_case_type_group_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseTypeGroupResponse from a dict
case_count_analytics_by_case_type_group_response_from_dict = CaseCountAnalyticsByCaseTypeGroupResponse.from_dict(case_count_analytics_by_case_type_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


