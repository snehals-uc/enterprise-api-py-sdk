# CaseCountAnalyticsByNormAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormAttorney']
**norm_attorney_id** | **str** |  | 
**norm_attorney_name** | **str** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_count** | **int** |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_attorney import CaseCountAnalyticsByNormAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormAttorney from a JSON string
case_count_analytics_by_norm_attorney_instance = CaseCountAnalyticsByNormAttorney.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormAttorney.to_json())

# convert the object into a dict
case_count_analytics_by_norm_attorney_dict = case_count_analytics_by_norm_attorney_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormAttorney from a dict
case_count_analytics_by_norm_attorney_from_dict = CaseCountAnalyticsByNormAttorney.from_dict(case_count_analytics_by_norm_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


