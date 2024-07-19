# JudgeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'JudgeType']
**judge_type_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.judge_type import JudgeType

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeType from a JSON string
judge_type_instance = JudgeType.from_json(json)
# print the JSON string representation of the object
print(JudgeType.to_json())

# convert the object into a dict
judge_type_dict = judge_type_instance.to_dict()
# create an instance of JudgeType from a dict
judge_type_from_dict = JudgeType.from_dict(judge_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


