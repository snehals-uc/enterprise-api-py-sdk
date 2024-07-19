# ReferencedDocketNumber

Object consisiting of each docket entry number and its corresponding API call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'ReferencedDocketNumber']
**docket_number** | **int** | Each referenced docket number | 
**docket_entries_api** | **str** | Link to Docket Entries API with the current docket number. The response of this API will give all the primary documents and secondary documents that are associated to it. | 

## Example

```python
from unicourt.models.referenced_docket_number import ReferencedDocketNumber

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedDocketNumber from a JSON string
referenced_docket_number_instance = ReferencedDocketNumber.from_json(json)
# print the JSON string representation of the object
print(ReferencedDocketNumber.to_json())

# convert the object into a dict
referenced_docket_number_dict = referenced_docket_number_instance.to_dict()
# create an instance of ReferencedDocketNumber from a dict
referenced_docket_number_from_dict = ReferencedDocketNumber.from_dict(referenced_docket_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


