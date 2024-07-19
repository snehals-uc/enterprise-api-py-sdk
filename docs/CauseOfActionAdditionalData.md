# CauseOfActionAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CauseOfActionAdditionalData']
**cause_of_action_additional_data_id** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.cause_of_action_additional_data import CauseOfActionAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of CauseOfActionAdditionalData from a JSON string
cause_of_action_additional_data_instance = CauseOfActionAdditionalData.from_json(json)
# print the JSON string representation of the object
print(CauseOfActionAdditionalData.to_json())

# convert the object into a dict
cause_of_action_additional_data_dict = cause_of_action_additional_data_instance.to_dict()
# create an instance of CauseOfActionAdditionalData from a dict
cause_of_action_additional_data_from_dict = CauseOfActionAdditionalData.from_dict(cause_of_action_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


