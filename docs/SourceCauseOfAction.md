# SourceCauseOfAction

Source Cause of Action data from the source site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'SourceCauseOfAction']
**is_visible** | **bool** | Signifies if the cause of action is currently isVisible or not for the case. | 
**source_cause_of_action_raw** | **str** | Raw Cause of Action data from the source site. | 
**source_cause_of_action** | **str** | Cause of Action data from the source site. | 
**source_statute** | **str** | Statute of a Cause of Action. | 
**first_fetch_date** | **str** | When this Cause of Action was first fetched from the court site. | 
**last_fetch_date** | **str** | When this Cause of Action was last fetched from the court site. | 

## Example

```python
from unicourt.models.source_cause_of_action import SourceCauseOfAction

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCauseOfAction from a JSON string
source_cause_of_action_instance = SourceCauseOfAction.from_json(json)
# print the JSON string representation of the object
print(SourceCauseOfAction.to_json())

# convert the object into a dict
source_cause_of_action_dict = source_cause_of_action_instance.to_dict()
# create an instance of SourceCauseOfAction from a dict
source_cause_of_action_from_dict = SourceCauseOfAction.from_dict(source_cause_of_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


