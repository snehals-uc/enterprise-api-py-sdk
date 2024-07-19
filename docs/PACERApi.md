# unicourt.PACERApi

All URIs are relative to *https://enterpriseapi.staging.unicourt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_courts_pacer_case_locator_case_search**](PACERApi.md#all_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/allCourts | PACER Case Locator Search API for All Courts.
[**all_courts_pacer_case_locator_party_search**](PACERApi.md#all_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/allCourts | PACER Case Locator Search API for All Courts.
[**appeal_courts_pacer_case_locator_case_search**](PACERApi.md#appeal_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/appealCourts | PACER Case Locator Search API for All Courts.
[**appeal_courts_pacer_case_locator_party_search**](PACERApi.md#appeal_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/appealCourts | PACER Case Locator Search API for All Courts.
[**bankruptcy_courts_pacer_case_locator_case_search**](PACERApi.md#bankruptcy_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/bankruptcyCourts | PACER Case Locator Search API for Bankruptcy Courts.
[**bankruptcy_courts_pacer_case_locator_party_search**](PACERApi.md#bankruptcy_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/bankruptcyCourts | PACER Case Locator Search API for All Courts.
[**civil_courts_pacer_case_locator_case_search**](PACERApi.md#civil_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/civilCourts | PACER Case Locator Search API for All Courts.
[**civil_courts_pacer_case_locator_party_search**](PACERApi.md#civil_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/civilCourts | PACER Case Locator Search API for All Courts.
[**criminal_courts_pacer_case_locator_case_search**](PACERApi.md#criminal_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/criminalCourts | PACER Case Locator Search API for All Courts.
[**criminal_courts_pacer_case_locator_party_search**](PACERApi.md#criminal_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/criminalCourts | PACER Case Locator Search API for All Courts.
[**import_pacer_case_by_court_using_case_number**](PACERApi.md#import_pacer_case_by_court_using_case_number) | **GET** /pacer/importCaseByCourtUsingCaseNumber | Find PACER Case for a requested Case Number and Court.
[**multi_district_courts_pacer_case_locator_case_search**](PACERApi.md#multi_district_courts_pacer_case_locator_case_search) | **GET** /pacerCaseLocator/caseSearch/multiDistrictCourts | PACER Case Locator Search API for All Courts.
[**multi_district_courts_pacer_case_locator_party_search**](PACERApi.md#multi_district_courts_pacer_case_locator_party_search) | **GET** /pacerCaseLocator/partySearch/multiDistrictCourts | PACER Case Locator Search API for All Courts.


# **all_courts_pacer_case_locator_case_search**
> PCLCase all_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search all courts within the PACER system for a particular case.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '21-119' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 17118 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.all_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->all_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->all_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_courts_pacer_case_locator_party_search**
> PCLParty all_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party across all PACER case filings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '21-119' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'Warden' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'first_name_example' # str | The first name of the target party. (optional)
    middle_name = 'middle_name_example' # str | The middle name of the target party. (optional)
    generation = 'generation_example' # str | The suffix (e.g., Jr., III) of the target party's name. (optional)
    party_type = 'party_type_example' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.all_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->all_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->all_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The suffix (e.g., Jr., III) of the target party&#39;s name. | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appeal_courts_pacer_case_locator_case_search**
> PCLCase appeal_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, nature_of_suits_array=nature_of_suits_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for PACER cases filed in U.S. Courts of Appeals.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    nature_of_suits_array = ['nature_of_suits_array_example'] # List[Optional[str]] | The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150 (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.appeal_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, nature_of_suits_array=nature_of_suits_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->appeal_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->appeal_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **nature_of_suits_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned nature of suit classification of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits&#39;&gt;PCL Nature of Suits&lt;/a&gt; for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments &amp; Enforc. of Judgments), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray&#x3D;1110&amp;natureOfSuitsArray&#x3D;1150 | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appeal_courts_pacer_case_locator_party_search**
> PCLParty appeal_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party across all PACER appeals cases.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'Smith' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'John' # str | The first name of the target party. (optional)
    middle_name = 'Doe' # str | The middle name of the target party. (optional)
    generation = 'MD' # str | The suffix (e.g., Jr., III) of the target party's name. (optional)
    party_type = 'ptf' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.appeal_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->appeal_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->appeal_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The suffix (e.g., Jr., III) of the target party&#39;s name. | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankruptcy_courts_pacer_case_locator_case_search**
> PCLCase bankruptcy_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, federal_bankruptcy_chapter_array=federal_bankruptcy_chapter_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, case_discharged_start_date=case_discharged_start_date, case_discharged_end_date=case_discharged_end_date, case_dismissed_start_date=case_dismissed_start_date, case_dismissed_end_date=case_dismissed_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for Bankruptcy Courts.

Search for PACER cases filed in U.S. Bankruptcy Courts.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    federal_bankruptcy_chapter_array = ['federal_bankruptcy_chapter_array_example'] # List[Optional[str]] | The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters'>PCL Bankruptcy Chapters</a> for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11 (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_discharged_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_discharged_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_dismissed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_dismissed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for Bankruptcy Courts.
        api_response = api_instance.bankruptcy_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, federal_bankruptcy_chapter_array=federal_bankruptcy_chapter_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, case_discharged_start_date=case_discharged_start_date, case_discharged_end_date=case_discharged_end_date, case_dismissed_start_date=case_dismissed_start_date, case_dismissed_end_date=case_dismissed_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->bankruptcy_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->bankruptcy_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **federal_bankruptcy_chapter_array** | [**List[Optional[str]]**](str.md)| The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please refer &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-d-bankruptcy-chapters&#39;&gt;PCL Bankruptcy Chapters&lt;/a&gt; for a list of valid chapter numbers.    Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.    Example: federalBankruptcyChapterArray&#x3D;7&amp;federalBankruptcyChapterArray&#x3D;11 | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_discharged_start_date** | **datetime**| The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_discharged_end_date** | **datetime**| The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_dismissed_start_date** | **datetime**| The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_dismissed_end_date** | **datetime**| The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bankruptcy_courts_pacer_case_locator_party_search**
> PCLParty bankruptcy_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, ssn_or_ein=ssn_or_ein, four_digit_ssn=four_digit_ssn, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, case_discharged_start_date=case_discharged_start_date, case_discharged_end_date=case_discharged_end_date, case_dismissed_start_date=case_dismissed_start_date, case_dismissed_end_date=case_dismissed_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party in PACER bankruptcy filings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'Smith' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'John' # str | The first name of the target party. (optional)
    middle_name = 'Doe' # str | The middle name of the target party. (optional)
    generation = 'MD' # str | The suffix (e.g., Jr., III) of the target party's name. (optional)
    party_type = 'ptf' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    ssn_or_ein = 'ssn_or_ein_example' # str | The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes. (optional)
    four_digit_ssn = 'four_digit_ssn_example' # str | The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified. (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_discharged_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_discharged_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_dismissed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. (optional)
    case_dismissed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.bankruptcy_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, ssn_or_ein=ssn_or_ein, four_digit_ssn=four_digit_ssn, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, case_discharged_start_date=case_discharged_start_date, case_discharged_end_date=case_discharged_end_date, case_dismissed_start_date=case_dismissed_start_date, case_dismissed_end_date=case_dismissed_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->bankruptcy_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->bankruptcy_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The suffix (e.g., Jr., III) of the target party&#39;s name. | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **ssn_or_ein** | **str**| The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes. | [optional] 
 **four_digit_ssn** | **str**| The last four digits of the Social Security number of the target party.   Note: When specified, a last name/entity name must also be specified. | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_discharged_start_date** | **datetime**| The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_discharged_end_date** | **datetime**| The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_dismissed_start_date** | **datetime**| The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).    Note: This parameter is applicable since we only perform this search for Bankruptcy Court type. | [optional] 
 **case_dismissed_end_date** | **datetime**| The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **civil_courts_pacer_case_locator_case_search**
> PCLCase civil_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, nature_of_suits_array=nature_of_suits_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for civil cases filed in PACER.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    nature_of_suits_array = ['nature_of_suits_array_example'] # List[Optional[str]] | The PACER-assigned nature of suit classification of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits'>PCL Nature of Suits</a> for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray=110&natureOfSuitsArray=140 (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.civil_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, nature_of_suits_array=nature_of_suits_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->civil_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->civil_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **nature_of_suits_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned nature of suit classification of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-e-nature-of-suits&#39;&gt;PCL Nature of Suits&lt;/a&gt; for valid nature-of-suit classifications for cases.    Scenario: When mulitple nature of suits needs to be requested.    Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.    Example: natureOfSuitsArray&#x3D;110&amp;natureOfSuitsArray&#x3D;140 | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **civil_courts_pacer_case_locator_party_search**
> PCLParty civil_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party in civil cases filed in PACER.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'Smith' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'John' # str | The first name of the target party. (optional)
    middle_name = 'Doe' # str | The middle name of the target party. (optional)
    generation = 'MD' # str | The name suffix (e.g., III, MD). (optional)
    party_type = 'ptf' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.civil_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->civil_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->civil_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The name suffix (e.g., III, MD). | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **criminal_courts_pacer_case_locator_case_search**
> PCLCase criminal_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for criminal cases in PACER.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.criminal_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->criminal_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->criminal_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **criminal_courts_pacer_case_locator_party_search**
> PCLParty criminal_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party in PACER criminal cases.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = '07-1026' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'Smith' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'John' # str | The first name of the target party. (optional)
    middle_name = 'Doe' # str | The middle name of the target party. (optional)
    generation = 'MD' # str | The suffix (e.g., Jr., III) of the target party's name. (optional)
    party_type = 'ptf' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.criminal_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->criminal_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->criminal_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The suffix (e.g., Jr., III) of the target party&#39;s name. | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_pacer_case_by_court_using_case_number**
> PACERImportCase import_pacer_case_by_court_using_case_number(pacer_user_id, case_number, court_id, pacer_client_code=pacer_client_code)

Find PACER Case for a requested Case Number and Court.

Import the specified case from PACER.    Workflow:     1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.     2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.    Note:     1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.     2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pacer_import_case import PACERImportCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The PACER username of the PACER account under which the case should be imported.
    case_number = '2:15-mc-12345' # str | The case number of the case to be imported.
    court_id = 'CORTjF63b8Z4d2i9UB' # str | The courtId value of the court from which the case is to be imported.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)

    try:
        # Find PACER Case for a requested Case Number and Court.
        api_response = api_instance.import_pacer_case_by_court_using_case_number(pacer_user_id, case_number, court_id, pacer_client_code=pacer_client_code)
        print("The response of PACERApi->import_pacer_case_by_court_using_case_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->import_pacer_case_by_court_using_case_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The PACER username of the PACER account under which the case should be imported. | 
 **case_number** | **str**| The case number of the case to be imported. | 
 **court_id** | **str**| The courtId value of the court from which the case is to be imported. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 

### Return type

[**PACERImportCase**](PACERImportCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multi_district_courts_pacer_case_locator_case_search**
> PCLCase multi_district_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, jpml_number=jpml_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for multidistrict litigation in PACER.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_case import PCLCase
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = 'case_number_example' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    jpml_number = 875 # int | Master JPML Case Number. (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'caseYear,DESC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC (optional) (default to 'caseYear,DESC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.multi_district_courts_pacer_case_locator_case_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, jpml_number=jpml_number, pacer_case_id=pacer_case_id, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->multi_district_courts_pacer_case_locator_case_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->multi_district_courts_pacer_case_locator_case_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **jpml_number** | **int**| Master JPML Case Number. | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC | [optional] [default to &#39;caseYear,DESC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLCase**](PCLCase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multi_district_courts_pacer_case_locator_party_search**
> PCLParty multi_district_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, jpml_number=jpml_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)

PACER Case Locator Search API for All Courts.

Search for the specified party in multidistrict litigation in PACER.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unicourt
from unicourt.models.pcl_party import PCLParty
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
    api_instance = unicourt.PACERApi(api_client)
    pacer_user_id = 'john_doe' # str | The username of the PACER account under which the search is to be performed.
    pacer_client_code = 'john' # str | This is mandatory if your setting in PACER website is set to Yes for the flag `Require Client Code?` under `Set PACER Billing Preferences` page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) (optional)
    case_number = 'case_number_example' # str | The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). (optional)
    jpml_number = 56 # int | Master JPML Case Number. (optional)
    pacer_case_id = 56 # int | The PACER-assigned identifier of the target case. (optional)
    last_name = 'John' # str | The last name (for an individual) or the entity name (for a business entity) of the target party. (optional)
    first_name = 'first_name_example' # str | The first name of the target party. (optional)
    middle_name = 'middle_name_example' # str | The middle name of the target party. (optional)
    generation = 'generation_example' # str | The suffix (e.g., Jr., III) of the target party's name. (optional)
    party_type = 'party_type_example' # str | The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    party_exact_name_match = True # bool | Specify whether the search string must match the name of the target party exactly. (optional)
    party_role_array = ['party_role_array_example'] # List[Optional[str]] | The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. (optional)
    case_title = 'case_title_example' # str | The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. (optional)
    case_office = 'case_office_example' # str | The divisional office in which the case was filed. (optional)
    case_sequence_number = 56 # int | The PACER-assigned sequence number of the target case. Ex 12345 (optional)
    case_year = 56 # int | The two- or four-digit year in which the target case was filed. (optional)
    case_type_array = ['case_type_array_example'] # List[Optional[str]] | The PACER-assigned case type of the target case. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types'>PCL Case Types</a> for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray=cv&caseTypeArray=cr (optional)
    court_region_id_array = ['court_region_id_array_example'] # List[Optional[str]] | The PACER-assigned court region in which the target case was filed. Please  refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions'>PCL Court Regions</a> for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray=cac&courtRegionIdArray=cae (optional)
    case_year_from = 56 # int | Limit the results of the search to those cases from the year specified or later (optional)
    case_year_to = 56 # int | Limit the results of the search to those cases from the year specified or earlier (optional)
    case_filed_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_filed_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_start_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    case_terminated_end_date = '2013-10-20T19:20:30+01:00' # datetime | The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). (optional)
    sort_parameter_query = 'lastName,ASC' # str | How search results from PACER are to be sorted. Please refer to <a href='https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter'>PCL Sort Parameters</a> for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtId,ASC&caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery=courtCase.caseOffice,ASC&caseId,DESC (optional) (default to 'lastName,ASC')
    case_status = 'case_status_example' # str | Whether the target case is marked as 'open' or 'closed' within PACER. (optional)
    page_number = 1 # int | The page number of the search results to be retrieved. (optional)

    try:
        # PACER Case Locator Search API for All Courts.
        api_response = api_instance.multi_district_courts_pacer_case_locator_party_search(pacer_user_id, pacer_client_code=pacer_client_code, case_number=case_number, jpml_number=jpml_number, pacer_case_id=pacer_case_id, last_name=last_name, first_name=first_name, middle_name=middle_name, generation=generation, party_type=party_type, party_exact_name_match=party_exact_name_match, party_role_array=party_role_array, case_title=case_title, case_office=case_office, case_sequence_number=case_sequence_number, case_year=case_year, case_type_array=case_type_array, court_region_id_array=court_region_id_array, case_year_from=case_year_from, case_year_to=case_year_to, case_filed_start_date=case_filed_start_date, case_filed_end_date=case_filed_end_date, case_terminated_start_date=case_terminated_start_date, case_terminated_end_date=case_terminated_end_date, sort_parameter_query=sort_parameter_query, case_status=case_status, page_number=page_number)
        print("The response of PACERApi->multi_district_courts_pacer_case_locator_party_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PACERApi->multi_district_courts_pacer_case_locator_party_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pacer_user_id** | **str**| The username of the PACER account under which the search is to be performed. | 
 **pacer_client_code** | **str**| This is mandatory if your setting in PACER website is set to Yes for the flag &#x60;Require Client Code?&#x60; under &#x60;Set PACER Billing Preferences&#x60; page. The client code is a text field entered by users upon login that can be used to track usage by person, client matter number, or other meaningful entry up to 32 characters, comprising the following:    Alphabetic characters (A-Z or a-z)    Numeric digits (0-9)   Period (.)    Underscore (_)    Hyphen (-)    Slash (/) | [optional] 
 **case_number** | **str**| The case number of the target case. You may use the following case-number formats:    yy-nnnnn    yy-tp-nnnnn    yy tp nnnnn    yytpnnnnn    o:yy-nnnnn    o:yy-tp-nnnnn    o:yy tp nnnnn    o:yytpnnnnn   where:   yy  case year (may be 2 or 4 digits)   nnnnn  case number (up to 5 digits)   tp  case type (up to 2 characters)   o  office where the case was filed (1 digit). | [optional] 
 **jpml_number** | **int**| Master JPML Case Number. | [optional] 
 **pacer_case_id** | **int**| The PACER-assigned identifier of the target case. | [optional] 
 **last_name** | **str**| The last name (for an individual) or the entity name (for a business entity) of the target party. | [optional] 
 **first_name** | **str**| The first name of the target party. | [optional] 
 **middle_name** | **str**| The middle name of the target party. | [optional] 
 **generation** | **str**| The suffix (e.g., Jr., III) of the target party&#39;s name. | [optional] 
 **party_type** | **str**| The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **party_exact_name_match** | **bool**| Specify whether the search string must match the name of the target party exactly. | [optional] 
 **party_role_array** | [**List[Optional[str]]**](str.md)| The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court. | [optional] 
 **case_title** | **str**| The title of the target case.    Examples:    A search for case title john doe v will result in all cases with the case title John Doe v.    A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc. | [optional] 
 **case_office** | **str**| The divisional office in which the case was filed. | [optional] 
 **case_sequence_number** | **int**| The PACER-assigned sequence number of the target case. Ex 12345 | [optional] 
 **case_year** | **int**| The two- or four-digit year in which the target case was filed. | [optional] 
 **case_type_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned case type of the target case. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-a-case-types&#39;&gt;PCL Case Types&lt;/a&gt; for valid case-type values.    Scenario: When mulitple case types needs to be requested.    Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.    Example: caseTypeArray&#x3D;cv&amp;caseTypeArray&#x3D;cr | [optional] 
 **court_region_id_array** | [**List[Optional[str]]**](str.md)| The PACER-assigned court region in which the target case was filed. Please  refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-b-court-regions&#39;&gt;PCL Court Regions&lt;/a&gt; for valid court-region values.    Scenario: When mulitple court region ids needs to be requested.    Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.    Example: courtRegionIdArray&#x3D;cac&amp;courtRegionIdArray&#x3D;cae | [optional] 
 **case_year_from** | **int**| Limit the results of the search to those cases from the year specified or later | [optional] 
 **case_year_to** | **int**| Limit the results of the search to those cases from the year specified or earlier | [optional] 
 **case_filed_start_date** | **datetime**| The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_filed_end_date** | **datetime**| The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_start_date** | **datetime**| The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **case_terminated_end_date** | **datetime**| The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00). | [optional] 
 **sort_parameter_query** | **str**| How search results from PACER are to be sorted. Please refer to &lt;a href&#x3D;&#39;https://docs.unicourt.com/knowledge-base/pacer-glossary.md/appendix-c-sort-parameter&#39;&gt;PCL Sort Parameters&lt;/a&gt; for valid sort-related settings.    Scenario 1: When mulitple sort paramters needs to be requested.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtId,ASC&amp;caseId,ASC    Scenario 2: When you want to sort the response using the case parameters in the party search.    Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.    Example: sortParameterQuery&#x3D;courtCase.caseOffice,ASC&amp;caseId,DESC | [optional] [default to &#39;lastName,ASC&#39;]
 **case_status** | **str**| Whether the target case is marked as &#39;open&#39; or &#39;closed&#39; within PACER. | [optional] 
 **page_number** | **int**| The page number of the search results to be retrieved. | [optional] 

### Return type

[**PCLParty**](PCLParty.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request is recieved. |  -  |
**400** | Invalid Input Parameter |  -  |
**424** | Issue at the Court Source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

