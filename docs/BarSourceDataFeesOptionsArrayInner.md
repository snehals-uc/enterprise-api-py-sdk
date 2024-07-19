# BarSourceDataFeesOptionsArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_fees** | **str** |  | 
**flat_fees** | **str** |  | 
**hourly_rate** | **str** |  | 
**payment_plans** | **str** |  | 
**sliding_scale_fees** | **str** |  | 

## Example

```python
from unicourt.models.bar_source_data_fees_options_array_inner import BarSourceDataFeesOptionsArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataFeesOptionsArrayInner from a JSON string
bar_source_data_fees_options_array_inner_instance = BarSourceDataFeesOptionsArrayInner.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataFeesOptionsArrayInner.to_json())

# convert the object into a dict
bar_source_data_fees_options_array_inner_dict = bar_source_data_fees_options_array_inner_instance.to_dict()
# create an instance of BarSourceDataFeesOptionsArrayInner from a dict
bar_source_data_fees_options_array_inner_from_dict = BarSourceDataFeesOptionsArrayInner.from_dict(bar_source_data_fees_options_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


