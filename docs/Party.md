# Party


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Party']
**party_id** | **str** | ID for the party in this case. This ID is unique within a case and NOT across cases. If the same party were to appear in another case this ID would be different. | 
**name** | **str** | Name of the party as provided by Court. | 
**name_prefix** | **str** |  | 
**first_name** | **str** | First name of the party. This is normalized by UniCourt. | 
**middle_name** | **str** | Middle name of the party. This is normalized by UniCourt. | 
**last_name** | **str** | Last name of the party. This is normalized by UniCourt. | 
**name_suffix** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**party_classification_type** | **str** | To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved. | 
**party_role** | [**PartyRole**](PartyRole.md) |  | 
**source_party_role** | **str** | Party Type as provided by Court. | 
**is_visible** | **bool** | Signifies if the party as this party type is currently isVisible or not for the case. | 
**first_fetch_date** | **datetime** | When was the party first fetched from the court site. | 
**last_fetch_date** | **datetime** | When was the party last fetched from the court site. | 
**attorney_representation_type** | [**AttorneyRepresentationType**](AttorneyRepresentationType.md) |  | 
**party_attorney_associations** | [**PartyAttorneyAssociations**](PartyAttorneyAssociations.md) |  | 
**possible_norm_party_array** | [**List[PossibleNormParty]**](PossibleNormParty.md) |  | 

## Example

```python
from unicourt.models.party import Party

# TODO update the JSON string below
json = "{}"
# create an instance of Party from a JSON string
party_instance = Party.from_json(json)
# print the JSON string representation of the object
print(Party.to_json())

# convert the object into a dict
party_dict = party_instance.to_dict()
# create an instance of Party from a dict
party_from_dict = Party.from_dict(party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


