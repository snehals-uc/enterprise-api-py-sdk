# CaseCountAnalyticsByAreaOfLaw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByAreaOfLaw']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**area_of_law** | [**AreaOfLaw**](AreaOfLaw.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_area_of_law import CaseCountAnalyticsByAreaOfLaw

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByAreaOfLaw from a JSON string
case_count_analytics_by_area_of_law_instance = CaseCountAnalyticsByAreaOfLaw.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByAreaOfLaw.to_json())

# convert the object into a dict
case_count_analytics_by_area_of_law_dict = case_count_analytics_by_area_of_law_instance.to_dict()
# create an instance of CaseCountAnalyticsByAreaOfLaw from a dict
case_count_analytics_by_area_of_law_from_dict = CaseCountAnalyticsByAreaOfLaw.from_dict(case_count_analytics_by_area_of_law_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


