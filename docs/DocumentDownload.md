# DocumentDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'DocumentDownload']
**case_document_id** | **str** | Requested Document ID. | 
**expiry_date** | **str** | Expiry date-time for the fileUrl provided in this object. | 
**file_url** | **str** | Link to download the file. | 
**case_document_download_api** | **str** | API call to download the document again if the above fileUrl is expired. | 
**exception** | [**Exception**](Exception.md) |  | 

## Example

```python
from unicourt.models.document_download import DocumentDownload

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDownload from a JSON string
document_download_instance = DocumentDownload.from_json(json)
# print the JSON string representation of the object
print(DocumentDownload.to_json())

# convert the object into a dict
document_download_dict = document_download_instance.to_dict()
# create an instance of DocumentDownload from a dict
document_download_from_dict = DocumentDownload.from_dict(document_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


