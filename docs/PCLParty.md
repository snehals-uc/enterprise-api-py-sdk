# PCLParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PCLParty']
**page_number** | **int** | Page number for which results where obtained. | 
**pacer_receipt** | [**PACERSearchReceipt**](PACERSearchReceipt.md) |  | 
**pacer_page_info** | [**PACERSearchPageInfo**](PACERSearchPageInfo.md) |  | 
**pacer_search_results_array** | [**List[PACERPartySearchResults]**](PACERPartySearchResults.md) |  | 
**next_page_api** | **str** | Link to next page of the PCL Search Results. | 
**total_pages** | **int** | Total number of pages to obtain all the objects the current PCL Search. | 
**total_count** | **int** | Total number of records available for this Search. | 

## Example

```python
from unicourt.models.pcl_party import PCLParty

# TODO update the JSON string below
json = "{}"
# create an instance of PCLParty from a JSON string
pcl_party_instance = PCLParty.from_json(json)
# print the JSON string representation of the object
print(PCLParty.to_json())

# convert the object into a dict
pcl_party_dict = pcl_party_instance.to_dict()
# create an instance of PCLParty from a dict
pcl_party_from_dict = PCLParty.from_dict(pcl_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


