# NormJudgePublicDataAbaRatings

American Bar Association (ABA) Rating of the Judge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **str** | rating | 
**year** | **int** | Year when Rating was recieved. | 

## Example

```python
from unicourt.models.norm_judge_public_data_aba_ratings import NormJudgePublicDataAbaRatings

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgePublicDataAbaRatings from a JSON string
norm_judge_public_data_aba_ratings_instance = NormJudgePublicDataAbaRatings.from_json(json)
# print the JSON string representation of the object
print(NormJudgePublicDataAbaRatings.to_json())

# convert the object into a dict
norm_judge_public_data_aba_ratings_dict = norm_judge_public_data_aba_ratings_instance.to_dict()
# create an instance of NormJudgePublicDataAbaRatings from a dict
norm_judge_public_data_aba_ratings_from_dict = NormJudgePublicDataAbaRatings.from_dict(norm_judge_public_data_aba_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


