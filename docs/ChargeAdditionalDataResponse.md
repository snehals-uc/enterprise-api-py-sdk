# ChargeAdditionalDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'ChargeAdditionalDataResponse']
**charge_additional_data_array** | [**List[ChargeAdditionalData]**](ChargeAdditionalData.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.charge_additional_data_response import ChargeAdditionalDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeAdditionalDataResponse from a JSON string
charge_additional_data_response_instance = ChargeAdditionalDataResponse.from_json(json)
# print the JSON string representation of the object
print(ChargeAdditionalDataResponse.to_json())

# convert the object into a dict
charge_additional_data_response_dict = charge_additional_data_response_instance.to_dict()
# create an instance of ChargeAdditionalDataResponse from a dict
charge_additional_data_response_from_dict = ChargeAdditionalDataResponse.from_dict(charge_additional_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


