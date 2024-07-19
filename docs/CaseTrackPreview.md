# CaseTrackPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseTrackPreview']
**case_id** | **str** | Unique Id for a Case in UniCourt. | 
**pacer_options** | [**CaseUpdatePacerOptionsResponse**](CaseUpdatePacerOptionsResponse.md) |  | 
**schedule** | [**Schedule**](Schedule.md) |  | 
**last_tracked_details** | [**LastTrackedDetails**](LastTrackedDetails.md) |  | 
**last_fetch_date** | **datetime** | The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist. | 
**last_fetch_date_with_updates** | **datetime** | The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, | 
**case_api** | **str** |  | 

## Example

```python
from unicourt.models.case_track_preview import CaseTrackPreview

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTrackPreview from a JSON string
case_track_preview_instance = CaseTrackPreview.from_json(json)
# print the JSON string representation of the object
print(CaseTrackPreview.to_json())

# convert the object into a dict
case_track_preview_dict = case_track_preview_instance.to_dict()
# create an instance of CaseTrackPreview from a dict
case_track_preview_from_dict = CaseTrackPreview.from_dict(case_track_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


