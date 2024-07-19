# CaseCountAnalyticsByCaseClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseClass']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_class** | [**CaseClass**](CaseClass.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_class import CaseCountAnalyticsByCaseClass

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseClass from a JSON string
case_count_analytics_by_case_class_instance = CaseCountAnalyticsByCaseClass.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseClass.to_json())

# convert the object into a dict
case_count_analytics_by_case_class_dict = case_count_analytics_by_case_class_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseClass from a dict
case_count_analytics_by_case_class_from_dict = CaseCountAnalyticsByCaseClass.from_dict(case_count_analytics_by_case_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


