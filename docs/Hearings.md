# Hearings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Hearings']
**page_number** | **int** | Page number for which results where obtained. | 
**hearing_array** | [**List[Hearing]**](Hearing.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.hearings import Hearings

# TODO update the JSON string below
json = "{}"
# create an instance of Hearings from a JSON string
hearings_instance = Hearings.from_json(json)
# print the JSON string representation of the object
print(Hearings.to_json())

# convert the object into a dict
hearings_dict = hearings_instance.to_dict()
# create an instance of Hearings from a dict
hearings_from_dict = Hearings.from_dict(hearings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


