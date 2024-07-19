# Court


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Court']
**court_id** | **str** |  | 
**court_type_id** | **str** |  | 
**court_system_id** | **str** |  | 
**type** | **str** |  | 
**system** | **str** |  | 
**name** | **str** |  | 
**name_aka** | **str** |  | 
**additional_levels** | [**AdditionalLevels**](AdditionalLevels.md) |  | 
**container_type** | **str** |  | 
**container** | **str** |  | 
**created_date** | **datetime** | The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 
**jurisdiction_geo_for_court_api** | **str** |  | 
**court_locations_for_court_api** | **str** |  | 
**appeal_courts_for_court_api** | **str** |  | 
**court_service_status_api** | **str** |  | 

## Example

```python
from unicourt.models.court import Court

# TODO update the JSON string below
json = "{}"
# create an instance of Court from a JSON string
court_instance = Court.from_json(json)
# print the JSON string representation of the object
print(Court.to_json())

# convert the object into a dict
court_dict = court_instance.to_dict()
# create an instance of Court from a dict
court_from_dict = Court.from_dict(court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


