# PossibleNormJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PossibleNormJudge']
**norm_judge_id** | **str** |  | 
**norm_judge_name** | **str** |  | 
**best_match** | **bool** |  | [default to False]
**confidence_score** | **float** |  | 
**score_constituents** | [**PossibleNormJudgeScoreConstituents**](PossibleNormJudgeScoreConstituents.md) |  | 
**norm_judge_api** | **str** | Link to Details For the Judge. | 
**associated_norm_attorneys_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 
**case_count_analytics_by_norm_judge_api** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_judge import PossibleNormJudge

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormJudge from a JSON string
possible_norm_judge_instance = PossibleNormJudge.from_json(json)
# print the JSON string representation of the object
print(PossibleNormJudge.to_json())

# convert the object into a dict
possible_norm_judge_dict = possible_norm_judge_instance.to_dict()
# create an instance of PossibleNormJudge from a dict
possible_norm_judge_from_dict = PossibleNormJudge.from_dict(possible_norm_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


