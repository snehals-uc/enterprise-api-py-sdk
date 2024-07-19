# CaseAnalyticsAPI

Provides Court Data per State Jurisdiction for an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseAnalyticsAPI']
**case_count_analytics_by_court_api** | **str** |  | 
**case_count_analytics_by_court_type_api** | **str** |  | 
**case_count_analytics_by_court_system_api** | **str** |  | 
**case_count_analytics_by_court_location_api** | **str** |  | 
**case_count_analytics_by_jurisdiction_geo_api** | **str** |  | 
**case_count_analytics_by_area_of_law_api** | **str** |  | 
**case_count_analytics_by_case_class_api** | **str** |  | 
**case_count_analytics_by_case_type_api** | **str** |  | 
**case_count_analytics_by_case_type_group_api** | **str** |  | 
**case_count_analytics_by_party_role_api** | **str** |  | 
**case_count_analytics_by_party_role_group_api** | **str** |  | 
**total_cases** | **int** |  | 

## Example

```python
from unicourt.models.case_analytics_api import CaseAnalyticsAPI

# TODO update the JSON string below
json = "{}"
# create an instance of CaseAnalyticsAPI from a JSON string
case_analytics_api_instance = CaseAnalyticsAPI.from_json(json)
# print the JSON string representation of the object
print(CaseAnalyticsAPI.to_json())

# convert the object into a dict
case_analytics_api_dict = case_analytics_api_instance.to_dict()
# create an instance of CaseAnalyticsAPI from a dict
case_analytics_api_from_dict = CaseAnalyticsAPI.from_dict(case_analytics_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


