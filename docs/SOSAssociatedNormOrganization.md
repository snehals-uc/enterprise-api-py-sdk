# SOSAssociatedNormOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'SOSAssociatedNormOrganization']
**norm_organization_id** | **str** |  | 
**norm_organization_api** | **str** |  | 
**relationship_type** | **str** |  | 
**name** | **str** |  | 
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 

## Example

```python
from unicourt.models.sos_associated_norm_organization import SOSAssociatedNormOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of SOSAssociatedNormOrganization from a JSON string
sos_associated_norm_organization_instance = SOSAssociatedNormOrganization.from_json(json)
# print the JSON string representation of the object
print(SOSAssociatedNormOrganization.to_json())

# convert the object into a dict
sos_associated_norm_organization_dict = sos_associated_norm_organization_instance.to_dict()
# create an instance of SOSAssociatedNormOrganization from a dict
sos_associated_norm_organization_from_dict = SOSAssociatedNormOrganization.from_dict(sos_associated_norm_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


