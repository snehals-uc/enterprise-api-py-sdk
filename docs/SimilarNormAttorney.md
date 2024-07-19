# SimilarNormAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'SimilarNormAttorney']
**norm_attorney_id** | **str** |  | 
**norm_attorney_api** | **str** |  | 
**name** | **str** |  | 
**norm_attorney_similarity_score** | **float** |  | 
**bar_record_preview_array** | [**List[BarRecordPreview]**](BarRecordPreview.md) |  | 

## Example

```python
from unicourt.models.similar_norm_attorney import SimilarNormAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of SimilarNormAttorney from a JSON string
similar_norm_attorney_instance = SimilarNormAttorney.from_json(json)
# print the JSON string representation of the object
print(SimilarNormAttorney.to_json())

# convert the object into a dict
similar_norm_attorney_dict = similar_norm_attorney_instance.to_dict()
# create an instance of SimilarNormAttorney from a dict
similar_norm_attorney_from_dict = SimilarNormAttorney.from_dict(similar_norm_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


