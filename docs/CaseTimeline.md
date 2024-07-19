# CaseTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseTimeline']
**first_case_filed_date** | **datetime** | The first date when the two entities have appeared together in the case. (These dates are determined from case filed dates) | 
**last_case_filed_date** | **datetime** | The last date when the two entities have appeared together in the case. (These dates are determined from case filed dates) | 

## Example

```python
from unicourt.models.case_timeline import CaseTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTimeline from a JSON string
case_timeline_instance = CaseTimeline.from_json(json)
# print the JSON string representation of the object
print(CaseTimeline.to_json())

# convert the object into a dict
case_timeline_dict = case_timeline_instance.to_dict()
# create an instance of CaseTimeline from a dict
case_timeline_from_dict = CaseTimeline.from_dict(case_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


