# InvalidateAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Client ID obtainable by logging into your UniCourt account. | 
**client_secret** | **str** | Your Client Secret ID obtainable by logging into your UniCourt account. | 
**token_id** | **str** | The Token ID of token being invalidated | 

## Example

```python
from unicourt.models.invalidate_access_token_request import InvalidateAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateAccessTokenRequest from a JSON string
invalidate_access_token_request_instance = InvalidateAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(InvalidateAccessTokenRequest.to_json())

# convert the object into a dict
invalidate_access_token_request_dict = invalidate_access_token_request_instance.to_dict()
# create an instance of InvalidateAccessTokenRequest from a dict
invalidate_access_token_request_from_dict = InvalidateAccessTokenRequest.from_dict(invalidate_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


