# SourceChargeAdditionalData

Additional data that enchances the information of a given charge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'SourceChargeAdditionalData']
**type** | **str** | Describes what type of additional data. | 
**value** | **str** | Value of additional data. | 

## Example

```python
from unicourt.models.source_charge_additional_data import SourceChargeAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of SourceChargeAdditionalData from a JSON string
source_charge_additional_data_instance = SourceChargeAdditionalData.from_json(json)
# print the JSON string representation of the object
print(SourceChargeAdditionalData.to_json())

# convert the object into a dict
source_charge_additional_data_dict = source_charge_additional_data_instance.to_dict()
# create an instance of SourceChargeAdditionalData from a dict
source_charge_additional_data_from_dict = SourceChargeAdditionalData.from_dict(source_charge_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


