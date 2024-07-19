# CaseCountAnalyticsByNormParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormParty']
**norm_party_id** | **str** |  | 
**norm_party_name** | **str** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_count** | **int** |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_party import CaseCountAnalyticsByNormParty

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormParty from a JSON string
case_count_analytics_by_norm_party_instance = CaseCountAnalyticsByNormParty.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormParty.to_json())

# convert the object into a dict
case_count_analytics_by_norm_party_dict = case_count_analytics_by_norm_party_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormParty from a dict
case_count_analytics_by_norm_party_from_dict = CaseCountAnalyticsByNormParty.from_dict(case_count_analytics_by_norm_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


