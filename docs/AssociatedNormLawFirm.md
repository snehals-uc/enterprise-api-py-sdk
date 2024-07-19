# AssociatedNormLawFirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AssociatedNormLawFirm']
**norm_law_firm_id** | **str** |  | 
**norm_law_firm_api** | **str** | Link to Details for this Law Firm. | 
**case_timeline** | [**CaseTimeline**](CaseTimeline.md) |  | 
**name** | **str** |  | 
**case_search_api** | **str** | Link to related cases for this association. | 
**case_count** | **int** |  | 
**sos_data_array** | [**List[SOSDataPreview]**](SOSDataPreview.md) |  | 

## Example

```python
from unicourt.models.associated_norm_law_firm import AssociatedNormLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormLawFirm from a JSON string
associated_norm_law_firm_instance = AssociatedNormLawFirm.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormLawFirm.to_json())

# convert the object into a dict
associated_norm_law_firm_dict = associated_norm_law_firm_instance.to_dict()
# create an instance of AssociatedNormLawFirm from a dict
associated_norm_law_firm_from_dict = AssociatedNormLawFirm.from_dict(associated_norm_law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


