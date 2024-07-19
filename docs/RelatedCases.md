# RelatedCases


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'RelatedCases']
**page_number** | **int** | Page number for which results where obtained. | 
**related_case_array** | [**List[RelatedCase]**](RelatedCase.md) |  | 
**next_page_api** | **str** | Link to next page of a particular entity in a Case. | 
**total_pages** | **int** | Total number of pages to obtain all the objects of a party in the Case. | 
**total_count** | **int** | Total number of parties of the Case entity in a Case. | 

## Example

```python
from unicourt.models.related_cases import RelatedCases

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedCases from a JSON string
related_cases_instance = RelatedCases.from_json(json)
# print the JSON string representation of the object
print(RelatedCases.to_json())

# convert the object into a dict
related_cases_dict = related_cases_instance.to_dict()
# create an instance of RelatedCases from a dict
related_cases_from_dict = RelatedCases.from_dict(related_cases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


