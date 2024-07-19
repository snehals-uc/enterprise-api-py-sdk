# CauseOfActionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CauseOfActionGroup']
**cause_of_action_group_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.cause_of_action_group import CauseOfActionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CauseOfActionGroup from a JSON string
cause_of_action_group_instance = CauseOfActionGroup.from_json(json)
# print the JSON string representation of the object
print(CauseOfActionGroup.to_json())

# convert the object into a dict
cause_of_action_group_dict = cause_of_action_group_instance.to_dict()
# create an instance of CauseOfActionGroup from a dict
cause_of_action_group_from_dict = CauseOfActionGroup.from_dict(cause_of_action_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


