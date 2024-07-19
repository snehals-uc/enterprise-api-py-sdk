# CaseCountAnalyticsByCourtType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourtType']
**case_count** | **int** |  | 
**case_search_api** | **str** | link to cases for this criteria. | 
**court_type** | [**CourtType**](CourtType.md) |  | 
**geo** | [**CaseCountAnalyticsByCourtGeo**](CaseCountAnalyticsByCourtGeo.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_court_type import CaseCountAnalyticsByCourtType

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourtType from a JSON string
case_count_analytics_by_court_type_instance = CaseCountAnalyticsByCourtType.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourtType.to_json())

# convert the object into a dict
case_count_analytics_by_court_type_dict = case_count_analytics_by_court_type_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourtType from a dict
case_count_analytics_by_court_type_from_dict = CaseCountAnalyticsByCourtType.from_dict(case_count_analytics_by_court_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


