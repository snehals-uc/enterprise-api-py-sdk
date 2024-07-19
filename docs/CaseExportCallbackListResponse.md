# CaseExportCallbackListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseExportCallbackListResponse']
**total_pages** | **int** | Total number of pages available. | 
**total_count** | **int** | Total number of case export callback objects available. | 
**page_number** | **int** | Current page number. | 
**next_page_api** | **str** | Link for the next page. | 
**previous_page_api** | **str** | Link for the previous page. | 
**callback_array** | [**List[CaseExportCallback]**](CaseExportCallback.md) | Array of case export callback objects. | 

## Example

```python
from unicourt.models.case_export_callback_list_response import CaseExportCallbackListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseExportCallbackListResponse from a JSON string
case_export_callback_list_response_instance = CaseExportCallbackListResponse.from_json(json)
# print the JSON string representation of the object
print(CaseExportCallbackListResponse.to_json())

# convert the object into a dict
case_export_callback_list_response_dict = case_export_callback_list_response_instance.to_dict()
# create an instance of CaseExportCallbackListResponse from a dict
case_export_callback_list_response_from_dict = CaseExportCallbackListResponse.from_dict(case_export_callback_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


