# CaseCountAnalyticsByJurisdictionGeo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByJurisdictionGeo']
**case_count** | **int** |  | 
**case_search_api** | **str** | link to cases for this criteria. | 
**jurisdiction_geo** | [**JurisdictionGeo**](JurisdictionGeo.md) |  | 
**geo** | [**CaseCountAnalyticsByCourtGeo**](CaseCountAnalyticsByCourtGeo.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_jurisdiction_geo import CaseCountAnalyticsByJurisdictionGeo

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByJurisdictionGeo from a JSON string
case_count_analytics_by_jurisdiction_geo_instance = CaseCountAnalyticsByJurisdictionGeo.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByJurisdictionGeo.to_json())

# convert the object into a dict
case_count_analytics_by_jurisdiction_geo_dict = case_count_analytics_by_jurisdiction_geo_instance.to_dict()
# create an instance of CaseCountAnalyticsByJurisdictionGeo from a dict
case_count_analytics_by_jurisdiction_geo_from_dict = CaseCountAnalyticsByJurisdictionGeo.from_dict(case_count_analytics_by_jurisdiction_geo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


