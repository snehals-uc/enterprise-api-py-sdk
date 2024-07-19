# PartyAnalyticsAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'PartyAnalyticsAPI']
**norm_party_api** | **str** | Link to Details for the Party. | 
**associated_norm_attorneys_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_judges_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_attorney_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_law_firm_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_party_api** | **str** |  | 

## Example

```python
from unicourt.models.party_analytics_api import PartyAnalyticsAPI

# TODO update the JSON string below
json = "{}"
# create an instance of PartyAnalyticsAPI from a JSON string
party_analytics_api_instance = PartyAnalyticsAPI.from_json(json)
# print the JSON string representation of the object
print(PartyAnalyticsAPI.to_json())

# convert the object into a dict
party_analytics_api_dict = party_analytics_api_instance.to_dict()
# create an instance of PartyAnalyticsAPI from a dict
party_analytics_api_from_dict = PartyAnalyticsAPI.from_dict(party_analytics_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


