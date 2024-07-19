# RelatedNormParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [default to 'RelatedNormParty']
**norm_party_id** | **str** |  | 
**relationship_type** | **str** |  | 

## Example

```python
from unicourt.models.related_norm_party import RelatedNormParty

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedNormParty from a JSON string
related_norm_party_instance = RelatedNormParty.from_json(json)
# print the JSON string representation of the object
print(RelatedNormParty.to_json())

# convert the object into a dict
related_norm_party_dict = related_norm_party_instance.to_dict()
# create an instance of RelatedNormParty from a dict
related_norm_party_from_dict = RelatedNormParty.from_dict(related_norm_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


