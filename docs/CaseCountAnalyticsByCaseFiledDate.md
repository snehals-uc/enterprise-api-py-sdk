# CaseCountAnalyticsByCaseFiledDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseCountAnalyticsByCaseFiledDate']
**case_count** | **int** |  | 
**case_search_api** | **str** | Link to cases for this criteria. | 
**grouped_by** | **str** |  | [default to 'Yearly']
**year** | **int** |  | 
**quarter** | **str** |  | 
**month_string** | **str** |  | 
**month_int** | **int** |  | 
**week_of_year** | **int** |  | 
**week_of_month** | **int** |  | 

## Example

```python
from unicourt.models.case_count_analytics_by_case_filed_date import CaseCountAnalyticsByCaseFiledDate

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountAnalyticsByCaseFiledDate from a JSON string
case_count_analytics_by_case_filed_date_instance = CaseCountAnalyticsByCaseFiledDate.from_json(json)
# print the JSON string representation of the object
print(CaseCountAnalyticsByCaseFiledDate.to_json())

# convert the object into a dict
case_count_analytics_by_case_filed_date_dict = case_count_analytics_by_case_filed_date_instance.to_dict()
# create an instance of CaseCountAnalyticsByCaseFiledDate from a dict
case_count_analytics_by_case_filed_date_from_dict = CaseCountAnalyticsByCaseFiledDate.from_dict(case_count_analytics_by_case_filed_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


