# CauseOfActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CauseOfActionResponse']
**cause_of_action_array** | [**List[CauseOfAction]**](CauseOfAction.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.cause_of_action_response import CauseOfActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CauseOfActionResponse from a JSON string
cause_of_action_response_instance = CauseOfActionResponse.from_json(json)
# print the JSON string representation of the object
print(CauseOfActionResponse.to_json())

# convert the object into a dict
cause_of_action_response_dict = cause_of_action_response_instance.to_dict()
# create an instance of CauseOfActionResponse from a dict
cause_of_action_response_from_dict = CauseOfActionResponse.from_dict(cause_of_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


