# ChargeAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeAdditionalData']
**charge_additional_data_id** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 

## Example

```python
from unicourt.models.charge_additional_data import ChargeAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeAdditionalData from a JSON string
charge_additional_data_instance = ChargeAdditionalData.from_json(json)
# print the JSON string representation of the object
print(ChargeAdditionalData.to_json())

# convert the object into a dict
charge_additional_data_dict = charge_additional_data_instance.to_dict()
# create an instance of ChargeAdditionalData from a dict
charge_additional_data_from_dict = ChargeAdditionalData.from_dict(charge_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


