# AccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Client ID obtainable by logging into your UniCourt account. | 
**client_secret** | **str** | Your Client Secret ID obtainable by logging into your UniCourt account. | 

## Example

```python
from unicourt.models.access_token_request import AccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenRequest from a JSON string
access_token_request_instance = AccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokenRequest.to_json())

# convert the object into a dict
access_token_request_dict = access_token_request_instance.to_dict()
# create an instance of AccessTokenRequest from a dict
access_token_request_from_dict = AccessTokenRequest.from_dict(access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


