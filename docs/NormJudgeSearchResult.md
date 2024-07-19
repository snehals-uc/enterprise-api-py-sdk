# NormJudgeSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormJudgeSearchResult']
**norm_judge_id** | **str** |  | 
**name** | **str** |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**norm_judge_details_api** | **str** |  | 
**matched_object_array** | [**List[MatchedObject]**](MatchedObject.md) |  | 

## Example

```python
from unicourt.models.norm_judge_search_result import NormJudgeSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgeSearchResult from a JSON string
norm_judge_search_result_instance = NormJudgeSearchResult.from_json(json)
# print the JSON string representation of the object
print(NormJudgeSearchResult.to_json())

# convert the object into a dict
norm_judge_search_result_dict = norm_judge_search_result_instance.to_dict()
# create an instance of NormJudgeSearchResult from a dict
norm_judge_search_result_from_dict = NormJudgeSearchResult.from_dict(norm_judge_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


