# PossibleNormLawFirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PossibleNormLawFirm']
**norm_law_firm_id** | **str** |  | 
**norm_law_firm_name** | **str** |  | 
**best_match** | **bool** |  | [default to False]
**source_details** | [**PossibleNormLawFirmSourceDetails**](PossibleNormLawFirmSourceDetails.md) |  | 
**confidence_score** | **float** |  | 
**score_constituents** | [**PossibleNormLawFirmScoreConstituents**](PossibleNormLawFirmScoreConstituents.md) |  | 
**norm_law_firm_api** | **str** |  | 
**associated_norm_attorney_api** | **str** |  | 
**associated_norm_judge_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 
**case_count_analytics_by_norm_law_firm_api** | **str** |  | 
**case_count_analytics_by_opposing_norm_law_firm_api** | **str** |  | 

## Example

```python
from unicourt.models.possible_norm_law_firm import PossibleNormLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleNormLawFirm from a JSON string
possible_norm_law_firm_instance = PossibleNormLawFirm.from_json(json)
# print the JSON string representation of the object
print(PossibleNormLawFirm.to_json())

# convert the object into a dict
possible_norm_law_firm_dict = possible_norm_law_firm_instance.to_dict()
# create an instance of PossibleNormLawFirm from a dict
possible_norm_law_firm_from_dict = PossibleNormLawFirm.from_dict(possible_norm_law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


