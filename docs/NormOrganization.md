# NormOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormOrganization']
**norm_organization_id** | **str** |  | 
**name** | **str** |  | 
**organization_type** | **str** |  | 
**lei** | **str** |  | 
**cik** | **str** |  | 
**ticker_array** | [**List[NormOrganizationTickerArrayInner]**](NormOrganizationTickerArrayInner.md) |  | 
**naics** | **str** |  | 
**naics_description** | **str** |  | 
**sic** | **str** |  | 
**sic_description** | **str** |  | 
**is_involved_in_litigation** | **bool** |  | 
**norm_party_api** | **str** |  | 
**norm_corporate_group_array** | [**List[NormCorporateGroup]**](NormCorporateGroup.md) |  | 
**sos_data_array** | [**List[SOSData]**](SOSData.md) |  | 

## Example

```python
from unicourt.models.norm_organization import NormOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of NormOrganization from a JSON string
norm_organization_instance = NormOrganization.from_json(json)
# print the JSON string representation of the object
print(NormOrganization.to_json())

# convert the object into a dict
norm_organization_dict = norm_organization_instance.to_dict()
# create an instance of NormOrganization from a dict
norm_organization_from_dict = NormOrganization.from_dict(norm_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


