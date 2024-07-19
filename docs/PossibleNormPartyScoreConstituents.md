# PossibleNormPartyScoreConstituents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_similarity_score** | **float** |  | 
**other_potential_norm_parties** | **int** |  | 
**secretary_of_state_id** | **str** |  | 
**address** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_party_score_constituents import PossibleNormPartyScoreConstituents

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormPartyScoreConstituents from a JSON string
possible_norm_party_score_constituents_instance = PossibleNormPartyScoreConstituents.from_json(json)
# print the JSON string representation of the object
print(PossibleNormPartyScoreConstituents.to_json())

# convert the object into a dict
possible_norm_party_score_constituents_dict = possible_norm_party_score_constituents_instance.to_dict()
# create an instance of PossibleNormPartyScoreConstituents from a dict
possible_norm_party_score_constituents_from_dict = PossibleNormPartyScoreConstituents.from_dict(possible_norm_party_score_constituents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


