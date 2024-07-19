# NormLawFirm

Schema for Norm Law Firm containing Organization sub-field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormLawFirm']
**norm_law_firm_id** | **str** |  | 
**name** | **str** |  | 
**case_search_api** | **str** |  | 
**case_analytics_api** | [**CaseAnalyticsAPI**](CaseAnalyticsAPI.md) |  | 
**norm_organization_data** | [**NormOrganization**](NormOrganization.md) |  | 
**law_firm_analytics_api** | [**LawFirmAnalyticsAPI**](LawFirmAnalyticsAPI.md) |  | 

## Example

```python
from unicourt.models.norm_law_firm import NormLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of NormLawFirm from a JSON string
norm_law_firm_instance = NormLawFirm.from_json(json)
# print the JSON string representation of the object
print(NormLawFirm.to_json())

# convert the object into a dict
norm_law_firm_dict = norm_law_firm_instance.to_dict()
# create an instance of NormLawFirm from a dict
norm_law_firm_from_dict = NormLawFirm.from_dict(norm_law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


