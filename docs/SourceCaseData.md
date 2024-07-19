# SourceCaseData

Source data in the court website.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'SourceCaseData']
**source_court** | **str** | Courtrhouse as provided by Court. | 
**source_case_type** | **str** | Case Type for a case which is provided by the Court. | 
**source_charge_array** | [**List[SourceCharge]**](SourceCharge.md) | Array of Charges for a case which is provided by the Court. | 
**nature_of_suit_array** | [**List[NatureOfSuit]**](NatureOfSuit.md) | Array of Charges for a case which is provided by the Court. | 
**source_cause_of_action_array** | [**List[SourceCauseOfAction]**](SourceCauseOfAction.md) | Array of Cause Of Action for a case which is provided by the Court. | 
**source_case_status** | **str** | Case Status as provided by Court. | 
**source_page_data** | [**List[SourcePageData]**](SourcePageData.md) |  | 

## Example

```python
from unicourt.models.source_case_data import SourceCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCaseData from a JSON string
source_case_data_instance = SourceCaseData.from_json(json)
# print the JSON string representation of the object
print(SourceCaseData.to_json())

# convert the object into a dict
source_case_data_dict = source_case_data_instance.to_dict()
# create an instance of SourceCaseData from a dict
source_case_data_from_dict = SourceCaseData.from_dict(source_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


