# PACERPartySearchContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERPartySearchContent']
**pcl_jurisdiction_type** | **str** | Link to case in the case management/electronic case files (CM/ECF) system at the court. | 
**pcl_case_id** | **int** | Sequentially generated number that identifies the case. | 
**pcl_case_number_full** | **str** | Case Number. | 
**pcl_case_title** | **str** | Title of the case. | 
**pcl_case_office** | **str** | The divisional office in which the case was filed. | 
**pcl_case_number** | **int** | The sequence number of the case. | 
**pcl_case_type** | **str** | Code that identifies the type of case. | 
**pcl_case_year** | **int** | The year in which the case falls. Could be two or four digit. | 
**pcl_court_id** | **str** | The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B | 
**pcl_date_filed** | **str** | Filing date of the case. | 
**pcl_last_name** | **str** | This parameter represents the last name of the case when it is present | 
**pcl_first_name** | **str** | This parameter represents the first name of the case when it is present | 
**pcl_middle_name** | **str** | This parameter represents the middle name of the case when it is present | 
**pcl_generation** | **str** | This parameter represents the generation of the case when it is present | 
**pcl_party_role** | **str** | This parameter represents the party role of the case when it is present | 
**pcl_party_type** | **str** | This parameter represents the party type of the case when it is present | 
**pcl_court_case** | [**PACERCaseSearchContent**](PACERCaseSearchContent.md) |  | 

## Example

```python
from unicourt.models.pacer_party_search_content import PACERPartySearchContent

# TODO update the JSON string below
json = "{}"
# create an instance of PACERPartySearchContent from a JSON string
pacer_party_search_content_instance = PACERPartySearchContent.from_json(json)
# print the JSON string representation of the object
print(PACERPartySearchContent.to_json())

# convert the object into a dict
pacer_party_search_content_dict = pacer_party_search_content_instance.to_dict()
# create an instance of PACERPartySearchContent from a dict
pacer_party_search_content_from_dict = PACERPartySearchContent.from_dict(pacer_party_search_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


