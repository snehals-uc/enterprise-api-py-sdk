# AttorneyRepresentationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AttorneyRepresentationType']
**attorney_representation_type_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.attorney_representation_type import AttorneyRepresentationType

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyRepresentationType from a JSON string
attorney_representation_type_instance = AttorneyRepresentationType.from_json(json)
# print the JSON string representation of the object
print(AttorneyRepresentationType.to_json())

# convert the object into a dict
attorney_representation_type_dict = attorney_representation_type_instance.to_dict()
# create an instance of AttorneyRepresentationType from a dict
attorney_representation_type_from_dict = AttorneyRepresentationType.from_dict(attorney_representation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


