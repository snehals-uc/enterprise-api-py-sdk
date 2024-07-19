# DocketEntrySecondaryDocuments

Secondary Documents refers to documents that are attached to a docket entry. Secondary Documents could be specific to a courts or case type in courts. For isntance the below example is in PACER. PACER District Courts - Here the secondary document is one which is attached in the docket entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'DocketEntrySecondaryDocuments']
**page_number** | **int** | Page number for which results where obtained. | 
**case_document_array** | [**List[CaseDocument]**](CaseDocument.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case. entity in a Case. | 

## Example

```python
from unicourt.models.docket_entry_secondary_documents import DocketEntrySecondaryDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of DocketEntrySecondaryDocuments from a JSON string
docket_entry_secondary_documents_instance = DocketEntrySecondaryDocuments.from_json(json)
# print the JSON string representation of the object
print(DocketEntrySecondaryDocuments.to_json())

# convert the object into a dict
docket_entry_secondary_documents_dict = docket_entry_secondary_documents_instance.to_dict()
# create an instance of DocketEntrySecondaryDocuments from a dict
docket_entry_secondary_documents_from_dict = DocketEntrySecondaryDocuments.from_dict(docket_entry_secondary_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


