# Attorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'Attorney']
**attorney_id** | **str** | ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different. | 
**name** | **str** | Name of the attorney as provided by Court. | 
**name_prefix** | **str** |  | 
**first_name** | **str** | First name of the attorney. This is normalized by UniCourt. | 
**middle_name** | **str** | Middle name of the attorney. This is normalized by UniCourt. | 
**last_name** | **str** | Last name of the attorney. This is normalized by UniCourt. | 
**name_suffix** | **str** |  | 
**contact** | [**Contact**](Contact.md) |  | 
**attorney_law_firm_array** | [**List[AttorneyLawFirm]**](AttorneyLawFirm.md) |  | 
**bar_number** | **str** | The bar enrollment number of an attorney. | 
**attorney_type** | [**AttorneyType**](AttorneyType.md) |  | 
**source_attorney_type** | **str** | Attorney Type as provided by Court. | 
**is_visible** | **bool** | Signifies if the attorney as this attorney type is currently isVisible or not for the case. | 
**first_fetch_date** | **datetime** | When was the attorney first fetched from the court site. | 
**last_fetch_date** | **datetime** | When was the attorney last fetched from the court site. | 
**party_attorney_associations** | [**PartyAttorneyAssociations**](PartyAttorneyAssociations.md) |  | 
**possible_norm_attorney_array** | [**List[PossibleNormAttorney]**](PossibleNormAttorney.md) |  | 
**possible_norm_law_firm_array** | [**List[PossibleNormLawFirm]**](PossibleNormLawFirm.md) | Possible Norm Lawfirm array for a Attorney. | 
**party_role_group_id_array** | **List[str]** | Party Role Group Id for a Attorney. | 
**party_role_id_array** | **List[str]** | Party Role Id for a Attorney. | 

## Example

```python
from unicourt.models.attorney import Attorney

# TODO update the JSON string below
json = "{}"
# create an instance of Attorney from a JSON string
attorney_instance = Attorney.from_json(json)
# print the JSON string representation of the object
print(Attorney.to_json())

# convert the object into a dict
attorney_dict = attorney_instance.to_dict()
# create an instance of Attorney from a dict
attorney_from_dict = Attorney.from_dict(attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


