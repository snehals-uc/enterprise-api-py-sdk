# Judges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Judges']
**page_number** | **int** | Page number for which results where obtained. | 
**judge_array** | [**List[Judge]**](Judge.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.judges import Judges

# TODO update the JSON string below
json = "{}"
# create an instance of Judges from a JSON string
judges_instance = Judges.from_json(json)
# print the JSON string representation of the object
print(Judges.to_json())

# convert the object into a dict
judges_dict = judges_instance.to_dict()
# create an instance of Judges from a dict
judges_from_dict = Judges.from_dict(judges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


