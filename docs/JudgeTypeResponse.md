# JudgeTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'JudgeTypeResponse']
**judge_type_array** | [**List[JudgeType]**](JudgeType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.judge_type_response import JudgeTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeTypeResponse from a JSON string
judge_type_response_instance = JudgeTypeResponse.from_json(json)
# print the JSON string representation of the object
print(JudgeTypeResponse.to_json())

# convert the object into a dict
judge_type_response_dict = judge_type_response_instance.to_dict()
# create an instance of JudgeTypeResponse from a dict
judge_type_response_from_dict = JudgeTypeResponse.from_dict(judge_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


