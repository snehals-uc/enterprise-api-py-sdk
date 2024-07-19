# CaseCountAnalyticsByCourtLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourtLocation']
**case_count** | **int** |  | 
**case_search_api** | **str** | link to cases for this criteria. | 
**court_location** | [**CourtLocation**](CourtLocation.md) |  | 
**court** | [**Court**](Court.md) |  | 
**geo** | [**CaseCountAnalyticsByCourtGeo**](CaseCountAnalyticsByCourtGeo.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_court_location import CaseCountAnalyticsByCourtLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourtLocation from a JSON string
case_count_analytics_by_court_location_instance = CaseCountAnalyticsByCourtLocation.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourtLocation.to_json())

# convert the object into a dict
case_count_analytics_by_court_location_dict = case_count_analytics_by_court_location_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourtLocation from a dict
case_count_analytics_by_court_location_from_dict = CaseCountAnalyticsByCourtLocation.from_dict(case_count_analytics_by_court_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


