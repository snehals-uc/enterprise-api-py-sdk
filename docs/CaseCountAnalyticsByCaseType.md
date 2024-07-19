# CaseCountAnalyticsByCaseType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseType']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_type** | [**CaseType**](CaseType.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_type import CaseCountAnalyticsByCaseType

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseType from a JSON string
case_count_analytics_by_case_type_instance = CaseCountAnalyticsByCaseType.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseType.to_json())

# convert the object into a dict
case_count_analytics_by_case_type_dict = case_count_analytics_by_case_type_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseType from a dict
case_count_analytics_by_case_type_from_dict = CaseCountAnalyticsByCaseType.from_dict(case_count_analytics_by_case_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


