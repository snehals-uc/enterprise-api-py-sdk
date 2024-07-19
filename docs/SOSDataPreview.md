# SOSDataPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'SOSDataPreview']
**sos_number** | **str** |  | 
**state_code** | **str** |  | 

## Example

```python
from unicourt.models.sos_data_preview import SOSDataPreview

# TODO update the JSON string below
json = "{}"
# create an instance of SOSDataPreview from a JSON string
sos_data_preview_instance = SOSDataPreview.from_json(json)
# print the JSON string representation of the object
print(SOSDataPreview.to_json())

# convert the object into a dict
sos_data_preview_dict = sos_data_preview_instance.to_dict()
# create an instance of SOSDataPreview from a dict
sos_data_preview_from_dict = SOSDataPreview.from_dict(sos_data_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


