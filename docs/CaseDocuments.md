# CaseDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'CaseDocuments']
**page_number** | **int** | Page number for which results where obtained. | 
**case_document_array** | [**List[CaseDocument]**](CaseDocument.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.case_documents import CaseDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDocuments from a JSON string
case_documents_instance = CaseDocuments.from_json(json)
# print the JSON string representation of the object
print(CaseDocuments.to_json())

# convert the object into a dict
case_documents_dict = case_documents_instance.to_dict()
# create an instance of CaseDocuments from a dict
case_documents_from_dict = CaseDocuments.from_dict(case_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


