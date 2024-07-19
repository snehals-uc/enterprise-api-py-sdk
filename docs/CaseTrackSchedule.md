# CaseTrackSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**days** | **List[int]** | [] -&gt; if schedule type is daily &lt;br&gt; 1-7 -&gt; if schedule type is weekly &lt;br&gt; 1-31 -&gt; if schedule type is monthly  | 

## Example

```python
from unicourt.models.case_track_schedule import CaseTrackSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTrackSchedule from a JSON string
case_track_schedule_instance = CaseTrackSchedule.from_json(json)
# print the JSON string representation of the object
print(CaseTrackSchedule.to_json())

# convert the object into a dict
case_track_schedule_dict = case_track_schedule_instance.to_dict()
# create an instance of CaseTrackSchedule from a dict
case_track_schedule_from_dict = CaseTrackSchedule.from_dict(case_track_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


