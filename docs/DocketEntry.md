# DocketEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'DocketEntry']
**sort_order** | **int** | Order number how the dockets have stored in UniCourt. | 
**docket_entry_date** | **datetime** | Docket Action Date | 
**docket_number** | **int** | The respective docket entry number which is defined in the court website. | 
**docket_badge** | **str** | Docket Badge helps you to know what type of a docket entry it is. | 
**text** | **str** | Source Docket Entry | 
**text_structured** | [**SourceStructuredData**](SourceStructuredData.md) |  | 
**referenced_docket_number_array** | [**List[ReferencedDocketNumber]**](ReferencedDocketNumber.md) | Other Docket Numbers that referenced for a particular docket entry. | 
**docket_entry_primary_documents** | [**DocketEntryPrimaryDocuments**](DocketEntryPrimaryDocuments.md) |  | 
**docket_entry_secondary_documents** | [**DocketEntrySecondaryDocuments**](DocketEntrySecondaryDocuments.md) |  | 
**last_fetch_date** | **str** | When this docket entry was last fetched from the source. | 
**boundary** | **str** | Determines if it is the first docket entry or the last docket entry. This value will be set only for the first and last docket entry. For other docket entries it will be null. However, this will be set as single_docket_entry when the Case contains only one docket entry. | 

## Example

```python
from unicourt.models.docket_entry import DocketEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DocketEntry from a JSON string
docket_entry_instance = DocketEntry.from_json(json)
# print the JSON string representation of the object
print(DocketEntry.to_json())

# convert the object into a dict
docket_entry_dict = docket_entry_instance.to_dict()
# create an instance of DocketEntry from a dict
docket_entry_from_dict = DocketEntry.from_dict(docket_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


