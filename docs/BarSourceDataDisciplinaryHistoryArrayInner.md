# BarSourceDataDisciplinaryHistoryArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**case_number** | **str** |  | 
**complaint** | **str** |  | 
**contact_id** | **str** |  | 
**date_of_action** | **datetime** |  | 
**definition** | **str** |  | 
**disciplinary_decision** | **str** |  | 
**entry_date** | **datetime** |  | 
**information** | **str** |  | 
**link** | **str** |  | 
**note** | **str** |  | 
**probation_date** | **datetime** |  | 
**reinstated_date** | **datetime** |  | 
**rule** | **str** |  | 
**rule_number** | **str** |  | 
**section_date** | **datetime** |  | 
**status** | **str** |  | 
**stay_date** | **datetime** |  | 
**supreme_court** | **str** |  | 
**term** | **str** |  | 
**type_of_action** | **str** |  | 

## Example

```python
from unicourt.models.bar_source_data_disciplinary_history_array_inner import BarSourceDataDisciplinaryHistoryArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataDisciplinaryHistoryArrayInner from a JSON string
bar_source_data_disciplinary_history_array_inner_instance = BarSourceDataDisciplinaryHistoryArrayInner.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataDisciplinaryHistoryArrayInner.to_json())

# convert the object into a dict
bar_source_data_disciplinary_history_array_inner_dict = bar_source_data_disciplinary_history_array_inner_instance.to_dict()
# create an instance of BarSourceDataDisciplinaryHistoryArrayInner from a dict
bar_source_data_disciplinary_history_array_inner_from_dict = BarSourceDataDisciplinaryHistoryArrayInner.from_dict(bar_source_data_disciplinary_history_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


