# BarRecordPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'BarRecordPreview']
**bar_source_type** | **str** |  | 
**bar_number** | **str** |  | 
**state_code** | **str** |  | 

## Example

```python
from unicourt.models.bar_record_preview import BarRecordPreview

# TODO update the JSON string below
json = "{}"
# create an instance of BarRecordPreview from a JSON string
bar_record_preview_instance = BarRecordPreview.from_json(json)
# print the JSON string representation of the object
print(BarRecordPreview.to_json())

# convert the object into a dict
bar_record_preview_dict = bar_record_preview_instance.to_dict()
# create an instance of BarRecordPreview from a dict
bar_record_preview_from_dict = BarRecordPreview.from_dict(bar_record_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


