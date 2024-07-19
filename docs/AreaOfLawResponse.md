# AreaOfLawResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'AreaOfLawResponse']
**area_of_law_array** | [**List[AreaOfLaw]**](AreaOfLaw.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.area_of_law_response import AreaOfLawResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AreaOfLawResponse from a JSON string
area_of_law_response_instance = AreaOfLawResponse.from_json(json)
# print the JSON string representation of the object
print(AreaOfLawResponse.to_json())

# convert the object into a dict
area_of_law_response_dict = area_of_law_response_instance.to_dict()
# create an instance of AreaOfLawResponse from a dict
area_of_law_response_from_dict = AreaOfLawResponse.from_dict(area_of_law_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


