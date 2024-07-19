# SOSNameChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'SOSNameChange']
**name** | **str** |  | 
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 

## Example

```python
from unicourt.models.sos_name_change import SOSNameChange

# TODO update the JSON string below
json = "{}"
# create an instance of SOSNameChange from a JSON string
sos_name_change_instance = SOSNameChange.from_json(json)
# print the JSON string representation of the object
print(SOSNameChange.to_json())

# convert the object into a dict
sos_name_change_dict = sos_name_change_instance.to_dict()
# create an instance of SOSNameChange from a dict
sos_name_change_from_dict = SOSNameChange.from_dict(sos_name_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


