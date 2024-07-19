# NatureOfSuit

Nature Of Suit for a case.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'NatureOfSuit']
**source_text** | **str** | Source nos code data from the court site. | 
**code** | **int** | Nos Code from the source site which is extracted from the sourceText. | 
**name** | **str** | Code Name from the source site which is extracted from the sourceText. | 
**section** | **str** | Section of a nos code extracted from the sourceText. | 

## Example

```python
from unicourt.models.nature_of_suit import NatureOfSuit

# TODO update the JSON string below
json = "{}"
# create an instance of NatureOfSuit from a JSON string
nature_of_suit_instance = NatureOfSuit.from_json(json)
# print the JSON string representation of the object
print(NatureOfSuit.to_json())

# convert the object into a dict
nature_of_suit_dict = nature_of_suit_instance.to_dict()
# create an instance of NatureOfSuit from a dict
nature_of_suit_from_dict = NatureOfSuit.from_dict(nature_of_suit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


