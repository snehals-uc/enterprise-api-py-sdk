# MatchedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'MatchedObject']
**matched_object_id** | **str** |  | 
**matched_object_name** | **str** |  | 
**matched_object_attribute** | **str** |  | 
**highlight_snippet** | **str** |  | 
**matched_object_api** | **str** |  | 

## Example

```python
from unicourt.models.matched_object import MatchedObject

# TODO update the JSON string below
json = "{}"
# create an instance of MatchedObject from a JSON string
matched_object_instance = MatchedObject.from_json(json)
# print the JSON string representation of the object
print(MatchedObject.to_json())

# convert the object into a dict
matched_object_dict = matched_object_instance.to_dict()
# create an instance of MatchedObject from a dict
matched_object_from_dict = MatchedObject.from_dict(matched_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


