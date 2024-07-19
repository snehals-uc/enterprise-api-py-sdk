# NormJudgePublicDataBio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ethnicity** | **str** | Ethnic Group of the Judge. | 
**birth_city** | **str** | The Birth City of the Judge. | 
**birth_date** | **datetime** | The Date of Birth of the Judge. | 
**birth_state** | **str** | The Birth State of the Judge. | 
**death_city** | **str** | The Death City of the Judge. | 
**death_date** | **datetime** | The Date of the Death of the Judge. | 
**death_state** | **str** | The Death State of the Judge. | 
**political_affiliation** | **str** | The Political Affiliation of the Judge. | 

## Example

```python
from unicourt.models.norm_judge_public_data_bio import NormJudgePublicDataBio

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgePublicDataBio from a JSON string
norm_judge_public_data_bio_instance = NormJudgePublicDataBio.from_json(json)
# print the JSON string representation of the object
print(NormJudgePublicDataBio.to_json())

# convert the object into a dict
norm_judge_public_data_bio_dict = norm_judge_public_data_bio_instance.to_dict()
# create an instance of NormJudgePublicDataBio from a dict
norm_judge_public_data_bio_from_dict = NormJudgePublicDataBio.from_dict(norm_judge_public_data_bio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


