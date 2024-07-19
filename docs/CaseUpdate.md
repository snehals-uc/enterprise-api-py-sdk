# CaseUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object. | [default to 'CaseUpdate']
**case_id** | **str** | Unique Id for a Case in UniCourt. | 
**status** | **str** | Status of the request. | 
**requested_date** | **datetime** | The date and time when the case was last requested for update  | 
**case_api** | **str** |  | 
**pacer_options** | [**CaseUpdatePacerOptionsResponse**](CaseUpdatePacerOptionsResponse.md) |  | 
**exception** | [**Exception**](Exception.md) |  | 
**case** | [**Case**](Case.md) |  | 

## Example

```python
from unicourt.models.case_update import CaseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdate from a JSON string
case_update_instance = CaseUpdate.from_json(json)
# print the JSON string representation of the object
print(CaseUpdate.to_json())

# convert the object into a dict
case_update_dict = case_update_instance.to_dict()
# create an instance of CaseUpdate from a dict
case_update_from_dict = CaseUpdate.from_dict(case_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


