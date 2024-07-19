# CaseCountAnalyticsByCaseTypeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseTypeGroup']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_type_group** | [**CaseTypeGroup**](CaseTypeGroup.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_type_group import CaseCountAnalyticsByCaseTypeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseTypeGroup from a JSON string
case_count_analytics_by_case_type_group_instance = CaseCountAnalyticsByCaseTypeGroup.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseTypeGroup.to_json())

# convert the object into a dict
case_count_analytics_by_case_type_group_dict = case_count_analytics_by_case_type_group_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseTypeGroup from a dict
case_count_analytics_by_case_type_group_from_dict = CaseCountAnalyticsByCaseTypeGroup.from_dict(case_count_analytics_by_case_type_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


