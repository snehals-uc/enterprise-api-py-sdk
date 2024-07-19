# unicourt.UsageApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_cycles**](UsageApi.md#get_billing_cycles) | **GET** /billingCycles | Get all the previous 12 billing cycles.
[**get_billing_usage_by_billing_cycle**](UsageApi.md#get_billing_usage_by_billing_cycle) | **GET** /billingCycleUsage/{billingCycle} | Specify the billing cycle to know the API usage.
[**get_daily_usage_by_date**](UsageApi.md#get_daily_usage_by_date) | **GET** /dailyUsage/{date} | Get API usage for a requested Date.


# **get_billing_cycles**
> BillingCyclesResponse get_billing_cycles()

Get all the previous 12 billing cycles.

An endpoint to obtain information on the previous 12 billing cycles.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.billing_cycles_response import BillingCyclesResponse
from unicourt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = unicourt.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unicourt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unicourt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unicourt.UsageApi(api_client)

    try:
        # Get all the previous 12 billing cycles.
        api_response = api_instance.get_billing_cycles()
        print("The response of UsageApi->get_billing_cycles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_billing_cycles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingCyclesResponse**](BillingCyclesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_usage_by_billing_cycle**
> BillingCycleUsageResponse get_billing_usage_by_billing_cycle(billing_cycle)

Specify the billing cycle to know the API usage.

An endpoint to obtain information on API usage for a specific billing cycle.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.billing_cycle_usage_response import BillingCycleUsageResponse
from unicourt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = unicourt.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unicourt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unicourt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unicourt.UsageApi(api_client)
    billing_cycle = '2023-01-25to2023-02-25' # str | The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on.

    try:
        # Specify the billing cycle to know the API usage.
        api_response = api_instance.get_billing_usage_by_billing_cycle(billing_cycle)
        print("The response of UsageApi->get_billing_usage_by_billing_cycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_billing_usage_by_billing_cycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_cycle** | **str**| The date obtainable from the /billingCycles endpoint which is used as an identifier for the specific billing cycle you wish to obtain information on. | 

### Return type

[**BillingCycleUsageResponse**](BillingCycleUsageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_daily_usage_by_date**
> DailyUsageResponse get_daily_usage_by_date(var_date)

Get API usage for a requested Date.

An endpoint to obtain information on API usage for a specific day.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.daily_usage_response import DailyUsageResponse
from unicourt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://enterpriseapi.staging.unicourt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = unicourt.Configuration(
    host = "https://enterpriseapi.staging.unicourt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unicourt.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unicourt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unicourt.UsageApi(api_client)
    var_date = '2023-02-21' # date | The specific date for which you wish to obtain information on API usage.

    try:
        # Get API usage for a requested Date.
        api_response = api_instance.get_daily_usage_by_date(var_date)
        print("The response of UsageApi->get_daily_usage_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_daily_usage_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| The specific date for which you wish to obtain information on API usage. | 

### Return type

[**DailyUsageResponse**](DailyUsageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

