# PartyAttorneyAssociations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PartyAttorneyAssociations']
**page_number** | **int** | Page number for which results where obtained. | 
**party_attorney_association_array** | [**List[PartyAttorneyAssociation]**](PartyAttorneyAssociation.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.party_attorney_associations import PartyAttorneyAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PartyAttorneyAssociations from a JSON string
party_attorney_associations_instance = PartyAttorneyAssociations.from_json(json)
# print the JSON string representation of the object
print(PartyAttorneyAssociations.to_json())

# convert the object into a dict
party_attorney_associations_dict = party_attorney_associations_instance.to_dict()
# create an instance of PartyAttorneyAssociations from a dict
party_attorney_associations_from_dict = PartyAttorneyAssociations.from_dict(party_attorney_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


