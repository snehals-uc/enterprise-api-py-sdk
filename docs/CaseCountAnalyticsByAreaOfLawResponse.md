# CaseCountAnalyticsByAreaOfLawResponse

Case Counts by Area Of Law Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByAreaOfLawResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByAreaOfLaw]**](CaseCountAnalyticsByAreaOfLaw.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_area_of_law_count** | **int** | Total no. of Area Of Law for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_area_of_law_response import CaseCountAnalyticsByAreaOfLawResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByAreaOfLawResponse from a JSON string
case_count_analytics_by_area_of_law_response_instance = CaseCountAnalyticsByAreaOfLawResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByAreaOfLawResponse.to_json())

# convert the object into a dict
case_count_analytics_by_area_of_law_response_dict = case_count_analytics_by_area_of_law_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByAreaOfLawResponse from a dict
case_count_analytics_by_area_of_law_response_from_dict = CaseCountAnalyticsByAreaOfLawResponse.from_dict(case_count_analytics_by_area_of_law_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


