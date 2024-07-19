# PossibleNormParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PossibleNormParty']
**norm_party_id** | **str** |  | 
**norm_party_name** | **str** |  | 
**best_match** | **bool** |  | [default to False]
**confidence_score** | **float** |  | 
**score_constituents** | [**PossibleNormPartyScoreConstituents**](PossibleNormPartyScoreConstituents.md) |  | 
**norm_party_api** | **str** | Link to Details For the Party. | 
**associated_norm_attorneys_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_judges_api** | **str** |  | 
**case_count_analytics_by_norm_party_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_party_api** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_party import PossibleNormParty

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormParty from a JSON string
possible_norm_party_instance = PossibleNormParty.from_json(json)
# print the JSON string representation of the object
print(PossibleNormParty.to_json())

# convert the object into a dict
possible_norm_party_dict = possible_norm_party_instance.to_dict()
# create an instance of PossibleNormParty from a dict
possible_norm_party_from_dict = PossibleNormParty.from_dict(possible_norm_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


