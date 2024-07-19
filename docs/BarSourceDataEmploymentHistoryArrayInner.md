# BarSourceDataEmploymentHistoryArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer** | **str** |  | 
**end_date** | **datetime** |  | 
**start_date** | **datetime** |  | 

## Example

```python
from unicourt.models.bar_source_data_employment_history_array_inner import BarSourceDataEmploymentHistoryArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataEmploymentHistoryArrayInner from a JSON string
bar_source_data_employment_history_array_inner_instance = BarSourceDataEmploymentHistoryArrayInner.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataEmploymentHistoryArrayInner.to_json())

# convert the object into a dict
bar_source_data_employment_history_array_inner_dict = bar_source_data_employment_history_array_inner_instance.to_dict()
# create an instance of BarSourceDataEmploymentHistoryArrayInner from a dict
bar_source_data_employment_history_array_inner_from_dict = BarSourceDataEmploymentHistoryArrayInner.from_dict(bar_source_data_employment_history_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


