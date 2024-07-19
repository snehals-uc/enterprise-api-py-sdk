# Success

Success object contains its message related to the API request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Success']
**message** | **str** | A message indicating that the request was successful. | 

## Example

```python
from unicourt.models.success import Success

# TODO update the JSON string below
json = "{}"
# create an instance of Success from a JSON string
success_instance = Success.from_json(json)
# print the JSON string representation of the object
print(Success.to_json())

# convert the object into a dict
success_dict = success_instance.to_dict()
# create an instance of Success from a dict
success_from_dict = Success.from_dict(success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


