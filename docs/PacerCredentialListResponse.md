# PacerCredentialListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'PacerCredentialListResponse']
**total_pages** | **int** | Total number of pages available. | 
**total_count** | **int** | Total number of pacer credentials available. | 
**page_number** | **int** | Current page number. | 
**next_page_api** | **str** | Link for the next page. | 
**previous_page_api** | **str** | Link for the previous page. | 
**pacer_credential_array** | [**List[PacerCredential]**](PacerCredential.md) | Array of pacer credentials. | 

## Example

```python
from unicourt.models.pacer_credential_list_response import PacerCredentialListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PacerCredentialListResponse from a JSON string
pacer_credential_list_response_instance = PacerCredentialListResponse.from_json(json)
# print the JSON string representation of the object
print(PacerCredentialListResponse.to_json())

# convert the object into a dict
pacer_credential_list_response_dict = pacer_credential_list_response_instance.to_dict()
# create an instance of PacerCredentialListResponse from a dict
pacer_credential_list_response_from_dict = PacerCredentialListResponse.from_dict(pacer_credential_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


