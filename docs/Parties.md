# Parties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Parties']
**page_number** | **int** | Page number for which results where obtained. | 
**party_array** | [**List[Party]**](Party.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.parties import Parties

# TODO update the JSON string below
json = "{}"
# create an instance of Parties from a JSON string
parties_instance = Parties.from_json(json)
# print the JSON string representation of the object
print(Parties.to_json())

# convert the object into a dict
parties_dict = parties_instance.to_dict()
# create an instance of Parties from a dict
parties_from_dict = Parties.from_dict(parties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


