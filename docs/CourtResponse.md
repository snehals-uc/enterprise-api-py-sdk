# CourtResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CourtResponse']
**court_array** | [**List[Court]**](Court.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** |  | 
**total_pages** | **int** | Total pages for matches that were found in the index. | 
**total_count** | **int** | The number of matches that were found in the index. | 

## Example

```python
from unicourt.models.court_response import CourtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourtResponse from a JSON string
court_response_instance = CourtResponse.from_json(json)
# print the JSON string representation of the object
print(CourtResponse.to_json())

# convert the object into a dict
court_response_dict = court_response_instance.to_dict()
# create an instance of CourtResponse from a dict
court_response_from_dict = CourtResponse.from_dict(court_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


