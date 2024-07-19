# CaseDocumentOrderCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseDocumentOrderCallback']
**case_document_order_callback_id** | **str** | Unique Id for the Case Document Order Callback. | 
**case_document_id** | **str** | UniCourt&#39;s Case Document ID. | 
**callback_generated_date** | **datetime** | Date when the job is run. | 
**status** | **str** | Status of the request. | 
**case_document** | [**CaseDocument**](CaseDocument.md) |  | 
**case_document_order_callback_api** | **str** |  | 
**file** | [**ExportFile**](ExportFile.md) |  | 
**exception** | [**Exception**](Exception.md) |  | 

## Example

```python
from unicourt.models.case_document_order_callback import CaseDocumentOrderCallback

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDocumentOrderCallback from a JSON string
case_document_order_callback_instance = CaseDocumentOrderCallback.from_json(json)
# print the JSON string representation of the object
print(CaseDocumentOrderCallback.to_json())

# convert the object into a dict
case_document_order_callback_dict = case_document_order_callback_instance.to_dict()
# create an instance of CaseDocumentOrderCallback from a dict
case_document_order_callback_from_dict = CaseDocumentOrderCallback.from_dict(case_document_order_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


