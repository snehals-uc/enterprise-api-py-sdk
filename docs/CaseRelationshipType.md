# CaseRelationshipType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseRelationshipType']
**case_relationship_type_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.case_relationship_type import CaseRelationshipType

# TODO update the JSON string below
json = "{}"
# create an instance of CaseRelationshipType from a JSON string
case_relationship_type_instance = CaseRelationshipType.from_json(json)
# print the JSON string representation of the object
print(CaseRelationshipType.to_json())

# convert the object into a dict
case_relationship_type_dict = case_relationship_type_instance.to_dict()
# create an instance of CaseRelationshipType from a dict
case_relationship_type_from_dict = CaseRelationshipType.from_dict(case_relationship_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


