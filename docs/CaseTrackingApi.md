# unicourt.CaseTrackingApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case_track_by_id**](CaseTrackingApi.md#get_case_track_by_id) | **GET** /caseTrack/{caseId} | Get Case Track for a requested Case Id.
[**get_case_tracks**](CaseTrackingApi.md#get_case_tracks) | **GET** /caseTracks | Get Case Track list.
[**remove_case_track_by_id**](CaseTrackingApi.md#remove_case_track_by_id) | **DELETE** /caseTrack/{caseId} | Remove Case Track for a specific Case Id.
[**track_case**](CaseTrackingApi.md#track_case) | **PUT** /caseTrack | Add Case Track for the requested Case Id.


# **get_case_track_by_id**
> CaseTrack get_case_track_by_id(case_id)

Get Case Track for a requested Case Id.

Retrieve case tracking information for the specified caseId value.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_track import CaseTrack
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
    api_instance = unicourt.CaseTrackingApi(api_client)
    case_id = 'CASEak99a698ea5413' # str | The caseId value for which case tracking information is to be retrieved.

    try:
        # Get Case Track for a requested Case Id.
        api_response = api_instance.get_case_track_by_id(case_id)
        print("The response of CaseTrackingApi->get_case_track_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseTrackingApi->get_case_track_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value for which case tracking information is to be retrieved. | 

### Return type

[**CaseTrack**](CaseTrack.md)

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

# **get_case_tracks**
> CaseTrackListResponse get_case_tracks(last_fetch_date=last_fetch_date, last_fetch_date_with_updates=last_fetch_date_with_updates, page_number=page_number)

Get Case Track list.

Retrieve a list of all tracked cases.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_track_list_response import CaseTrackListResponse
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
    api_instance = unicourt.CaseTrackingApi(api_client)
    last_fetch_date = '2023-03-08T10:17:56+00:00' # datetime | The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.  (optional)
    last_fetch_date_with_updates = '2023-03-08T10:17:56+00:00' # datetime | The date on which changes were last found in the case information.  (optional)
    page_number = 1 # int | The page number of the results to be retrieved.<br>   - Minimum: 1  (optional)

    try:
        # Get Case Track list.
        api_response = api_instance.get_case_tracks(last_fetch_date=last_fetch_date, last_fetch_date_with_updates=last_fetch_date_with_updates, page_number=page_number)
        print("The response of CaseTrackingApi->get_case_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseTrackingApi->get_case_tracks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_fetch_date** | **datetime**| The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.  | [optional] 
 **last_fetch_date_with_updates** | **datetime**| The date on which changes were last found in the case information.  | [optional] 
 **page_number** | **int**| The page number of the results to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional] 

### Return type

[**CaseTrackListResponse**](CaseTrackListResponse.md)

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

# **remove_case_track_by_id**
> Success remove_case_track_by_id(case_id)

Remove Case Track for a specific Case Id.

Remove Case Track for a specific Case Id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.success import Success
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
    api_instance = unicourt.CaseTrackingApi(api_client)
    case_id = 'CASEak99a698ea5413' # str | The caseId value for which case tracking information is to be retrieved.

    try:
        # Remove Case Track for a specific Case Id.
        api_response = api_instance.remove_case_track_by_id(case_id)
        print("The response of CaseTrackingApi->remove_case_track_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseTrackingApi->remove_case_track_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The caseId value for which case tracking information is to be retrieved. | 

### Return type

[**Success**](Success.md)

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

# **track_case**
> Success track_case(case_track_request=case_track_request)

Add Case Track for the requested Case Id.

Track the specified case. The progress of this Case Track request is available via web socket messages documented on <a href=\"https://sapp.unicourt.com/developers/enterpriseapi/api/?api=UniCourt-Enterprise-Callback-Async-API-Spec.yaml#liveCallbacks\">  Async API Documentation </a>

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.case_track_request import CaseTrackRequest
from unicourt.models.success import Success
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
    api_instance = unicourt.CaseTrackingApi(api_client)
    case_track_request = unicourt.CaseTrackRequest() # CaseTrackRequest |  (optional)

    try:
        # Add Case Track for the requested Case Id.
        api_response = api_instance.track_case(case_track_request=case_track_request)
        print("The response of CaseTrackingApi->track_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseTrackingApi->track_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_track_request** | [**CaseTrackRequest**](CaseTrackRequest.md)|  | [optional] 

### Return type

[**Success**](Success.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

