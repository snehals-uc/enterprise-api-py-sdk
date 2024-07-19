# BillingCyclesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'BillingCyclesResponse']
**billing_cycle_array** | **List[Optional[str]]** | Array of previous 12 Billing Cycles. | 

## Example

```python
from unicourt.models.billing_cycles_response import BillingCyclesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCyclesResponse from a JSON string
billing_cycles_response_instance = BillingCyclesResponse.from_json(json)
# print the JSON string representation of the object
print(BillingCyclesResponse.to_json())

# convert the object into a dict
billing_cycles_response_dict = billing_cycles_response_instance.to_dict()
# create an instance of BillingCyclesResponse from a dict
billing_cycles_response_from_dict = BillingCyclesResponse.from_dict(billing_cycles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


