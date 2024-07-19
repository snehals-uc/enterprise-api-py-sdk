# CaseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseStatus']
**case_status_id** | **str** |  | 
**case_status_group_id** | **str** |  | 
**case_status_group** | **str** |  | 
**name** | **str** |  | 
**case_class_array** | **List[str]** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_status import CaseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CaseStatus from a JSON string
case_status_instance = CaseStatus.from_json(json)
# print the JSON string representation of the object
print(CaseStatus.to_json())

# convert the object into a dict
case_status_dict = case_status_instance.to_dict()
# create an instance of CaseStatus from a dict
case_status_from_dict = CaseStatus.from_dict(case_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


