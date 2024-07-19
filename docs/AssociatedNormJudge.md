# AssociatedNormJudge

Associated Judge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AssociatedNormJudge']
**norm_judge_id** | **str** |  | 
**norm_judge_api** | **str** | Link to Details from the Judge. | 
**case_timeline** | [**CaseTimeline**](CaseTimeline.md) |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**middle_name** | **str** |  | 
**last_name** | **str** |  | 
**case_search_api** | **str** | Link to related cases for this association. | 
**case_count** | **int** |  | 
**version** | **str** |  | 

## Example

```python
from unicourt.models.associated_norm_judge import AssociatedNormJudge

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormJudge from a JSON string
associated_norm_judge_instance = AssociatedNormJudge.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormJudge.to_json())

# convert the object into a dict
associated_norm_judge_dict = associated_norm_judge_instance.to_dict()
# create an instance of AssociatedNormJudge from a dict
associated_norm_judge_from_dict = AssociatedNormJudge.from_dict(associated_norm_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


