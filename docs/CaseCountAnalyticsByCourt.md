# CaseCountAnalyticsByCourt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCourt']
**case_count** | **int** |  | 
**case_search_api** | **str** | link to cases for this criteria. | 
**court** | [**Court**](Court.md) |  | 
**geo** | [**CaseCountAnalyticsByCourtGeo**](CaseCountAnalyticsByCourtGeo.md) |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_court import CaseCountAnalyticsByCourt

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCourt from a JSON string
case_count_analytics_by_court_instance = CaseCountAnalyticsByCourt.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCourt.to_json())

# convert the object into a dict
case_count_analytics_by_court_dict = case_count_analytics_by_court_instance.to_dict()
# create an instance of CaseCountAnalyticsByCourt from a dict
case_count_analytics_by_court_from_dict = CaseCountAnalyticsByCourt.from_dict(case_count_analytics_by_court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


