# AttorneyAnalyticsAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AttorneyAnalyticsAPI']
**norm_attorney_api** | **str** | Link to Details for the Attorney. | 
**associated_norm_judges_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_attorney_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_law_firm_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_party_api** | **str** |  | 

## Example

```python
from unicourt.models.attorney_analytics_api import AttorneyAnalyticsAPI

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyAnalyticsAPI from a JSON string
attorney_analytics_api_instance = AttorneyAnalyticsAPI.from_json(json)
# print the JSON string representation of the object
print(AttorneyAnalyticsAPI.to_json())

# convert the object into a dict
attorney_analytics_api_dict = attorney_analytics_api_instance.to_dict()
# create an instance of AttorneyAnalyticsAPI from a dict
attorney_analytics_api_from_dict = AttorneyAnalyticsAPI.from_dict(attorney_analytics_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


