# PossibleNormAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PossibleNormAttorney']
**norm_attorney_id** | **str** |  | 
**norm_attorney_name** | **str** |  | 
**best_match** | **bool** |  | [default to False]
**confidence_score** | **float** |  | 
**score_constituents** | [**PossibleNormAttorneyScoreConstituents**](PossibleNormAttorneyScoreConstituents.md) |  | 
**norm_attorney_api** | **str** |  | 
**associated_norm_judges_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 
**case_count_analytics_by_norm_attorney_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_attorney_api** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_attorney import PossibleNormAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormAttorney from a JSON string
possible_norm_attorney_instance = PossibleNormAttorney.from_json(json)
# print the JSON string representation of the object
print(PossibleNormAttorney.to_json())

# convert the object into a dict
possible_norm_attorney_dict = possible_norm_attorney_instance.to_dict()
# create an instance of PossibleNormAttorney from a dict
possible_norm_attorney_from_dict = PossibleNormAttorney.from_dict(possible_norm_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


