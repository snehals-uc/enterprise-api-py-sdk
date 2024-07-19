# CaseCountAnalyticsByPartyRoleResponse

Case Count by Party Type Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByPartyRoleResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByPartyRole]**](CaseCountAnalyticsByPartyRole.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_party_role_count** | **int** | Total no. of Party Role for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_party_role_response import CaseCountAnalyticsByPartyRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByPartyRoleResponse from a JSON string
case_count_analytics_by_party_role_response_instance = CaseCountAnalyticsByPartyRoleResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByPartyRoleResponse.to_json())

# convert the object into a dict
case_count_analytics_by_party_role_response_dict = case_count_analytics_by_party_role_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByPartyRoleResponse from a dict
case_count_analytics_by_party_role_response_from_dict = CaseCountAnalyticsByPartyRoleResponse.from_dict(case_count_analytics_by_party_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


