# PartyRoleGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'PartyRoleGroup']
**party_role_group_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.party_role_group import PartyRoleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PartyRoleGroup from a JSON string
party_role_group_instance = PartyRoleGroup.from_json(json)
# print the JSON string representation of the object
print(PartyRoleGroup.to_json())

# convert the object into a dict
party_role_group_dict = party_role_group_instance.to_dict()
# create an instance of PartyRoleGroup from a dict
party_role_group_from_dict = PartyRoleGroup.from_dict(party_role_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


