# SourcePageData

Source data from different pages in the court website.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'SourcePageData']
**page_name** | **str** | Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases. | 
**additional_source_data** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**first_fetch_date** | **str** | When was the page first fetched from the court site. | 
**last_fetch_date** | **str** | When was the page last fetched from the court site. | 

## Example

```python
from unicourt.models.source_page_data import SourcePageData

# TODO update the JSON string below
json = "{}"
# create an instance of SourcePageData from a JSON string
source_page_data_instance = SourcePageData.from_json(json)
# print the JSON string representation of the object
print(SourcePageData.to_json())

# convert the object into a dict
source_page_data_dict = source_page_data_instance.to_dict()
# create an instance of SourcePageData from a dict
source_page_data_from_dict = SourcePageData.from_dict(source_page_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


