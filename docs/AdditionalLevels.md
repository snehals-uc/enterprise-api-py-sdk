# AdditionalLevels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AdditionalLevels']
**level1** | **str** |  | 
**level2** | **str** |  | 
**level3** | **str** |  | 
**level4** | **str** |  | 

## Example

```python
from unicourt.models.additional_levels import AdditionalLevels

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalLevels from a JSON string
additional_levels_instance = AdditionalLevels.from_json(json)
# print the JSON string representation of the object
print(AdditionalLevels.to_json())

# convert the object into a dict
additional_levels_dict = additional_levels_instance.to_dict()
# create an instance of AdditionalLevels from a dict
additional_levels_from_dict = AdditionalLevels.from_dict(additional_levels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


