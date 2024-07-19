# RawOrderedDataChildChildArrayInner

Contact object Data Schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lbl** | **str** | Label of the docket from the source. | 
**ord** | **int** | Structure order. | 
**val** | **str** | List of available addresses. | 
**child_array** | **List[object]** |  | 

## Example

```python
from unicourt.models.raw_ordered_data_child_child_array_inner import RawOrderedDataChildChildArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of RawOrderedDataChildChildArrayInner from a JSON string
raw_ordered_data_child_child_array_inner_instance = RawOrderedDataChildChildArrayInner.from_json(json)
# print the JSON string representation of the object
print(RawOrderedDataChildChildArrayInner.to_json())

# convert the object into a dict
raw_ordered_data_child_child_array_inner_dict = raw_ordered_data_child_child_array_inner_instance.to_dict()
# create an instance of RawOrderedDataChildChildArrayInner from a dict
raw_ordered_data_child_child_array_inner_from_dict = RawOrderedDataChildChildArrayInner.from_dict(raw_ordered_data_child_child_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


