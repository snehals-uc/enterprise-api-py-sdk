# CaseUpdateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseUpdateListResponse']
**total_pages** | **int** | Total number of pages available. | 
**total_count** | **int** | Total number of case update objects available. | 
**page_number** | **int** | Current page number. | 
**next_page_api** | **str** | Link for the next page. | 
**previous_page_api** | **str** | Link for the previous page. | 
**case_update_preview_array** | [**List[CaseUpdatePreview]**](CaseUpdatePreview.md) | Array of case update objects. | 

## Example

```python
from unicourt.models.case_update_list_response import CaseUpdateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdateListResponse from a JSON string
case_update_list_response_instance = CaseUpdateListResponse.from_json(json)
# print the JSON string representation of the object
print(CaseUpdateListResponse.to_json())

# convert the object into a dict
case_update_list_response_dict = case_update_list_response_instance.to_dict()
# create an instance of CaseUpdateListResponse from a dict
case_update_list_response_from_dict = CaseUpdateListResponse.from_dict(case_update_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


