# RawOrderedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_array** | [**List[RawOrderedDataChild]**](RawOrderedDataChild.md) | Any docket text that belongs to the main docket text is added in the child. | 
**lbl** | **str** | Label of the docket from the source. | 
**ord** | **int** | Structure order | 
**val** | **str** | List of available addresses. | 

## Example

```python
from unicourt.models.raw_ordered_data import RawOrderedData

# TODO update the JSON string below
json = "{}"
# create an instance of RawOrderedData from a JSON string
raw_ordered_data_instance = RawOrderedData.from_json(json)
# print the JSON string representation of the object
print(RawOrderedData.to_json())

# convert the object into a dict
raw_ordered_data_dict = raw_ordered_data_instance.to_dict()
# create an instance of RawOrderedData from a dict
raw_ordered_data_from_dict = RawOrderedData.from_dict(raw_ordered_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


