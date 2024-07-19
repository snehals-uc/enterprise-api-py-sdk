# PCLCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PCLCase']
**page_number** | **int** | Page number for which results where obtained. | 
**pacer_receipt** | [**PACERSearchReceipt**](PACERSearchReceipt.md) |  | 
**pacer_page_info** | [**PACERSearchPageInfo**](PACERSearchPageInfo.md) |  | 
**pacer_search_results_array** | [**List[PACERCaseSearchResults]**](PACERCaseSearchResults.md) |  | 
**next_page_api** | **str** | Link to next page of the PCL Search Results. | 
**total_pages** | **int** | Total number of pages to obtain all the objects the current PCL Search. | 
**total_count** | **int** | Total number of records available for this Search. | 

## Example

```python
from unicourt.models.pcl_case import PCLCase

# TODO update the JSON string below
json = "{}"
# create an instance of PCLCase from a JSON string
pcl_case_instance = PCLCase.from_json(json)
# print the JSON string representation of the object
print(PCLCase.to_json())

# convert the object into a dict
pcl_case_dict = pcl_case_instance.to_dict()
# create an instance of PCLCase from a dict
pcl_case_from_dict = PCLCase.from_dict(pcl_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


