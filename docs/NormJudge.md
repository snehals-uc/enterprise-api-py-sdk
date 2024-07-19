# NormJudge

Norm Judge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormJudge']
**norm_judge_id** | **str** |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**case_search_api** | **str** |  | 
**case_analytics_api** | [**CaseAnalyticsAPI**](CaseAnalyticsAPI.md) |  | 
**has_associated_public_data** | **bool** |  | 
**judicial_data_array** | [**List[NormJudgePublicData]**](NormJudgePublicData.md) |  | 
**judge_analytics_api** | [**JudgeAnalyticsAPI**](JudgeAnalyticsAPI.md) |  | 

## Example

```python
from unicourt.models.norm_judge import NormJudge

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudge from a JSON string
norm_judge_instance = NormJudge.from_json(json)
# print the JSON string representation of the object
print(NormJudge.to_json())

# convert the object into a dict
norm_judge_dict = norm_judge_instance.to_dict()
# create an instance of NormJudge from a dict
norm_judge_from_dict = NormJudge.from_dict(norm_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


