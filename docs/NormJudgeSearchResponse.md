# NormJudgeSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormJudgeSearchResponse']
**norm_judge_search_result_array** | [**List[NormJudgeSearchResult]**](NormJudgeSearchResult.md) |  | 
**q** | **str** | Query been sent by client | 
**norm_judge_search_id** | **str** | Query been sent by client | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** |  | 
**total_pages** | **int** | Total pages for matches that were found in the index. | 
**total_count** | **int** | The number of matches that were found in the index. | 

## Example

```python
from unicourt.models.norm_judge_search_response import NormJudgeSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgeSearchResponse from a JSON string
norm_judge_search_response_instance = NormJudgeSearchResponse.from_json(json)
# print the JSON string representation of the object
print(NormJudgeSearchResponse.to_json())

# convert the object into a dict
norm_judge_search_response_dict = norm_judge_search_response_instance.to_dict()
# create an instance of NormJudgeSearchResponse from a dict
norm_judge_search_response_from_dict = NormJudgeSearchResponse.from_dict(norm_judge_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


