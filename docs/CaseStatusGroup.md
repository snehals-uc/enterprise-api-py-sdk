# CaseStatusGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseStatusGroup']
**case_status_group_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_status_group import CaseStatusGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CaseStatusGroup from a JSON string
case_status_group_instance = CaseStatusGroup.from_json(json)
# print the JSON string representation of the object
print(CaseStatusGroup.to_json())

# convert the object into a dict
case_status_group_dict = case_status_group_instance.to_dict()
# create an instance of CaseStatusGroup from a dict
case_status_group_from_dict = CaseStatusGroup.from_dict(case_status_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


