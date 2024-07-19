# PACERImportCaseResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERImportCaseResults']
**has_only_meta_info** | **bool** | This field determines if the UniCourt Content has only meta information. If the value is true and you require to get the latest updates of the case you will need to make a request to the updateCase API. | 
**uni_court_content** | [**CaseSearchResult**](CaseSearchResult.md) |  | 

## Example

```python
from unicourt.models.pacer_import_case_results import PACERImportCaseResults

# TODO update the JSON string below
json = "{}"
# create an instance of PACERImportCaseResults from a JSON string
pacer_import_case_results_instance = PACERImportCaseResults.from_json(json)
# print the JSON string representation of the object
print(PACERImportCaseResults.to_json())

# convert the object into a dict
pacer_import_case_results_dict = pacer_import_case_results_instance.to_dict()
# create an instance of PACERImportCaseResults from a dict
pacer_import_case_results_from_dict = PACERImportCaseResults.from_dict(pacer_import_case_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


