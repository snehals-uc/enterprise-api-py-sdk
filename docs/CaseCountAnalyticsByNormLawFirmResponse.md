# CaseCountAnalyticsByNormLawFirmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormLawFirmResponse']
**results** | [**List[CaseCountAnalyticsByNormLawFirm]**](CaseCountAnalyticsByNormLawFirm.md) |  | 
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_norm_law_firm_count** | **int** | Total no. of NormLawFirm for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_law_firm_response import CaseCountAnalyticsByNormLawFirmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormLawFirmResponse from a JSON string
case_count_analytics_by_norm_law_firm_response_instance = CaseCountAnalyticsByNormLawFirmResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormLawFirmResponse.to_json())

# convert the object into a dict
case_count_analytics_by_norm_law_firm_response_dict = case_count_analytics_by_norm_law_firm_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormLawFirmResponse from a dict
case_count_analytics_by_norm_law_firm_response_from_dict = CaseCountAnalyticsByNormLawFirmResponse.from_dict(case_count_analytics_by_norm_law_firm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


