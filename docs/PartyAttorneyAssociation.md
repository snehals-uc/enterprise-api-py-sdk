# PartyAttorneyAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PartyAttorneyAssociation']
**party_attorney_association_id** | **str** | ID of the association | 
**attorney_id** | **str** | ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**party_id** | **str** | ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**is_visible** | **bool** | Signifies if this party attorney relationship is currently isVisible or not for the case. | 

## Example

```python
from unicourt.models.party_attorney_association import PartyAttorneyAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of PartyAttorneyAssociation from a JSON string
party_attorney_association_instance = PartyAttorneyAssociation.from_json(json)
# print the JSON string representation of the object
print(PartyAttorneyAssociation.to_json())

# convert the object into a dict
party_attorney_association_dict = party_attorney_association_instance.to_dict()
# create an instance of PartyAttorneyAssociation from a dict
party_attorney_association_from_dict = PartyAttorneyAssociation.from_dict(party_attorney_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


