# BarSourceDataAdministrativeActionsArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_number** | **str** |  | 
**description** | **str** |  | 
**effective_date** | **datetime** |  | 
**resulting_status** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from unicourt.models.bar_source_data_administrative_actions_array_inner import BarSourceDataAdministrativeActionsArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataAdministrativeActionsArrayInner from a JSON string
bar_source_data_administrative_actions_array_inner_instance = BarSourceDataAdministrativeActionsArrayInner.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataAdministrativeActionsArrayInner.to_json())

# convert the object into a dict
bar_source_data_administrative_actions_array_inner_dict = bar_source_data_administrative_actions_array_inner_instance.to_dict()
# create an instance of BarSourceDataAdministrativeActionsArrayInner from a dict
bar_source_data_administrative_actions_array_inner_from_dict = BarSourceDataAdministrativeActionsArrayInner.from_dict(bar_source_data_administrative_actions_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


