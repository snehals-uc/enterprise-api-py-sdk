# CaseCountAnalyticsByNormJudgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormJudgeResponse']
**results** | [**List[CaseCountAnalyticsByNormJudge]**](CaseCountAnalyticsByNormJudge.md) |  | 
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_norm_judge_count** | **int** | Total no. of NormJudge for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_judge_response import CaseCountAnalyticsByNormJudgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormJudgeResponse from a JSON string
case_count_analytics_by_norm_judge_response_instance = CaseCountAnalyticsByNormJudgeResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormJudgeResponse.to_json())

# convert the object into a dict
case_count_analytics_by_norm_judge_response_dict = case_count_analytics_by_norm_judge_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormJudgeResponse from a dict
case_count_analytics_by_norm_judge_response_from_dict = CaseCountAnalyticsByNormJudgeResponse.from_dict(case_count_analytics_by_norm_judge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


