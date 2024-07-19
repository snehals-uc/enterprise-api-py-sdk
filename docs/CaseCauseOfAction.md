# CaseCauseOfAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CaseCauseOfAction']
**cause_of_action** | [**CauseOfAction**](CauseOfAction.md) |  | 
**cause_of_action_additional_data_array** | [**List[CauseOfActionAdditionalData]**](CauseOfActionAdditionalData.md) |  | 

## Example

```python
from unicourt.models.case_cause_of_action import CaseCauseOfAction

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCauseOfAction from a JSON string
case_cause_of_action_instance = CaseCauseOfAction.from_json(json)
# print the JSON string representation of the object
print(CaseCauseOfAction.to_json())

# convert the object into a dict
case_cause_of_action_dict = case_cause_of_action_instance.to_dict()
# create an instance of CaseCauseOfAction from a dict
case_cause_of_action_from_dict = CaseCauseOfAction.from_dict(case_cause_of_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


