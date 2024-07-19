# CaseCountAnalyticsByNormLawFirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormLawFirm']
**norm_law_firm_id** | **str** |  | 
**norm_law_firm_name** | **str** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_count** | **int** |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_law_firm import CaseCountAnalyticsByNormLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormLawFirm from a JSON string
case_count_analytics_by_norm_law_firm_instance = CaseCountAnalyticsByNormLawFirm.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormLawFirm.to_json())

# convert the object into a dict
case_count_analytics_by_norm_law_firm_dict = case_count_analytics_by_norm_law_firm_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormLawFirm from a dict
case_count_analytics_by_norm_law_firm_from_dict = CaseCountAnalyticsByNormLawFirm.from_dict(case_count_analytics_by_norm_law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


