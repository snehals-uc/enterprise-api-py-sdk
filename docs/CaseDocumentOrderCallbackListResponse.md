# CaseDocumentOrderCallbackListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseDocumentOrderCallbackListResponse']
**total_pages** | **int** | Total number of pages available. | 
**total_count** | **int** | Total number of case document order callback objects available. | 
**page_number** | **int** | Current page number. | 
**next_page_api** | **str** | Link for the next page. | 
**previous_page_api** | **str** | Link for the previous page. | 
**callback_array** | [**List[CaseDocumentOrderCallback]**](CaseDocumentOrderCallback.md) | Array of case document order callback objects. | 

## Example

```python
from unicourt.models.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDocumentOrderCallbackListResponse from a JSON string
case_document_order_callback_list_response_instance = CaseDocumentOrderCallbackListResponse.from_json(json)
# print the JSON string representation of the object
print(CaseDocumentOrderCallbackListResponse.to_json())

# convert the object into a dict
case_document_order_callback_list_response_dict = case_document_order_callback_list_response_instance.to_dict()
# create an instance of CaseDocumentOrderCallbackListResponse from a dict
case_document_order_callback_list_response_from_dict = CaseDocumentOrderCallbackListResponse.from_dict(case_document_order_callback_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


