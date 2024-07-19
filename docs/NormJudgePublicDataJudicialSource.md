# NormJudgePublicDataJudicialSource

The judicial source of the Judge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Judicial Data Source | 
**type** | **str** | Type of acquisition of the data source | 
**url** | **str** | URL of the data source, if type is Website | 

## Example

```python
from unicourt.models.norm_judge_public_data_judicial_source import NormJudgePublicDataJudicialSource

# TODO update the JSON string below
json = "{}"
# create an instance of NormJudgePublicDataJudicialSource from a JSON string
norm_judge_public_data_judicial_source_instance = NormJudgePublicDataJudicialSource.from_json(json)
# print the JSON string representation of the object
print(NormJudgePublicDataJudicialSource.to_json())

# convert the object into a dict
norm_judge_public_data_judicial_source_dict = norm_judge_public_data_judicial_source_instance.to_dict()
# create an instance of NormJudgePublicDataJudicialSource from a dict
norm_judge_public_data_judicial_source_from_dict = NormJudgePublicDataJudicialSource.from_dict(norm_judge_public_data_judicial_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


