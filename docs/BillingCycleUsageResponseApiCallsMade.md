# BillingCycleUsageResponseApiCallsMade

Total API calls made for the billing cycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total API calls made for the billing cycle | 
**last_updated** | **datetime** | Last Updated date and time for the field apiCallsMade | 

## Example

```python
from unicourt.models.billing_cycle_usage_response_api_calls_made import BillingCycleUsageResponseApiCallsMade

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleUsageResponseApiCallsMade from a JSON string
billing_cycle_usage_response_api_calls_made_instance = BillingCycleUsageResponseApiCallsMade.from_json(json)
# print the JSON string representation of the object
print(BillingCycleUsageResponseApiCallsMade.to_json())

# convert the object into a dict
billing_cycle_usage_response_api_calls_made_dict = billing_cycle_usage_response_api_calls_made_instance.to_dict()
# create an instance of BillingCycleUsageResponseApiCallsMade from a dict
billing_cycle_usage_response_api_calls_made_from_dict = BillingCycleUsageResponseApiCallsMade.from_dict(billing_cycle_usage_response_api_calls_made_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


