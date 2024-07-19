# PACERCaseSearchContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Name of the object | [default to 'PACERCaseSearchContent']
**pcl_case_link** | **str** | Link to case in the case management/electronic case files (CM/ECF) system at the court. | 
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
**pcl_jpml_number** | **int** | JPML Case Seed number. | 
**pcl_mdl_court_id** | **str** | Which court does this mdl belongs too. | 
**pcl_mdl_date_ordered** | **str** | This parameter represents the mdl date ordered of the case when it is present | 
**pcl_mdl_date_received** | **str** | This parameter represents the mdl date received of the case when it is present | 
**pcl_mdl_extension** | **str** | This parameter represents the mdl extension of the case when it is present | 
**pcl_mdl_judge_last_name** | **str** | This parameter represents the mdl judge lastname of the case when it is present | 
**pcl_mdl_littype** | **str** | This parameter represents the mdl lit type of the case when it is present | 
**pcl_mdl_status** | **str** | This parameter represents the mdl status of the case when it is present | 
**pcl_mdl_transferee** | **str** | This parameter represents the mdl transferee of the case when it is present | 
**pcl_mdl_transferee_district** | **str** | This parameter represents the mdl transferee district of the case when it is present | 
**pcl_civil_cto_number** | **str** | This parameter represents the civil cto number of the case when it is present | 
**pcl_civil_date_disposition** | **str** | This parameter represents the civil disposition date of the case when it is present | 
**pcl_civil_date_initiated** | **str** | This parameter represents the civil initiated date of the case when it is present | 
**pcl_civil_date_terminated** | **str** | This parameter represents the civil terminated date of the case when it is present | 
**pcl_civil_stat_disposition** | **str** | This parameter represents the civil stat disposition of the case when it is present | 
**pcl_civil_stat_initiated** | **str** | This parameter represents the civil stat initiated of the case when it is present | 
**pcl_civil_stat_terminated** | **str** | This parameter represents the civil stat terminated of the case when it is present | 
**pcl_civil_transferee** | **str** | This parameter represents the civil transferee of the case when it is present | 
**pcl_bankruptcy_chapter** | **str** | This parameter represents the bankruptcy chapter of the case when it is present | 
**pcl_date_discharged** | **str** | This parameter represents the date discharged of the case when it is present | 
**pcl_date_dismissed** | **str** | This parameter represents the date dismissed of the case when it is present | 
**pcl_date_reopened** | **str** | This parameter represents the date reopened of the case when it is present | 
**pcl_date_termed** | **str** | This parameter represents the date termed of the case when it is present | 
**pcl_disposition** | **str** | This parameter represents the disposition of the case when it is present | 
**pcl_disposition_method** | **str** | This parameter represents the disposition method of the case when it is present | 
**pcl_joint_bankruptcy_flag** | **str** | This parameter represents the joint bankruptcy flag of the case when it is present | 
**pcl_joint_discharged_date** | **str** | This parameter represents the joint discharged date of the case when it is present | 
**pcl_joint_dismissed_date** | **str** | This parameter represents the joint dismissed date of the case when it is present | 
**pcl_joint_disposition_method** | **str** | This parameter represents the joint disposition method of the case when it is present | 
**pcl_nature_of_suit** | **str** | This parameter represents the nature of suit of the case when it is present | 

## Example

```python
from unicourt.models.pacer_case_search_content import PACERCaseSearchContent

# TODO update the JSON string below
json = "{}"
# create an instance of PACERCaseSearchContent from a JSON string
pacer_case_search_content_instance = PACERCaseSearchContent.from_json(json)
# print the JSON string representation of the object
print(PACERCaseSearchContent.to_json())

# convert the object into a dict
pacer_case_search_content_dict = pacer_case_search_content_instance.to_dict()
# create an instance of PACERCaseSearchContent from a dict
pacer_case_search_content_from_dict = PACERCaseSearchContent.from_dict(pacer_case_search_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


