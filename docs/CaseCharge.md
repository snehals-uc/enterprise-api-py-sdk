# CaseCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CaseCharge']
**charge** | [**Charge**](Charge.md) |  | 
**charge_degree** | [**ChargeDegree**](ChargeDegree.md) |  | 
**charge_severity** | [**ChargeSeverity**](ChargeSeverity.md) |  | 
**charge_additional_data_array** | [**List[ChargeAdditionalData]**](ChargeAdditionalData.md) |  | 

## Example

```python
from unicourt.models.case_charge import CaseCharge

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCharge from a JSON string
case_charge_instance = CaseCharge.from_json(json)
# print the JSON string representation of the object
print(CaseCharge.to_json())

# convert the object into a dict
case_charge_dict = case_charge_instance.to_dict()
# create an instance of CaseCharge from a dict
case_charge_from_dict = CaseCharge.from_dict(case_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


