# PreviewDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PreviewDocument']
**in_library** | **bool** | Determines if the preview document is present in the UniCourt Library or not. | 
**added_to_library_date** | **str** | Date and time when the preview document was downloaded and added to the UniCourt CrowdSourced Library. | 
**download_api** | **str** | Link to get the file url for the preview document which is already present in the UniCourt CrowdSourced Library. | 

## Example

```python
from unicourt.models.preview_document import PreviewDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewDocument from a JSON string
preview_document_instance = PreviewDocument.from_json(json)
# print the JSON string representation of the object
print(PreviewDocument.to_json())

# convert the object into a dict
preview_document_dict = preview_document_instance.to_dict()
# create an instance of PreviewDocument from a dict
preview_document_from_dict = PreviewDocument.from_dict(preview_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


