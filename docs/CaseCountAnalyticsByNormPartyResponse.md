# CaseCountAnalyticsByNormPartyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByNormPartyResponse']
**results** | [**List[CaseCountAnalyticsByNormParty]**](CaseCountAnalyticsByNormParty.md) |  | 
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_norm_party_count** | **int** | Total no. of NormParty for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_norm_party_response import CaseCountAnalyticsByNormPartyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByNormPartyResponse from a JSON string
case_count_analytics_by_norm_party_response_instance = CaseCountAnalyticsByNormPartyResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByNormPartyResponse.to_json())

# convert the object into a dict
case_count_analytics_by_norm_party_response_dict = case_count_analytics_by_norm_party_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByNormPartyResponse from a dict
case_count_analytics_by_norm_party_response_from_dict = CaseCountAnalyticsByNormPartyResponse.from_dict(case_count_analytics_by_norm_party_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


