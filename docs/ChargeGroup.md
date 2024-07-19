# ChargeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeGroup']
**charge_group_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.charge_group import ChargeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeGroup from a JSON string
charge_group_instance = ChargeGroup.from_json(json)
# print the JSON string representation of the object
print(ChargeGroup.to_json())

# convert the object into a dict
charge_group_dict = charge_group_instance.to_dict()
# create an instance of ChargeGroup from a dict
charge_group_from_dict = ChargeGroup.from_dict(charge_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


