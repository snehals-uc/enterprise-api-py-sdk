# PACERSearchPageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERSearchPageInfo']
**number** | **int** | Current Page number. | 
**size** | **int** | Number of results obtained in a page.. | 
**total_pages** | **int** | Total pages of data available. | 
**total_elements** | **int** | Total number of records available | 
**number_of_elements** | **int** | Number of records returned. | 
**first** | **bool** | Indicates if the current page is the first page. | 
**last** | **bool** | Indicates if the current page is the last page. | 

## Example

```python
from unicourt.models.pacer_search_page_info import PACERSearchPageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PACERSearchPageInfo from a JSON string
pacer_search_page_info_instance = PACERSearchPageInfo.from_json(json)
# print the JSON string representation of the object
print(PACERSearchPageInfo.to_json())

# convert the object into a dict
pacer_search_page_info_dict = pacer_search_page_info_instance.to_dict()
# create an instance of PACERSearchPageInfo from a dict
pacer_search_page_info_from_dict = PACERSearchPageInfo.from_dict(pacer_search_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


