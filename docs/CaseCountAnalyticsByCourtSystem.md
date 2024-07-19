# CaseCountAnalyticsByCourtSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourtSystem']
**case_count** | **int** |  | 
**case_search_api** | **str** | link to cases for this criteria. | 
**court_system** | [**CourtSystem**](CourtSystem.md) |  | 
**geo** | [**CaseCountAnalyticsByCourtGeo**](CaseCountAnalyticsByCourtGeo.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_court_system import CaseCountAnalyticsByCourtSystem

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourtSystem from a JSON string
case_count_analytics_by_court_system_instance = CaseCountAnalyticsByCourtSystem.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourtSystem.to_json())

# convert the object into a dict
case_count_analytics_by_court_system_dict = case_count_analytics_by_court_system_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourtSystem from a dict
case_count_analytics_by_court_system_from_dict = CaseCountAnalyticsByCourtSystem.from_dict(case_count_analytics_by_court_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


