# CourtServiceStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtServiceStatusResponse']
**court_service_status_array** | [**List[CourtServiceStatus]**](CourtServiceStatus.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.court_service_status_response import CourtServiceStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourtServiceStatusResponse from a JSON string
court_service_status_response_instance = CourtServiceStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CourtServiceStatusResponse.to_json())

# convert the object into a dict
court_service_status_response_dict = court_service_status_response_instance.to_dict()
# create an instance of CourtServiceStatusResponse from a dict
court_service_status_response_from_dict = CourtServiceStatusResponse.from_dict(court_service_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


