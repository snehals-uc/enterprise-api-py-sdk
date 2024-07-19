# NormAttorney

Norm Attorney

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormAttorney']
**norm_attorney_id** | **str** |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**case_search_api** | **str** |  | 
**case_analytics_api** | [**CaseAnalyticsAPI**](CaseAnalyticsAPI.md) |  | 
**has_associated_public_data** | **bool** |  | 
**bar_record_array** | [**List[BarRecord]**](BarRecord.md) |  | 
**attorney_analytics_api** | [**AttorneyAnalyticsAPI**](AttorneyAnalyticsAPI.md) |  | 
**similar_norm_attorney_array** | [**List[SimilarNormAttorney]**](SimilarNormAttorney.md) |  | 

## Example

```python
from unicourt.models.norm_attorney import NormAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of NormAttorney from a JSON string
norm_attorney_instance = NormAttorney.from_json(json)
# print the JSON string representation of the object
print(NormAttorney.to_json())

# convert the object into a dict
norm_attorney_dict = norm_attorney_instance.to_dict()
# create an instance of NormAttorney from a dict
norm_attorney_from_dict = NormAttorney.from_dict(norm_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


