# DocketEntries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'DocketEntries']
**page_number** | **int** | Page number for which results where obtained. | 
**docket_entry_array** | [**List[DocketEntry]**](DocketEntry.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.docket_entries import DocketEntries

# TODO update the JSON string below
json = "{}"
# create an instance of DocketEntries from a JSON string
docket_entries_instance = DocketEntries.from_json(json)
# print the JSON string representation of the object
print(DocketEntries.to_json())

# convert the object into a dict
docket_entries_dict = docket_entries_instance.to_dict()
# create an instance of DocketEntries from a dict
docket_entries_from_dict = DocketEntries.from_dict(docket_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


