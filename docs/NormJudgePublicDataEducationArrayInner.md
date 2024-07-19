# NormJudgePublicDataEducationArrayInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**degree** | **str** | The Degree Awarded to the Judge | 
**year** | **int** | The year when the degree was awarded. | 
**school** | **str** | The University which awarded the degree to the Judge. | 

## Example

```python
from unicourt.models.norm_judge_public_data_education_array_inner import NormJudgePublicDataEducationArrayInner

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgePublicDataEducationArrayInner from a JSON string
norm_judge_public_data_education_array_inner_instance = NormJudgePublicDataEducationArrayInner.from_json(json)
# print the JSON string representation of the object
print(NormJudgePublicDataEducationArrayInner.to_json())

# convert the object into a dict
norm_judge_public_data_education_array_inner_dict = norm_judge_public_data_education_array_inner_instance.to_dict()
# create an instance of NormJudgePublicDataEducationArrayInner from a dict
norm_judge_public_data_education_array_inner_from_dict = NormJudgePublicDataEducationArrayInner.from_dict(norm_judge_public_data_education_array_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


