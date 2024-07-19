# CourtSystemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtSystemResponse']
**court_system_array** | [**List[CourtSystem]**](CourtSystem.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.court_system_response import CourtSystemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourtSystemResponse from a JSON string
court_system_response_instance = CourtSystemResponse.from_json(json)
# print the JSON string representation of the object
print(CourtSystemResponse.to_json())

# convert the object into a dict
court_system_response_dict = court_system_response_instance.to_dict()
# create an instance of CourtSystemResponse from a dict
court_system_response_from_dict = CourtSystemResponse.from_dict(court_system_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


