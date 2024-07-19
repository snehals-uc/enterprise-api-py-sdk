# CaseCountAnalyticsByNormJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormJudge']
**norm_judge_id** | **str** |  | 
**norm_judge_name** | **str** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**case_count** | **int** |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_judge import CaseCountAnalyticsByNormJudge

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormJudge from a JSON string
case_count_analytics_by_norm_judge_instance = CaseCountAnalyticsByNormJudge.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormJudge.to_json())

# convert the object into a dict
case_count_analytics_by_norm_judge_dict = case_count_analytics_by_norm_judge_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormJudge from a dict
case_count_analytics_by_norm_judge_from_dict = CaseCountAnalyticsByNormJudge.from_dict(case_count_analytics_by_norm_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


