# BarSourceDataStatusHistoryArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** |  | 
**status_change** | **str** |  | 

## Example

```python
from unicourt.models.bar_source_data_status_history_array_inner import BarSourceDataStatusHistoryArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataStatusHistoryArrayInner from a JSON string
bar_source_data_status_history_array_inner_instance = BarSourceDataStatusHistoryArrayInner.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataStatusHistoryArrayInner.to_json())

# convert the object into a dict
bar_source_data_status_history_array_inner_dict = bar_source_data_status_history_array_inner_instance.to_dict()
# create an instance of BarSourceDataStatusHistoryArrayInner from a dict
bar_source_data_status_history_array_inner_from_dict = BarSourceDataStatusHistoryArrayInner.from_dict(bar_source_data_status_history_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


