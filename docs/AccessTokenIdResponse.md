# AccessTokenIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'AccessTokenIdResponse']
**token_id** | **str** | Unique Id for the access token. | 
**issued_date** | **datetime** | Date when access token was created. | 
**issue_address** | **str** | Ip address. | 

## Example

```python
from unicourt.models.access_token_id_response import AccessTokenIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenIdResponse from a JSON string
access_token_id_response_instance = AccessTokenIdResponse.from_json(json)
# print the JSON string representation of the object
print(AccessTokenIdResponse.to_json())

# convert the object into a dict
access_token_id_response_dict = access_token_id_response_instance.to_dict()
# create an instance of AccessTokenIdResponse from a dict
access_token_id_response_from_dict = AccessTokenIdResponse.from_dict(access_token_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


