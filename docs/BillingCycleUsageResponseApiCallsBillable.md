# BillingCycleUsageResponseApiCallsBillable

Total number of API calls billed for the billing cycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total API calls billed  for the billing cycle | 
**last_updated** | **datetime** | Last Updated date and time for the field apiCallsBillable | 

## Example

```python
from unicourt.models.billing_cycle_usage_response_api_calls_billable import BillingCycleUsageResponseApiCallsBillable

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleUsageResponseApiCallsBillable from a JSON string
billing_cycle_usage_response_api_calls_billable_instance = BillingCycleUsageResponseApiCallsBillable.from_json(json)
# print the JSON string representation of the object
print(BillingCycleUsageResponseApiCallsBillable.to_json())

# convert the object into a dict
billing_cycle_usage_response_api_calls_billable_dict = billing_cycle_usage_response_api_calls_billable_instance.to_dict()
# create an instance of BillingCycleUsageResponseApiCallsBillable from a dict
billing_cycle_usage_response_api_calls_billable_from_dict = BillingCycleUsageResponseApiCallsBillable.from_dict(billing_cycle_usage_response_api_calls_billable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


