# LawFirmAnalyticsAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'LawFirmAnalyticsAPI']
**norm_law_firm_api** | **str** | Link to Details for the Law Firm. | 
**associated_norm_attorney_api** | **str** |  | 
**associated_norm_judge_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_attorney_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_law_firm_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_party_api** | **str** |  | 

## Example

```python
from unicourt.models.law_firm_analytics_api import LawFirmAnalyticsAPI

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmAnalyticsAPI from a JSON string
law_firm_analytics_api_instance = LawFirmAnalyticsAPI.from_json(json)
# print the JSON string representation of the object
print(LawFirmAnalyticsAPI.to_json())

# convert the object into a dict
law_firm_analytics_api_dict = law_firm_analytics_api_instance.to_dict()
# create an instance of LawFirmAnalyticsAPI from a dict
law_firm_analytics_api_from_dict = LawFirmAnalyticsAPI.from_dict(law_firm_analytics_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


