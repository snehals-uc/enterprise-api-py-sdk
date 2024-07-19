# PossibleNormJudgeScoreConstituents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_similarity_score** | **float** |  | 
**other_potential_norm_judges** | **int** |  | 
**address** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_judge_score_constituents import PossibleNormJudgeScoreConstituents

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormJudgeScoreConstituents from a JSON string
possible_norm_judge_score_constituents_instance = PossibleNormJudgeScoreConstituents.from_json(json)
# print the JSON string representation of the object
print(PossibleNormJudgeScoreConstituents.to_json())

# convert the object into a dict
possible_norm_judge_score_constituents_dict = possible_norm_judge_score_constituents_instance.to_dict()
# create an instance of PossibleNormJudgeScoreConstituents from a dict
possible_norm_judge_score_constituents_from_dict = PossibleNormJudgeScoreConstituents.from_dict(possible_norm_judge_score_constituents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


