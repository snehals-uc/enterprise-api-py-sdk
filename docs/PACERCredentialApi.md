# unicourt.PACERCredentialApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pacer_credential**](PACERCredentialApi.md#add_pacer_credential) | **PUT** /pacerCredential | Add Pacer Credential.
[**get_pacer_credential**](PACERCredentialApi.md#get_pacer_credential) | **GET** /pacerCredential | Get Pacer Credential List.
[**get_pacer_credential_by_id**](PACERCredentialApi.md#get_pacer_credential_by_id) | **GET** /pacerCredential/{pacerUserId} | Get Pacer Credential for a requested pacer User Id.
[**remove_pacer_credential_by_id**](PACERCredentialApi.md#remove_pacer_credential_by_id) | **DELETE** /pacerCredential/{pacerUserId} | Remove Pacer credential for a specific Pacer User Id.


# **add_pacer_credential**
> Success add_pacer_credential(pacer_credential_request=pacer_credential_request)

Add Pacer Credential.

Register PACER credentials with UniCourt.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pacer_credential_request import PacerCredentialRequest
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
    api_instance = unicourt.PACERCredentialApi(api_client)
    pacer_credential_request = unicourt.PacerCredentialRequest() # PacerCredentialRequest |  (optional)

    try:
        # Add Pacer Credential.
        api_response = api_instance.add_pacer_credential(pacer_credential_request=pacer_credential_request)
        print("The response of PACERCredentialApi->add_pacer_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERCredentialApi->add_pacer_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_credential_request** | [**PacerCredentialRequest**](PacerCredentialRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pacer_credential**
> PacerCredentialListResponse get_pacer_credential(page_number=page_number)

Get Pacer Credential List.

List registered PACER credentials.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pacer_credential_list_response import PacerCredentialListResponse
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
    api_instance = unicourt.PACERCredentialApi(api_client)
    page_number = 1 # int | The page number of the PACER credentials to be retrieved.<br>   - Minimum: 1  (optional)

    try:
        # Get Pacer Credential List.
        api_response = api_instance.get_pacer_credential(page_number=page_number)
        print("The response of PACERCredentialApi->get_pacer_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERCredentialApi->get_pacer_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| The page number of the PACER credentials to be retrieved.&lt;br&gt;   - Minimum: 1  | [optional] 

### Return type

[**PacerCredentialListResponse**](PacerCredentialListResponse.md)

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

# **get_pacer_credential_by_id**
> PacerCredential get_pacer_credential_by_id(pacer_user_id)

Get Pacer Credential for a requested pacer User Id.

Retrieve the PACER credentials for the specified PACER username.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pacer_credential import PacerCredential
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
    api_instance = unicourt.PACERCredentialApi(api_client)
    pacer_user_id = 'URKYwer3tyh5r56gq2' # str | The PACER username for which PACER credentials are to be retrieved.

    try:
        # Get Pacer Credential for a requested pacer User Id.
        api_response = api_instance.get_pacer_credential_by_id(pacer_user_id)
        print("The response of PACERCredentialApi->get_pacer_credential_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERCredentialApi->get_pacer_credential_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The PACER username for which PACER credentials are to be retrieved. | 

### Return type

[**PacerCredential**](PacerCredential.md)

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

# **remove_pacer_credential_by_id**
> Success remove_pacer_credential_by_id(pacer_user_id)

Remove Pacer credential for a specific Pacer User Id.

De-register the PACER credentials for the specified PACER username.

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
    api_instance = unicourt.PACERCredentialApi(api_client)
    pacer_user_id = 'URKYwer3tyh5r56gq2' # str | The PACER username for which PACER credentials are to be retrieved.

    try:
        # Remove Pacer credential for a specific Pacer User Id.
        api_response = api_instance.remove_pacer_credential_by_id(pacer_user_id)
        print("The response of PACERCredentialApi->remove_pacer_credential_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERCredentialApi->remove_pacer_credential_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The PACER username for which PACER credentials are to be retrieved. | 

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

