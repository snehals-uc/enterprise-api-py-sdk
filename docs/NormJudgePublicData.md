# NormJudgePublicData

This contains the Judge Public details that is obtained from various sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'NormJudgePublicData']
**judicial_status** | **str** | The judicial status of the Judge | 
**judicial_source** | [**NormJudgePublicDataJudicialSource**](NormJudgePublicDataJudicialSource.md) |  | 
**aba_ratings** | [**NormJudgePublicDataAbaRatings**](NormJudgePublicDataAbaRatings.md) |  | 
**alias_array** | **List[str]** | Other Names of the Judge. | 
**bio** | [**NormJudgePublicDataBio**](NormJudgePublicDataBio.md) |  | 
**contact** | [**Contact**](Contact.md) |  | 
**education_array** | [**List[NormJudgePublicDataEducationArrayInner]**](NormJudgePublicDataEducationArrayInner.md) | The Education History of the judge. | 
**professional_career_array** | **List[str]** | The non-judicial career history of the judge. | 
**service_history_array** | [**List[ServiceHistory]**](ServiceHistory.md) | Judicial History of the Judge. | 
**name_history_array** | [**List[NormJudgePublicDataNameHistoryArrayInner]**](NormJudgePublicDataNameHistoryArrayInner.md) | Name changes of the Judge. Change in the official name. Other names go to Alias array. | 
**first_fetch_date** | **datetime** |  | 
**last_fetch_date** | **datetime** |  | 
**last_fetch_date_with_updates** | **datetime** | Last Fetch Date of the Judge Update. | 

## Example

```python
from unicourt.models.norm_judge_public_data import NormJudgePublicData

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgePublicData from a JSON string
norm_judge_public_data_instance = NormJudgePublicData.from_json(json)
# print the JSON string representation of the object
print(NormJudgePublicData.to_json())

# convert the object into a dict
norm_judge_public_data_dict = norm_judge_public_data_instance.to_dict()
# create an instance of NormJudgePublicData from a dict
norm_judge_public_data_from_dict = NormJudgePublicData.from_dict(norm_judge_public_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


