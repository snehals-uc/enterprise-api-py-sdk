# CallbackListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CallbackListResponse']
**case_document_order_callbacks** | [**CallbackListResponseCaseDocumentOrderCallbacks**](CallbackListResponseCaseDocumentOrderCallbacks.md) |  | 
**case_export_callbacks** | [**CallbackListResponseCaseDocumentOrderCallbacks**](CallbackListResponseCaseDocumentOrderCallbacks.md) |  | 

## Example

```python
from unicourt.models.callback_list_response import CallbackListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackListResponse from a JSON string
callback_list_response_instance = CallbackListResponse.from_json(json)
# print the JSON string representation of the object
print(CallbackListResponse.to_json())

# convert the object into a dict
callback_list_response_dict = callback_list_response_instance.to_dict()
# create an instance of CallbackListResponse from a dict
callback_list_response_from_dict = CallbackListResponse.from_dict(callback_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


