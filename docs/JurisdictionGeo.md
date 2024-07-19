# JurisdictionGeo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'JurisdictionGeo']
**jurisdiction_geo_id** | **str** |  | 
**country** | **str** |  | 
**state** | **str** |  | 
**county** | **str** |  | 
**city** | **str** |  | 
**fips_code** | **str** |  | 
**zip_code_array** | **List[str]** |  | 
**created_date** | **datetime** | The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS. | 
**courts_for_jurisdiction_geo_api** | **str** |  | 

## Example

```python
from unicourt.models.jurisdiction_geo import JurisdictionGeo

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionGeo from a JSON string
jurisdiction_geo_instance = JurisdictionGeo.from_json(json)
# print the JSON string representation of the object
print(JurisdictionGeo.to_json())

# convert the object into a dict
jurisdiction_geo_dict = jurisdiction_geo_instance.to_dict()
# create an instance of JurisdictionGeo from a dict
jurisdiction_geo_from_dict = JurisdictionGeo.from_dict(jurisdiction_geo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


