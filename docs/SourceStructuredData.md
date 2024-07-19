# SourceStructuredData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_ordered_data_array** | [**List[RawOrderedData]**](RawOrderedData.md) |  | 
**extracted_fields** | [**ExtractedFields**](ExtractedFields.md) |  | 

## Example

```python
from unicourt.models.source_structured_data import SourceStructuredData

# TODO update the JSON string below
json = "{}"
# create an instance of SourceStructuredData from a JSON string
source_structured_data_instance = SourceStructuredData.from_json(json)
# print the JSON string representation of the object
print(SourceStructuredData.to_json())

# convert the object into a dict
source_structured_data_dict = source_structured_data_instance.to_dict()
# create an instance of SourceStructuredData from a dict
source_structured_data_from_dict = SourceStructuredData.from_dict(source_structured_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


