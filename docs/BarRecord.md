# BarRecord

This contains the Attorney details that is obtained from the State Bar where the attorney is registered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'BarRecord']
**bar_number** | **str** |  | 
**bar_source_type** | **str** |  | 
**admitted_date** | **datetime** | The admittedDate is the date when an attorney was admitted to the bar of a given state. | 
**state_code** | **str** |  | 
**status** | **str** |  | 
**inactivation_date** | **datetime** |  | 
**bar_source_data** | [**BarSourceData**](BarSourceData.md) |  | 
**contact** | [**Contact**](Contact.md) |  | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**last_fetch_date_with_updates** | **datetime** | Last Fetch Date of the Attorney Update. | 

## Example

```python
from unicourt.models.bar_record import BarRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BarRecord from a JSON string
bar_record_instance = BarRecord.from_json(json)
# print the JSON string representation of the object
print(BarRecord.to_json())

# convert the object into a dict
bar_record_dict = bar_record_instance.to_dict()
# create an instance of BarRecord from a dict
bar_record_from_dict = BarRecord.from_dict(bar_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


