# CaseCountAnalyticsByJurisdictionGeoResponse

Case Counts by Juridiction Geo Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByJurisdictionGeoResponse']
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**results** | [**List[CaseCountAnalyticsByJurisdictionGeo]**](CaseCountAnalyticsByJurisdictionGeo.md) |  | 
**total_pages** | **int** | Total no. of pages. | 
**total_case_count** | **int** | Total no. of Cases for this criteria. | 
**total_jurisdiction_geo_count** | **int** | Total no. of Jurisdiction for this criteria. | 

## Example

```python
from unicourt.models.case_count_analytics_by_jurisdiction_geo_response import CaseCountAnalyticsByJurisdictionGeoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByJurisdictionGeoResponse from a JSON string
case_count_analytics_by_jurisdiction_geo_response_instance = CaseCountAnalyticsByJurisdictionGeoResponse.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByJurisdictionGeoResponse.to_json())

# convert the object into a dict
case_count_analytics_by_jurisdiction_geo_response_dict = case_count_analytics_by_jurisdiction_geo_response_instance.to_dict()
# create an instance of CaseCountAnalyticsByJurisdictionGeoResponse from a dict
case_count_analytics_by_jurisdiction_geo_response_from_dict = CaseCountAnalyticsByJurisdictionGeoResponse.from_dict(case_count_analytics_by_jurisdiction_geo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


