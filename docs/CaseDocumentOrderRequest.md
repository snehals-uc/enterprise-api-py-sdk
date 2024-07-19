# CaseDocumentOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_document_id** | **str** | Document ID which you want to order. | 
**is_preview_only** | **bool** | Flag value to determine if the document order is a preview order or no. | 
**pacer_options** | [**CaseDocumentOrderPacerOptions**](CaseDocumentOrderPacerOptions.md) |  | [optional] 

## Example

```python
from unicourt.models.case_document_order_request import CaseDocumentOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDocumentOrderRequest from a JSON string
case_document_order_request_instance = CaseDocumentOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CaseDocumentOrderRequest.to_json())

# convert the object into a dict
case_document_order_request_dict = case_document_order_request_instance.to_dict()
# create an instance of CaseDocumentOrderRequest from a dict
case_document_order_request_from_dict = CaseDocumentOrderRequest.from_dict(case_document_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


