# AccessTokenIdListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'AccessTokenIdListResponse']
**access_token_id_array** | [**List[AccessTokenIdResponse]**](AccessTokenIdResponse.md) | Array of access tokens Id. | 

## Example

```python
from unicourt.models.access_token_id_list_response import AccessTokenIdListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenIdListResponse from a JSON string
access_token_id_list_response_instance = AccessTokenIdListResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenIdListResponse.to_json())

# convert the object into a dict
access_token_id_list_response_dict = access_token_id_list_response_instance.to_dict()
# create an instance of AccessTokenIdListResponse from a dict
access_token_id_list_response_from_dict = AccessTokenIdListResponse.from_dict(access_token_id_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


