# unicourt.CaseUpdateApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case_update_by_case_id**](CaseUpdateApi.md#get_case_update_by_case_id) | **GET** /caseUpdate/{caseId} | Get Case Updates for a requested CaseId.
[**get_case_updates**](CaseUpdateApi.md#get_case_updates) | **GET** /caseUpdates | Get Case Update  list for a requested Date.
[**update_case**](CaseUpdateApi.md#update_case) | **PUT** /caseUpdate | Add Case Update for the requested Case Id.


# **get_case_update_by_case_id**
> CaseUpdate get_case_update_by_case_id(case_id)

Get Case Updates for a requested CaseId.

Retrieve case updates for the specified case object.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_update import CaseUpdate
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
    api_instance = unicourt.CaseUpdateApi(api_client)
    case_id = 'CASEak99a698ea5413' # str | The caseId value of the case object for which updates are to be retrieved.

    try:
        # Get Case Updates for a requested CaseId.
        api_response = api_instance.get_case_update_by_case_id(case_id)
        print("The response of CaseUpdateApi->get_case_update_by_case_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseUpdateApi->get_case_update_by_case_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value of the case object for which updates are to be retrieved. | 

### Return type

[**CaseUpdate**](CaseUpdate.md)

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
**451** | Sealed Case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_updates**
> CaseUpdateListResponse get_case_updates(case_id=case_id, requested_date=requested_date, status=status, page_number=page_number)

Get Case Update  list for a requested Date.

Retrieve case updates for the specified date.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_update_list_response import CaseUpdateListResponse
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
    api_instance = unicourt.CaseUpdateApi(api_client)
    case_id = 'CASEak99a698ea5413' # str | The caseId value of the case for which updates should be retrieved. (optional)
    requested_date = '2023-03-08T10:17:56+00:00' # datetime | The date for which case updates are to be retrieved. (optional)
    status = '' # str | Status of the case updates to be retrieved. (optional)
    page_number = 1 # int | The page number of the callbacks to be retrieved.<br>   - Minimum: 1  (optional) (default to 1)

    try:
        # Get Case Update  list for a requested Date.
        api_response = api_instance.get_case_updates(case_id=case_id, requested_date=requested_date, status=status, page_number=page_number)
        print("The response of CaseUpdateApi->get_case_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseUpdateApi->get_case_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value of the case for which updates should be retrieved. | [optional] 
 **requested_date** | **datetime**| The date for which case updates are to be retrieved. | [optional] 
 **status** | **str**| Status of the case updates to be retrieved. | [optional] 
 **page_number** | **int**| The page number of the callbacks to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional] [default to 1]

### Return type

[**CaseUpdateListResponse**](CaseUpdateListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_case**
> CaseUpdate update_case(case_update_request=case_update_request)

Add Case Update for the requested Case Id.

Request case updates for the specified case. The status will be ``IN_PROGRESS`` after it has been requested. If the request is not processed within 4 hours, it will be reported as ``DELAYED``.  If the request is still incomplete after 4 hours, it will remain in the DELAYED status for up to 72 hours after the request was approved. Such requests will be recorded as ``TIMEOUT`` after 72 hours. The progress of this Case Update request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/?api=UniCourt-Enterprise-Callback-Async-API-Spec.yaml#caseUpdate\">  Async API Documentation </a>

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_update import CaseUpdate
from unicourt.models.case_update_request import CaseUpdateRequest
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
    api_instance = unicourt.CaseUpdateApi(api_client)
    case_update_request = unicourt.CaseUpdateRequest() # CaseUpdateRequest |  (optional)

    try:
        # Add Case Update for the requested Case Id.
        api_response = api_instance.update_case(case_update_request=case_update_request)
        print("The response of CaseUpdateApi->update_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseUpdateApi->update_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_update_request** | [**CaseUpdateRequest**](CaseUpdateRequest.md)|  | [optional] 

### Return type

[**CaseUpdate**](CaseUpdate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

