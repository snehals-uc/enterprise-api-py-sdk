# NormParty

Norm Party

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormParty']
**norm_party_id** | **str** |  | 
**name** | **str** |  | 
**party_classification_type** | **str** |  | 
**case_search_api** | **str** |  | 
**case_analytics_api** | [**CaseAnalyticsAPI**](CaseAnalyticsAPI.md) |  | 
**individual_data** | [**Individual**](Individual.md) |  | 
**norm_organization_data** | [**NormOrganization**](NormOrganization.md) |  | 
**party_analytics_api** | [**PartyAnalyticsAPI**](PartyAnalyticsAPI.md) |  | 
**related_norm_party_array** | [**List[RelatedNormParty]**](RelatedNormParty.md) |  | 

## Example

```python
from unicourt.models.norm_party import NormParty

# TODO update the JSON string below
json = "{}"
# create an instance of NormParty from a JSON string
norm_party_instance = NormParty.from_json(json)
# print the JSON string representation of the object
print(NormParty.to_json())

# convert the object into a dict
norm_party_dict = norm_party_instance.to_dict()
# create an instance of NormParty from a dict
norm_party_from_dict = NormParty.from_dict(norm_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


