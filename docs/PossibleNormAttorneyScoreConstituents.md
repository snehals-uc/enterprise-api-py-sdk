# PossibleNormAttorneyScoreConstituents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_similarity_score** | **float** |  | 
**other_potential_norm_attorneys** | **int** |  | 
**bar_id** | **str** |  | 
**address** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**law_firm** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_attorney_score_constituents import PossibleNormAttorneyScoreConstituents

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormAttorneyScoreConstituents from a JSON string
possible_norm_attorney_score_constituents_instance = PossibleNormAttorneyScoreConstituents.from_json(json)
# print the JSON string representation of the object
print(PossibleNormAttorneyScoreConstituents.to_json())

# convert the object into a dict
possible_norm_attorney_score_constituents_dict = possible_norm_attorney_score_constituents_instance.to_dict()
# create an instance of PossibleNormAttorneyScoreConstituents from a dict
possible_norm_attorney_score_constituents_from_dict = PossibleNormAttorneyScoreConstituents.from_dict(possible_norm_attorney_score_constituents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


