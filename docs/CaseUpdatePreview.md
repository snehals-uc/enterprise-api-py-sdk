# CaseUpdatePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseUpdatePreview']
**case_id** | **str** | Unique Id for a Case in UniCourt. | 
**status** | **str** | Status of the request. | 
**requested_date** | **datetime** | The date and time when the case was last requested for update  | 
**case_api** | **str** |  | 
**pacer_options** | [**CaseUpdatePacerOptionsResponse**](CaseUpdatePacerOptionsResponse.md) |  | 
**exception** | [**Exception**](Exception.md) |  | 

## Example

```python
from unicourt.models.case_update_preview import CaseUpdatePreview

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdatePreview from a JSON string
case_update_preview_instance = CaseUpdatePreview.from_json(json)
# print the JSON string representation of the object
print(CaseUpdatePreview.to_json())

# convert the object into a dict
case_update_preview_dict = case_update_preview_instance.to_dict()
# create an instance of CaseUpdatePreview from a dict
case_update_preview_from_dict = CaseUpdatePreview.from_dict(case_update_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


