# BarSourceDataName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**prefix** | **str** |  | 
**suffix** | **str** |  | 

## Example

```python
from unicourt.models.bar_source_data_name import BarSourceDataName

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataName from a JSON string
bar_source_data_name_instance = BarSourceDataName.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataName.to_json())

# convert the object into a dict
bar_source_data_name_dict = bar_source_data_name_instance.to_dict()
# create an instance of BarSourceDataName from a dict
bar_source_data_name_from_dict = BarSourceDataName.from_dict(bar_source_data_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


