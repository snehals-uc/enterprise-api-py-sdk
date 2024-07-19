# RawOrderedDataChild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_array** | [**List[RawOrderedDataChildChildArrayInner]**](RawOrderedDataChildChildArrayInner.md) | Any docket text that belongs to the main docket text is added in the child. | 
**lbl** | **str** | Label of the docket from the source. | 
**ord** | **int** | Structure order. | 
**val** | **str** | List of available addresses. | 

## Example

```python
from unicourt.models.raw_ordered_data_child import RawOrderedDataChild

# TODO update the JSON string below
json = "{}"
# create an instance of RawOrderedDataChild from a JSON string
raw_ordered_data_child_instance = RawOrderedDataChild.from_json(json)
# print the JSON string representation of the object
print(RawOrderedDataChild.to_json())

# convert the object into a dict
raw_ordered_data_child_dict = raw_ordered_data_child_instance.to_dict()
# create an instance of RawOrderedDataChild from a dict
raw_ordered_data_child_from_dict = RawOrderedDataChild.from_dict(raw_ordered_data_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


