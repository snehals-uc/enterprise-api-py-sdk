# CaseTrackListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseTrackListResponse']
**total_pages** | **int** | Total number of pages available. | 
**total_count** | **int** | Total number of case track available. | 
**page_number** | **int** | Current page number. | 
**next_page_api** | **str** | Link for the next page. | 
**previous_page_api** | **str** | Link for the previous page. | 
**case_track_preview_array** | [**List[CaseTrackPreview]**](CaseTrackPreview.md) | Array of cases tracked. | 

## Example

```python
from unicourt.models.case_track_list_response import CaseTrackListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTrackListResponse from a JSON string
case_track_list_response_instance = CaseTrackListResponse.from_json(json)
# print the JSON string representation of the object
print(CaseTrackListResponse.to_json())

# convert the object into a dict
case_track_list_response_dict = case_track_list_response_instance.to_dict()
# create an instance of CaseTrackListResponse from a dict
case_track_list_response_from_dict = CaseTrackListResponse.from_dict(case_track_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


