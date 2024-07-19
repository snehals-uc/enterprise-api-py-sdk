# SourceCharge

Source charge data from the source site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'SourceCharge']
**source_charge_raw** | **str** | Raw charge data from the source site. | 
**source_charge** | **str** | Charge data from the source site. | 
**is_visible** | **bool** | Signifies if the charge is currently isVisible or not for the case. | 
**source_statute** | **str** | Statute of a charge. | 
**source_charge_degree** | **str** | Charge degree data from the source site. | 
**source_charge_severity** | **str** | Charge severity data from the source site. | 
**source_charge_additional_data_array** | [**List[SourceChargeAdditionalData]**](SourceChargeAdditionalData.md) | Additional data related to the charge which is available in the source site. | 
**first_fetch_date** | **str** | When this charge was first fetched from the court site. | 
**last_fetch_date** | **str** | When this charge was last fetched from the court site. | 

## Example

```python
from unicourt.models.source_charge import SourceCharge

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCharge from a JSON string
source_charge_instance = SourceCharge.from_json(json)
# print the JSON string representation of the object
print(SourceCharge.to_json())

# convert the object into a dict
source_charge_dict = source_charge_instance.to_dict()
# create an instance of SourceCharge from a dict
source_charge_from_dict = SourceCharge.from_dict(source_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


