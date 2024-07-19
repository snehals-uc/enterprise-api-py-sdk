# AttorneyLawFirm

Name of the attorney's law firm as provided by Court. This can be null as some Courts do not provide this as a separate field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'AttorneyLawFirm']
**attorney_law_firm_id** | **str** | ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**name** | **str** | Name of the law firm as provided by Court. | 
**is_visible** | **bool** | Signifies if the attorney as this attorney type is currently isVisible or not for the case. | 
**first_fetch_date** | **str** | Is the date when the document was first fetched from the court site. | 
**last_fetch_date** | **str** | Is the date when the document was last fetched from the court site. | 

## Example

```python
from unicourt.models.attorney_law_firm import AttorneyLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyLawFirm from a JSON string
attorney_law_firm_instance = AttorneyLawFirm.from_json(json)
# print the JSON string representation of the object
print(AttorneyLawFirm.to_json())

# convert the object into a dict
attorney_law_firm_dict = attorney_law_firm_instance.to_dict()
# create an instance of AttorneyLawFirm from a dict
attorney_law_firm_from_dict = AttorneyLawFirm.from_dict(attorney_law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


