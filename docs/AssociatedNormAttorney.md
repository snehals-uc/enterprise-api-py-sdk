# AssociatedNormAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AssociatedNormAttorney']
**norm_attorney_api** | **str** | Link to details for the Attorney. | 
**norm_attorney_id** | **str** |  | 
**case_timeline** | [**CaseTimeline**](CaseTimeline.md) |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**case_search_api** | **str** | Link to related cases for this association. | 
**case_count** | **int** |  | 
**state_bar_data_array** | [**List[BarRecordPreview]**](BarRecordPreview.md) |  | 

## Example

```python
from unicourt.models.associated_norm_attorney import AssociatedNormAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormAttorney from a JSON string
associated_norm_attorney_instance = AssociatedNormAttorney.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormAttorney.to_json())

# convert the object into a dict
associated_norm_attorney_dict = associated_norm_attorney_instance.to_dict()
# create an instance of AssociatedNormAttorney from a dict
associated_norm_attorney_from_dict = AssociatedNormAttorney.from_dict(associated_norm_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


