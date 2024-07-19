# CaseRelationshipTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'CaseRelationshipTypeResponse']
**case_relationship_type_array** | [**List[CaseRelationshipType]**](CaseRelationshipType.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.case_relationship_type_response import CaseRelationshipTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseRelationshipTypeResponse from a JSON string
case_relationship_type_response_instance = CaseRelationshipTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CaseRelationshipTypeResponse.to_json())

# convert the object into a dict
case_relationship_type_response_dict = case_relationship_type_response_instance.to_dict()
# create an instance of CaseRelationshipTypeResponse from a dict
case_relationship_type_response_from_dict = CaseRelationshipTypeResponse.from_dict(case_relationship_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


