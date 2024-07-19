# NormAttorneySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormAttorneySearchResponse']
**norm_attorney_search_result_array** | [**List[NormAttorneySearchResult]**](NormAttorneySearchResult.md) |  | 
**q** | **str** | Query been sent by client | 
**norm_attorney_search_id** | **str** | Query been sent by client | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** |  | 
**total_pages** | **int** | Total pages for matches that were found in the index. | 
**total_count** | **int** | The number of matches that were found in the index. | 

## Example

```python
from unicourt.models.norm_attorney_search_response import NormAttorneySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NormAttorneySearchResponse from a JSON string
norm_attorney_search_response_instance = NormAttorneySearchResponse.from_json(json)
# print the JSON string representation of the object
print(NormAttorneySearchResponse.to_json())

# convert the object into a dict
norm_attorney_search_response_dict = norm_attorney_search_response_instance.to_dict()
# create an instance of NormAttorneySearchResponse from a dict
norm_attorney_search_response_from_dict = NormAttorneySearchResponse.from_dict(norm_attorney_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


