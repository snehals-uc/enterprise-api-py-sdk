# BillingCycleUsageResponseApiCallsCredited

Total number of callbackFailures including caseUpdate, caseDocumentOrder and caseExport for the billing cycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total API calls credited back for the billing cycle | 
**last_updated** | **datetime** | Last Updated date and time for the field apiCallsCredited | 

## Example

```python
from unicourt.models.billing_cycle_usage_response_api_calls_credited import BillingCycleUsageResponseApiCallsCredited

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleUsageResponseApiCallsCredited from a JSON string
billing_cycle_usage_response_api_calls_credited_instance = BillingCycleUsageResponseApiCallsCredited.from_json(json)
# print the JSON string representation of the object
print(BillingCycleUsageResponseApiCallsCredited.to_json())

# convert the object into a dict
billing_cycle_usage_response_api_calls_credited_dict = billing_cycle_usage_response_api_calls_credited_instance.to_dict()
# create an instance of BillingCycleUsageResponseApiCallsCredited from a dict
billing_cycle_usage_response_api_calls_credited_from_dict = BillingCycleUsageResponseApiCallsCredited.from_dict(billing_cycle_usage_response_api_calls_credited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


