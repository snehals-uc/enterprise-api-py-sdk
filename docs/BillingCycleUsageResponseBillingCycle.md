# BillingCycleUsageResponseBillingCycle

StartDate and endDate of the billing cycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start date of the billing cycle. | 
**end_date** | **datetime** | End date of the billing cycle. | 

## Example

```python
from unicourt.models.billing_cycle_usage_response_billing_cycle import BillingCycleUsageResponseBillingCycle

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleUsageResponseBillingCycle from a JSON string
billing_cycle_usage_response_billing_cycle_instance = BillingCycleUsageResponseBillingCycle.from_json(json)
# print the JSON string representation of the object
print(BillingCycleUsageResponseBillingCycle.to_json())

# convert the object into a dict
billing_cycle_usage_response_billing_cycle_dict = billing_cycle_usage_response_billing_cycle_instance.to_dict()
# create an instance of BillingCycleUsageResponseBillingCycle from a dict
billing_cycle_usage_response_billing_cycle_from_dict = BillingCycleUsageResponseBillingCycle.from_dict(billing_cycle_usage_response_billing_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


