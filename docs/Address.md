# Address

Address object Data Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'Address']
**street_address1** | **str** | 1st part of the street address. | 
**street_address2** | **str** | 2nd part of the street address. | 
**city** | **str** | City | 
**state_name** | **str** | State Name if present else default value. | [default to 'UNKNOWN']
**state_code** | **str** | State Code if the state is a US state else contains null. | 
**country_name** | **str** | Country Name if present else default value. | [default to 'UNKNOWN']
**country_code** | **str** | ISO 3166-1 alpha-3 (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements). Code of the country if country name is present. | 
**zip** | **str** | Zip code of the address. | 
**zip4** | **str** | 4 digit extension of the zip code if the address is a US address. | 
**is_visible** | **bool** | Boolean indicating if the address is visible or not. | 
**first_fetch_date** | **datetime** | Date at which this record is created in UniCourt. | 
**last_fetch_date** | **datetime** | Date at which this record was updated in UniCourt. | 
**latitude** | **float** | Coordinates at geographic coordinate system. | 
**longitude** | **float** | Coordinates at geographic coordinate system. | 

## Example

```python
from unicourt.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


