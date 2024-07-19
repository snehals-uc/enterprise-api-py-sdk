# JudgeAnalyticsAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'JudgeAnalyticsAPI']
**norm_judge_api** | **str** | Link to Details for the Judge. | 
**associated_norm_attorneys_api** | **str** |  | 
**associated_norm_law_firms_api** | **str** |  | 
**associated_norm_parties_api** | **str** |  | 

## Example

```python
from unicourt.models.judge_analytics_api import JudgeAnalyticsAPI

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeAnalyticsAPI from a JSON string
judge_analytics_api_instance = JudgeAnalyticsAPI.from_json(json)
# print the JSON string representation of the object
print(JudgeAnalyticsAPI.to_json())

# convert the object into a dict
judge_analytics_api_dict = judge_analytics_api_instance.to_dict()
# create an instance of JudgeAnalyticsAPI from a dict
judge_analytics_api_from_dict = JudgeAnalyticsAPI.from_dict(judge_analytics_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


