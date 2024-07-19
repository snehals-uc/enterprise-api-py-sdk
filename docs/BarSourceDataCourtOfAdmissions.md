# BarSourceDataCourtOfAdmissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court_state_array** | **List[str]** |  | 
**federal_array** | **List[str]** |  | 
**other_courts_array** | **List[str]** |  | 

## Example

```python
from unicourt.models.bar_source_data_court_of_admissions import BarSourceDataCourtOfAdmissions

# TODO update the JSON string below
json = "{}"
# create an instance of BarSourceDataCourtOfAdmissions from a JSON string
bar_source_data_court_of_admissions_instance = BarSourceDataCourtOfAdmissions.from_json(json)
# print the JSON string representation of the object
print(BarSourceDataCourtOfAdmissions.to_json())

# convert the object into a dict
bar_source_data_court_of_admissions_dict = bar_source_data_court_of_admissions_instance.to_dict()
# create an instance of BarSourceDataCourtOfAdmissions from a dict
bar_source_data_court_of_admissions_from_dict = BarSourceDataCourtOfAdmissions.from_dict(bar_source_data_court_of_admissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


