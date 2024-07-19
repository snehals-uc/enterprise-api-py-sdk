# CourtLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtLocationResponse']
**court_location_array** | [**List[CourtLocation]**](CourtLocation.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.court_location_response import CourtLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourtLocationResponse from a JSON string
court_location_response_instance = CourtLocationResponse.from_json(json)
# print the JSON string representation of the object
print(CourtLocationResponse.to_json())

# convert the object into a dict
court_location_response_dict = court_location_response_instance.to_dict()
# create an instance of CourtLocationResponse from a dict
court_location_response_from_dict = CourtLocationResponse.from_dict(court_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


