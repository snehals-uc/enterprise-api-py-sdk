# JurisdictionGeoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'JurisdictionGeoResponse']
**jurisdiction_geo_array** | [**List[JurisdictionGeo]**](JurisdictionGeo.md) |  | 
**next_page_api** | **str** | Link to next page. | 
**previous_page_api** | **str** | Link to previous page. | 
**page_number** | **int** | Page number for which results where obtained. | 
**total_pages** | **int** | Total number of pages to obtain all the objects. | 
**total_count** | **int** | Total number of matches found. | 

## Example

```python
from unicourt.models.jurisdiction_geo_response import JurisdictionGeoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionGeoResponse from a JSON string
jurisdiction_geo_response_instance = JurisdictionGeoResponse.from_json(json)
# print the JSON string representation of the object
print(JurisdictionGeoResponse.to_json())

# convert the object into a dict
jurisdiction_geo_response_dict = jurisdiction_geo_response_instance.to_dict()
# create an instance of JurisdictionGeoResponse from a dict
jurisdiction_geo_response_from_dict = JurisdictionGeoResponse.from_dict(jurisdiction_geo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


