# AssociatedNormLawFirmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_norm_law_firm_array** | [**List[AssociatedNormLawFirm]**](AssociatedNormLawFirm.md) |  | 
**next_page_api** | **str** | Next page of results if applicable. | 
**previous_page_api** | **str** | Link to previous page of results. | 
**total_pages** | **int** | Total no. of pages. | 
**total_count** | **int** | Total no. of results for this criteria. | 

## Example

```python
from unicourt.models.associated_norm_law_firm_response import AssociatedNormLawFirmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedNormLawFirmResponse from a JSON string
associated_norm_law_firm_response_instance = AssociatedNormLawFirmResponse.from_json(json)
# print the JSON string representation of the object
print(AssociatedNormLawFirmResponse.to_json())

# convert the object into a dict
associated_norm_law_firm_response_dict = associated_norm_law_firm_response_instance.to_dict()
# create an instance of AssociatedNormLawFirmResponse from a dict
associated_norm_law_firm_response_from_dict = AssociatedNormLawFirmResponse.from_dict(associated_norm_law_firm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


