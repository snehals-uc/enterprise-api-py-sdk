# PartyRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'PartyRoleResponse']
**party_role_array** | [**List[PartyRole]**](PartyRole.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.party_role_response import PartyRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartyRoleResponse from a JSON string
party_role_response_instance = PartyRoleResponse.from_json(json)
# print the JSON string representation of the object
print(PartyRoleResponse.to_json())

# convert the object into a dict
party_role_response_dict = party_role_response_instance.to_dict()
# create an instance of PartyRoleResponse from a dict
party_role_response_from_dict = PartyRoleResponse.from_dict(party_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


