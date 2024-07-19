# CaseType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseType']
**case_type_id** | **str** |  | 
**case_class_id** | **str** |  | 
**area_of_law_id** | **str** |  | 
**case_type_group_id** | **str** |  | 
**case_class** | **str** |  | 
**area_of_law** | **str** |  | 
**case_type_group** | **str** |  | 
**name** | **str** |  | 
**sali_code** | **str** |  | 
**case_type_tag** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_type import CaseType

# TODO update the JSON string below
json = "{}"
# create an instance of CaseType from a JSON string
case_type_instance = CaseType.from_json(json)
# print the JSON string representation of the object
print(CaseType.to_json())

# convert the object into a dict
case_type_dict = case_type_instance.to_dict()
# create an instance of CaseType from a dict
case_type_from_dict = CaseType.from_dict(case_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


