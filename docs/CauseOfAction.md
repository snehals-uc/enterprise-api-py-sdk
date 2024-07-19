# CauseOfAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CauseOfAction']
**cause_of_action_id** | **str** |  | 
**cause_of_action_group_id** | **str** |  | 
**cause_of_action_group** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.cause_of_action import CauseOfAction

# TODO update the JSON string below
json = "{}"
# create an instance of CauseOfAction from a JSON string
cause_of_action_instance = CauseOfAction.from_json(json)
# print the JSON string representation of the object
print(CauseOfAction.to_json())

# convert the object into a dict
cause_of_action_dict = cause_of_action_instance.to_dict()
# create an instance of CauseOfAction from a dict
cause_of_action_from_dict = CauseOfAction.from_dict(cause_of_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


