# BillingCycleUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'BillingCycleUsageResponse']
**billing_cycle** | [**BillingCycleUsageResponseBillingCycle**](BillingCycleUsageResponseBillingCycle.md) |  | 
**days** | **object** | Billing cycle days. | 
**api_usage** | **object** | Billing cycle apiUsage. | 
**api_calls_made** | [**BillingCycleUsageResponseApiCallsMade**](BillingCycleUsageResponseApiCallsMade.md) |  | 
**api_calls_credited** | [**BillingCycleUsageResponseApiCallsCredited**](BillingCycleUsageResponseApiCallsCredited.md) |  | 
**api_calls_billable** | [**BillingCycleUsageResponseApiCallsBillable**](BillingCycleUsageResponseApiCallsBillable.md) |  | 
**total_cases_tracked** | **int** | Total number of successful case tracks. | 

## Example

```python
from unicourt.models.billing_cycle_usage_response import BillingCycleUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleUsageResponse from a JSON string
billing_cycle_usage_response_instance = BillingCycleUsageResponse.from_json(json)
# print the JSON string representation of the object
print(BillingCycleUsageResponse.to_json())

# convert the object into a dict
billing_cycle_usage_response_dict = billing_cycle_usage_response_instance.to_dict()
# create an instance of BillingCycleUsageResponse from a dict
billing_cycle_usage_response_from_dict = BillingCycleUsageResponse.from_dict(billing_cycle_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


