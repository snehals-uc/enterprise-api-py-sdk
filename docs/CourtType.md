# CourtType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtType']
**court_type_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.court_type import CourtType

# TODO update the JSON string below
json = "{}"
# create an instance of CourtType from a JSON string
court_type_instance = CourtType.from_json(json)
# print the JSON string representation of the object
print(CourtType.to_json())

# convert the object into a dict
court_type_dict = court_type_instance.to_dict()
# create an instance of CourtType from a dict
court_type_from_dict = CourtType.from_dict(court_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


