# CaseTypeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseTypeGroup']
**case_type_group_id** | **str** |  | 
**case_class_id** | **str** |  | 
**area_of_law_id** | **str** |  | 
**case_class** | **str** |  | 
**area_of_law** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_type_group import CaseTypeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTypeGroup from a JSON string
case_type_group_instance = CaseTypeGroup.from_json(json)
# print the JSON string representation of the object
print(CaseTypeGroup.to_json())

# convert the object into a dict
case_type_group_dict = case_type_group_instance.to_dict()
# create an instance of CaseTypeGroup from a dict
case_type_group_from_dict = CaseTypeGroup.from_dict(case_type_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


