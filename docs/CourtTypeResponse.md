# CourtTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtTypeResponse']
**court_type_array** | [**List[CourtType]**](CourtType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.court_type_response import CourtTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourtTypeResponse from a JSON string
court_type_response_instance = CourtTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CourtTypeResponse.to_json())

# convert the object into a dict
court_type_response_dict = court_type_response_instance.to_dict()
# create an instance of CourtTypeResponse from a dict
court_type_response_from_dict = CourtTypeResponse.from_dict(court_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


