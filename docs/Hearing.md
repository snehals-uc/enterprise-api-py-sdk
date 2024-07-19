# Hearing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Hearing']
**hearing_date** | **datetime** | Hearing Date | 
**hearing_description** | **str** | Source Hearing Description Text | 
**hearing_structured** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**location** | **str** | Location where the hearing will takeplace. | 
**first_fetch_date** | **str** | When this hearing was first fetched from the source. | 
**last_fetch_date** | **str** | When this hearing was last fetched from the source. | 

## Example

```python
from unicourt.models.hearing import Hearing

# TODO update the JSON string below
json = "{}"
# create an instance of Hearing from a JSON string
hearing_instance = Hearing.from_json(json)
# print the JSON string representation of the object
print(Hearing.to_json())

# convert the object into a dict
hearing_dict = hearing_instance.to_dict()
# create an instance of Hearing from a dict
hearing_from_dict = Hearing.from_dict(hearing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


