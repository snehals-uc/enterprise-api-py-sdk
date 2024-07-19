# ChargeSeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeSeverity']
**charge_severity_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.charge_severity import ChargeSeverity

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeSeverity from a JSON string
charge_severity_instance = ChargeSeverity.from_json(json)
# print the JSON string representation of the object
print(ChargeSeverity.to_json())

# convert the object into a dict
charge_severity_dict = charge_severity_instance.to_dict()
# create an instance of ChargeSeverity from a dict
charge_severity_from_dict = ChargeSeverity.from_dict(charge_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


