# CourtLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtLocation']
**court_location_id** | **str** |  | 
**name** | **str** |  | 
**street_address1** | **str** | 1st part of the street address. | 
**street_address2** | **str** | 2nd part of the street address. | 
**city** | **str** | City | 
**state_name** | **str** | State Name if present else default value. | [default to 'UNKNOWN']
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 
**courts_for_court_location_api** | **str** |  | 
**court_service_status_api** | **str** |  | 

## Example

```python
from unicourt.models.court_location import CourtLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CourtLocation from a JSON string
court_location_instance = CourtLocation.from_json(json)
# print the JSON string representation of the object
print(CourtLocation.to_json())

# convert the object into a dict
court_location_dict = court_location_instance.to_dict()
# create an instance of CourtLocation from a dict
court_location_from_dict = CourtLocation.from_dict(court_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


