# CauseOfActionAdditionalDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CauseOfActionAdditionalDataResponse']
**cause_of_action_additional_data_array** | [**List[CauseOfActionAdditionalData]**](CauseOfActionAdditionalData.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.cause_of_action_additional_data_response import CauseOfActionAdditionalDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CauseOfActionAdditionalDataResponse from a JSON string
cause_of_action_additional_data_response_instance = CauseOfActionAdditionalDataResponse.from_json(json)
# print the JSON string representation of the object
print(CauseOfActionAdditionalDataResponse.to_json())

# convert the object into a dict
cause_of_action_additional_data_response_dict = cause_of_action_additional_data_response_instance.to_dict()
# create an instance of CauseOfActionAdditionalDataResponse from a dict
cause_of_action_additional_data_response_from_dict = CauseOfActionAdditionalDataResponse.from_dict(cause_of_action_additional_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


