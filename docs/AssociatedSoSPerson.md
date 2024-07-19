# AssociatedSoSPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AssociatedSoSPerson']
**contact** | [**Contact**](Contact.md) |  | 
**entity_name** | **str** |  | 
**entity_type** | **str** |  | 

## Example

```python
from unicourt.models.associated_so_s_person import AssociatedSoSPerson

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedSoSPerson from a JSON string
associated_so_s_person_instance = AssociatedSoSPerson.from_json(json)
# print the JSON string representation of the object
print(AssociatedSoSPerson.to_json())

# convert the object into a dict
associated_so_s_person_dict = associated_so_s_person_instance.to_dict()
# create an instance of AssociatedSoSPerson from a dict
associated_so_s_person_from_dict = AssociatedSoSPerson.from_dict(associated_so_s_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


