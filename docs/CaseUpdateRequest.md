# CaseUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** | UniCourt&#39;s Case Id for update. | 
**pacer_options** | [**CaseUpdatePacerOptions**](CaseUpdatePacerOptions.md) |  | [optional] 

## Example

```python
from unicourt.models.case_update_request import CaseUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdateRequest from a JSON string
case_update_request_instance = CaseUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CaseUpdateRequest.to_json())

# convert the object into a dict
case_update_request_dict = case_update_request_instance.to_dict()
# create an instance of CaseUpdateRequest from a dict
case_update_request_from_dict = CaseUpdateRequest.from_dict(case_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


