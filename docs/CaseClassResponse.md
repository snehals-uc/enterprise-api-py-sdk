# CaseClassResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseClassResponse']
**case_class_array** | [**List[CaseClass]**](CaseClass.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.case_class_response import CaseClassResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseClassResponse from a JSON string
case_class_response_instance = CaseClassResponse.from_json(json)
# print the JSON string representation of the object
print(CaseClassResponse.to_json())

# convert the object into a dict
case_class_response_dict = case_class_response_instance.to_dict()
# create an instance of CaseClassResponse from a dict
case_class_response_from_dict = CaseClassResponse.from_dict(case_class_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


