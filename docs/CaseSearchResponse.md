# CaseSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseSearchResponse']
**case_search_result_array** | [**List[CaseSearchResult]**](CaseSearchResult.md) |  | 
**q** | **str** | Query been sent by client | 
**case_search_id** | **str** | Query been sent by client | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** |  | 
**total_pages** | **int** | Total pages for matches that were found in the index. | 
**total_count** | **int** | The number of matches that were found in the index. | 

## Example

```python
from unicourt.models.case_search_response import CaseSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseSearchResponse from a JSON string
case_search_response_instance = CaseSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CaseSearchResponse.to_json())

# convert the object into a dict
case_search_response_dict = case_search_response_instance.to_dict()
# create an instance of CaseSearchResponse from a dict
case_search_response_from_dict = CaseSearchResponse.from_dict(case_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


