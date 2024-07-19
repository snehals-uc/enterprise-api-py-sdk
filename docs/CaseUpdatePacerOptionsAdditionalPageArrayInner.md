# CaseUpdatePacerOptionsAdditionalPageArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **str** |  | [optional] 
**fetch_if_older_than_days** | **int** | You can limit how often this page information is fetched to reduce your PACER fees.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that this page is fetched from PACER for this case update irrespective of when the page was last fetched. 2.  Specifying a value of 30 ensures that this page is fetched from PACER for this case update only if the last fetch was older than 30 days.  | [optional] [default to 0]

## Example

```python
from unicourt.models.case_update_pacer_options_additional_page_array_inner import CaseUpdatePacerOptionsAdditionalPageArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdatePacerOptionsAdditionalPageArrayInner from a JSON string
case_update_pacer_options_additional_page_array_inner_instance = CaseUpdatePacerOptionsAdditionalPageArrayInner.from_json(json)
# print the JSON string representation of the object
print(CaseUpdatePacerOptionsAdditionalPageArrayInner.to_json())

# convert the object into a dict
case_update_pacer_options_additional_page_array_inner_dict = case_update_pacer_options_additional_page_array_inner_instance.to_dict()
# create an instance of CaseUpdatePacerOptionsAdditionalPageArrayInner from a dict
case_update_pacer_options_additional_page_array_inner_from_dict = CaseUpdatePacerOptionsAdditionalPageArrayInner.from_dict(case_update_pacer_options_additional_page_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


