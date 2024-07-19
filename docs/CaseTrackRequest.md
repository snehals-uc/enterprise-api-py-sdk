# CaseTrackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_track_params** | [**CaseUpdateRequest**](CaseUpdateRequest.md) |  | 
**schedule** | [**CaseTrackSchedule**](CaseTrackSchedule.md) |  | 

## Example

```python
from unicourt.models.case_track_request import CaseTrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTrackRequest from a JSON string
case_track_request_instance = CaseTrackRequest.from_json(json)
# print the JSON string representation of the object
print(CaseTrackRequest.to_json())

# convert the object into a dict
case_track_request_dict = case_track_request_instance.to_dict()
# create an instance of CaseTrackRequest from a dict
case_track_request_from_dict = CaseTrackRequest.from_dict(case_track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


