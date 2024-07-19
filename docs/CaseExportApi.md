# unicourt.CaseExportApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_case**](CaseExportApi.md#export_case) | **GET** /caseExport/{caseId} | Gets case exported for a requested Case ID.
[**get_case_export_callback_by_id**](CaseExportApi.md#get_case_export_callback_by_id) | **GET** /caseExport/callbacks/{caseExportCallbackId} | Get Case Export Callback for a requested Case Export Callback Id.
[**get_case_export_callbacks**](CaseExportApi.md#get_case_export_callbacks) | **GET** /caseExport/callbacks | Get Case Export Callback list for a requested Date.


# **export_case**
> CaseExportCallback export_case(case_id)

Gets case exported for a requested Case ID.

Retrieve information about the specified case export.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_export_callback import CaseExportCallback
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
    api_instance = unicourt.CaseExportApi(api_client)
    case_id = 'CASEhq2c3224900a48' # str | The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/?api=UniCourt-Enterprise-Callback-Async-API-Spec.yaml#caseExport\">  Async API Documentation </a>

    try:
        # Gets case exported for a requested Case ID.
        api_response = api_instance.export_case(case_id)
        print("The response of CaseExportApi->export_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseExportApi->export_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value of the case for which case export information is to be retrieved. The progress of this Case Export request is available via web socket messages documented on &lt;a href&#x3D;\&quot;https://sapp.unicourt.com/developers/enterpriseapi/api/?api&#x3D;UniCourt-Enterprise-Callback-Async-API-Spec.yaml#caseExport\&quot;&gt;  Async API Documentation &lt;/a&gt; | 

### Return type

[**CaseExportCallback**](CaseExportCallback.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_export_callback_by_id**
> CaseExportCallback get_case_export_callback_by_id(case_export_callback_id)

Get Case Export Callback for a requested Case Export Callback Id.

Retrieve the specified case export callback object.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_export_callback import CaseExportCallback
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
    api_instance = unicourt.CaseExportApi(api_client)
    case_export_callback_id = 'CBCEG63f4e233eXqD1' # str | The caseExportCallbackId value of the case export callback object to be retrieved.

    try:
        # Get Case Export Callback for a requested Case Export Callback Id.
        api_response = api_instance.get_case_export_callback_by_id(case_export_callback_id)
        print("The response of CaseExportApi->get_case_export_callback_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseExportApi->get_case_export_callback_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_export_callback_id** | **str**| The caseExportCallbackId value of the case export callback object to be retrieved. | 

### Return type

[**CaseExportCallback**](CaseExportCallback.md)

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

# **get_case_export_callbacks**
> CaseExportCallbackListResponse get_case_export_callbacks(var_date=var_date, status=status, page_number=page_number)

Get Case Export Callback list for a requested Date.

Retrieve callbacks according to the specified criteria.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_export_callback_list_response import CaseExportCallbackListResponse
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
    api_instance = unicourt.CaseExportApi(api_client)
    var_date = '2023-03-08T10:17:56+00:00' # datetime | The date for which callbacks are to be retrieved. (optional)
    status = '' # str | The status code of the callbacks to be retrieved. (optional)
    page_number = 1 # int | The page number of the callbacks to be retrieved.<br>   - Minimum: 1  (optional) (default to 1)

    try:
        # Get Case Export Callback list for a requested Date.
        api_response = api_instance.get_case_export_callbacks(var_date=var_date, status=status, page_number=page_number)
        print("The response of CaseExportApi->get_case_export_callbacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseExportApi->get_case_export_callbacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| The date for which callbacks are to be retrieved. | [optional] 
 **status** | **str**| The status code of the callbacks to be retrieved. | [optional] 
 **page_number** | **int**| The page number of the callbacks to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional] [default to 1]

### Return type

[**CaseExportCallbackListResponse**](CaseExportCallbackListResponse.md)

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

