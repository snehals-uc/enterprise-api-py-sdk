# CaseTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseTypeResponse']
**case_type_array** | [**List[CaseType]**](CaseType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.case_type_response import CaseTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTypeResponse from a JSON string
case_type_response_instance = CaseTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CaseTypeResponse.to_json())

# convert the object into a dict
case_type_response_dict = case_type_response_instance.to_dict()
# create an instance of CaseTypeResponse from a dict
case_type_response_from_dict = CaseTypeResponse.from_dict(case_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


