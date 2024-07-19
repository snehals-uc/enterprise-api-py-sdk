# RelatedCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'RelatedCase']
**case_id** | **str** | Case ID of the related Case. This can be null if this case in not found in our database. However the meta information of the related case will be present. | 
**case_number** | **str** | Case Number of the related Case. | 
**case_name** | **str** | Case Name of the related Case. | 
**case_relationship_type** | [**CaseRelationshipType**](CaseRelationshipType.md) |  | 
**source_case_relationship_type** | **str** | Case Relationship Type provided by court. | 
**is_visible** | **bool** | This specifies if the related cases is still related to the parent case or not. | 
**additional_source_data** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**case_api** | **str** | Link to the Case API of the current related case. | 

## Example

```python
from unicourt.models.related_case import RelatedCase

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedCase from a JSON string
related_case_instance = RelatedCase.from_json(json)
# print the JSON string representation of the object
print(RelatedCase.to_json())

# convert the object into a dict
related_case_dict = related_case_instance.to_dict()
# create an instance of RelatedCase from a dict
related_case_from_dict = RelatedCase.from_dict(related_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


