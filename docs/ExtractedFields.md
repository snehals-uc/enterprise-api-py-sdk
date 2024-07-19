# ExtractedFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | This can be an field that is extracted from rawOrderedDataArray on request of different users. | [optional] 

## Example

```python
from unicourt.models.extracted_fields import ExtractedFields

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractedFields from a JSON string
extracted_fields_instance = ExtractedFields.from_json(json)
# print the JSON string representation of the object
print(ExtractedFields.to_json())

# convert the object into a dict
extracted_fields_dict = extracted_fields_instance.to_dict()
# create an instance of ExtractedFields from a dict
extracted_fields_from_dict = ExtractedFields.from_dict(extracted_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


