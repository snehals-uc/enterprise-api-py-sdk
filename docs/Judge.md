# Judge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Judge']
**judge_id** | **str** | ID for the judge in this case. This ID is unique within a case and NOT across cases. If the same Judge were to appear in another case this ID would be different. | 
**name** | **str** | Name of the judge as provided by Court. | 
**name_prefix** | **str** |  | 
**first_name** | **str** | First name of the judge. This is normalized by UniCourt. | 
**middle_name** | **str** | Middle name of the judge. This is normalized by UniCourt. | 
**last_name** | **str** | Last name of the judge. This is normalized by UniCourt. | 
**name_suffix** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**judge_type** | [**JudgeType**](JudgeType.md) |  | 
**source_judge_type** | **str** |  | 
**is_visible** | **bool** | Signifies if the judge as this judge type is currently isVisible or not for the case. | 
**first_fetch_date** | **datetime** | When was the judge first fetched from the court site. | 
**last_fetch_date** | **datetime** | When was the judge last fetched from the court site. | 
**possible_norm_judge_array** | [**List[PossibleNormJudge]**](PossibleNormJudge.md) |  | 

## Example

```python
from unicourt.models.judge import Judge

# TODO update the JSON string below
json = "{}"
# create an instance of Judge from a JSON string
judge_instance = Judge.from_json(json)
# print the JSON string representation of the object
print(Judge.to_json())

# convert the object into a dict
judge_dict = judge_instance.to_dict()
# create an instance of Judge from a dict
judge_from_dict = Judge.from_dict(judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


