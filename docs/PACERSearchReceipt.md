# PACERSearchReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERSearchReceipt']
**transaction_date** | **datetime** | Date when the transaction was made at the pacer court site. | 
**search_fee** | **str** | PACER Search Fee. | 
**billable_pages** | **int** | No of pages that was billed for the given PACER search. | 
**login_id** | **str** | ID which is used for PACER login. | 
**client_code** | **str** | client code added if any was set. | 
**firm_id** | **str** | Firm ID. | 
**search** | **str** | Details of the search made for this request. | 
**description** | **str** | Description of the search made. | 
**cso_id** | **int** | PACER Account ID. | 
**report_id** | **str** | Report ID for the search made. | 

## Example

```python
from unicourt.models.pacer_search_receipt import PACERSearchReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of PACERSearchReceipt from a JSON string
pacer_search_receipt_instance = PACERSearchReceipt.from_json(json)
# print the JSON string representation of the object
print(PACERSearchReceipt.to_json())

# convert the object into a dict
pacer_search_receipt_dict = pacer_search_receipt_instance.to_dict()
# create an instance of PACERSearchReceipt from a dict
pacer_search_receipt_from_dict = PACERSearchReceipt.from_dict(pacer_search_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


