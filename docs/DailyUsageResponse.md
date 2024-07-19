# DailyUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'DailyUsageResponse']
**usage_start_time** | **datetime** | Start time of the usage. | 
**usage_end_time** | **datetime** | End time of the usage. | 
**api_usage** | **object** | Api Usage made in real time. | 
**api_calls_made** | [**BillingCycleUsageResponseApiCallsMade**](BillingCycleUsageResponseApiCallsMade.md) |  | 
**api_calls_credited** | [**BillingCycleUsageResponseApiCallsCredited**](BillingCycleUsageResponseApiCallsCredited.md) |  | 
**api_calls_billable** | [**BillingCycleUsageResponseApiCallsBillable**](BillingCycleUsageResponseApiCallsBillable.md) |  | 

## Example

```python
from unicourt.models.daily_usage_response import DailyUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DailyUsageResponse from a JSON string
daily_usage_response_instance = DailyUsageResponse.from_json(json)
# print the JSON string representation of the object
print(DailyUsageResponse.to_json())

# convert the object into a dict
daily_usage_response_dict = daily_usage_response_instance.to_dict()
# create an instance of DailyUsageResponse from a dict
daily_usage_response_from_dict = DailyUsageResponse.from_dict(daily_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


