# SOSData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'SOSData']
**sos_number** | **str** |  | 
**state_code** | **str** |  | 
**fein** | **str** |  | 
**domestic_registration** | **bool** |  | [default to True]
**registered_date** | **datetime** |  | 
**status** | **str** |  | 
**is_active** | **bool** |  | [default to True]
**inactivation_date** | **datetime** |  | 
**associated_so_s_person_array** | [**List[AssociatedSoSPerson]**](AssociatedSoSPerson.md) |  | 
**contact** | [**Contact**](Contact.md) |  | 
**name_changes_array** | [**List[SOSNameChange]**](SOSNameChange.md) |  | 
**sos_associated_norm_organization_array** | [**List[SOSAssociatedNormOrganization]**](SOSAssociatedNormOrganization.md) |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**last_fetch_date_with_updates** | **datetime** | Last Fetch Date of Organization with Updates. | 

## Example

```python
from unicourt.models.sos_data import SOSData

# TODO update the JSON string below
json = "{}"
# create an instance of SOSData from a JSON string
sos_data_instance = SOSData.from_json(json)
# print the JSON string representation of the object
print(SOSData.to_json())

# convert the object into a dict
sos_data_dict = sos_data_instance.to_dict()
# create an instance of SOSData from a dict
sos_data_from_dict = SOSData.from_dict(sos_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


