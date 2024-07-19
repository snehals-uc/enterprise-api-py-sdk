# AttorneyRepresentationTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AttorneyRepresentationTypeResponse']
**attorney_representation_type_array** | [**List[AttorneyRepresentationType]**](AttorneyRepresentationType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.attorney_representation_type_response import AttorneyRepresentationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyRepresentationTypeResponse from a JSON string
attorney_representation_type_response_instance = AttorneyRepresentationTypeResponse.from_json(json)
# print the JSON string representation of the object
print(AttorneyRepresentationTypeResponse.to_json())

# convert the object into a dict
attorney_representation_type_response_dict = attorney_representation_type_response_instance.to_dict()
# create an instance of AttorneyRepresentationTypeResponse from a dict
attorney_representation_type_response_from_dict = AttorneyRepresentationTypeResponse.from_dict(attorney_representation_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


