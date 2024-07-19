# AssociatedNormParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AssociatedNormParty']
**norm_party_id** | **str** |  | 
**norm_party_api** | **str** | Link to Details for the Party. | 
**case_timeline** | [**CaseTimeline**](CaseTimeline.md) |  | 
**name** | **str** |  | 
**case_search_api** | **str** | Link to related cases for this association. | 
**case_count** | **int** |  | 
**sos_data_array** | [**List[SOSDataPreview]**](SOSDataPreview.md) |  | 

## Example

```python
from unicourt.models.associated_norm_party import AssociatedNormParty

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormParty from a JSON string
associated_norm_party_instance = AssociatedNormParty.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormParty.to_json())

# convert the object into a dict
associated_norm_party_dict = associated_norm_party_instance.to_dict()
# create an instance of AssociatedNormParty from a dict
associated_norm_party_from_dict = AssociatedNormParty.from_dict(associated_norm_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


