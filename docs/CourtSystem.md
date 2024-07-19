# CourtSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtSystem']
**court_type_id** | **str** |  | 
**court_system_id** | **str** |  | 
**court_type** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.court_system import CourtSystem

# TODO update the JSON string below
json = "{}"
# create an instance of CourtSystem from a JSON string
court_system_instance = CourtSystem.from_json(json)
# print the JSON string representation of the object
print(CourtSystem.to_json())

# convert the object into a dict
court_system_dict = court_system_instance.to_dict()
# create an instance of CourtSystem from a dict
court_system_from_dict = CourtSystem.from_dict(court_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


