# LastTrackedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'LastTrackedDetails']
**pacer_options** | [**CaseUpdatePacerOptionsResponse**](CaseUpdatePacerOptionsResponse.md) |  | 
**last_track_date** | **datetime** | The date and time when the case was tracked for this account. | 
**last_track_exception** | [**Exception**](Exception.md) |  | 

## Example

```python
from unicourt.models.last_tracked_details import LastTrackedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LastTrackedDetails from a JSON string
last_tracked_details_instance = LastTrackedDetails.from_json(json)
# print the JSON string representation of the object
print(LastTrackedDetails.to_json())

# convert the object into a dict
last_tracked_details_dict = last_tracked_details_instance.to_dict()
# create an instance of LastTrackedDetails from a dict
last_tracked_details_from_dict = LastTrackedDetails.from_dict(last_tracked_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


