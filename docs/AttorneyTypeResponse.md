# AttorneyTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AttorneyTypeResponse']
**attorney_type_array** | [**List[AttorneyType]**](AttorneyType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.attorney_type_response import AttorneyTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyTypeResponse from a JSON string
attorney_type_response_instance = AttorneyTypeResponse.from_json(json)
# print the JSON string representation of the object
print(AttorneyTypeResponse.to_json())

# convert the object into a dict
attorney_type_response_dict = attorney_type_response_instance.to_dict()
# create an instance of AttorneyTypeResponse from a dict
attorney_type_response_from_dict = AttorneyTypeResponse.from_dict(attorney_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


