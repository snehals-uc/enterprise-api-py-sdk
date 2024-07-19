# Charge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Charge']
**charge_id** | **str** |  | 
**charge_group_id** | **str** |  | 
**charge_group** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.charge import Charge

# TODO update the JSON string below
json = "{}"
# create an instance of Charge from a JSON string
charge_instance = Charge.from_json(json)
# print the JSON string representation of the object
print(Charge.to_json())

# convert the object into a dict
charge_dict = charge_instance.to_dict()
# create an instance of Charge from a dict
charge_from_dict = Charge.from_dict(charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


