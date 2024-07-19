# PartyRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'PartyRole']
**party_role_id** | **str** |  | 
**party_role_group_id** | **str** |  | 
**party_role_group** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.party_role import PartyRole

# TODO update the JSON string below
json = "{}"
# create an instance of PartyRole from a JSON string
party_role_instance = PartyRole.from_json(json)
# print the JSON string representation of the object
print(PartyRole.to_json())

# convert the object into a dict
party_role_dict = party_role_instance.to_dict()
# create an instance of PartyRole from a dict
party_role_from_dict = PartyRole.from_dict(party_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


