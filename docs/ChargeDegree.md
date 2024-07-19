# ChargeDegree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeDegree']
**charge_degree_id** | **str** |  | 
**name** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.charge_degree import ChargeDegree

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeDegree from a JSON string
charge_degree_instance = ChargeDegree.from_json(json)
# print the JSON string representation of the object
print(ChargeDegree.to_json())

# convert the object into a dict
charge_degree_dict = charge_degree_instance.to_dict()
# create an instance of ChargeDegree from a dict
charge_degree_from_dict = ChargeDegree.from_dict(charge_degree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


