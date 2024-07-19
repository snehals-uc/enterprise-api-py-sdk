# AssociatedNormJudgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_norm_judge_array** | [**List[AssociatedNormJudge]**](AssociatedNormJudge.md) |  | 
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Previous page of results if applicable. | 
**total_pages** | **int** | Total no. of pages. | 
**total_count** | **int** | Total no. of results for this criteria. | 

## Example

```python
from unicourt.models.associated_norm_judge_response import AssociatedNormJudgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormJudgeResponse from a JSON string
associated_norm_judge_response_instance = AssociatedNormJudgeResponse.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormJudgeResponse.to_json())

# convert the object into a dict
associated_norm_judge_response_dict = associated_norm_judge_response_instance.to_dict()
# create an instance of AssociatedNormJudgeResponse from a dict
associated_norm_judge_response_from_dict = AssociatedNormJudgeResponse.from_dict(associated_norm_judge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


