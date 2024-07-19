# CaseCountAnalyticsByCourtLocationResponse

Case Counts by Court Location Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourtLocationResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByCourtLocation]**](CaseCountAnalyticsByCourtLocation.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_court_location_count** | **int** | Total no. of Court Location for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_court_location_response import CaseCountAnalyticsByCourtLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourtLocationResponse from a JSON string
case_count_analytics_by_court_location_response_instance = CaseCountAnalyticsByCourtLocationResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourtLocationResponse.to_json())

# convert the object into a dict
case_count_analytics_by_court_location_response_dict = case_count_analytics_by_court_location_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourtLocationResponse from a dict
case_count_analytics_by_court_location_response_from_dict = CaseCountAnalyticsByCourtLocationResponse.from_dict(case_count_analytics_by_court_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


