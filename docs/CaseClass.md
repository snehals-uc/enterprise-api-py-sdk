# CaseClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseClass']
**case_class_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_class import CaseClass

# TODO update the JSON string below
json = "{}"
# create an instance of CaseClass from a JSON string
case_class_instance = CaseClass.from_json(json)
# print the JSON string representation of the object
print(CaseClass.to_json())

# convert the object into a dict
case_class_dict = case_class_instance.to_dict()
# create an instance of CaseClass from a dict
case_class_from_dict = CaseClass.from_dict(case_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


