# ServiceHistory

A timeline of courts where the judge has been employed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ServiceHistory']
**appointed_by** | **str** | The President-in-charge of the Judges appointment. | 
**reason_for_termination** | **str** | The reason for the Judges termination for the current position. | 
**source_court** | **str** | The court served by the Judge. The court is taken from source. | 
**title** | **str** | Title held by the Judge. | 
**from_year** | **int** | The year in which the Judge began practicing in his current service. | 
**to_year** | **int** | The year in which the Judge stoped practicing in his current service. | 
**from_date** | **datetime** | The year in which the Judge began practicing in his current service. | 
**to_date** | **datetime** | The year in which the Judge stoped practicing in his current service. | 
**is_visible** | **bool** | Boolean indicating if the service history  is visible or not. | 

## Example

```python
from unicourt.models.service_history import ServiceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceHistory from a JSON string
service_history_instance = ServiceHistory.from_json(json)
# print the JSON string representation of the object
print(ServiceHistory.to_json())

# convert the object into a dict
service_history_dict = service_history_instance.to_dict()
# create an instance of ServiceHistory from a dict
service_history_from_dict = ServiceHistory.from_dict(service_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


