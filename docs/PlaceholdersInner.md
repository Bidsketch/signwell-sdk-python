# PlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that you will give to each placeholder. We recommend numbering sequentially from 1 to X. IDs are required for associating recipients to fields and more. | 
**name** | **str** | Name of the placeholder. | 
**preassigned_recipient_name** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the name. | [optional] 
**preassigned_recipient_email** | **str** | In some cases, it may be necessary to pre-fill the name and email for a placeholder because it will always be the same person for all documents created from this template. This sets the email. | [optional] 

## Example

```python
from signwell_sdk.models.placeholders_inner import PlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceholdersInner from a JSON string
placeholders_inner_instance = PlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(PlaceholdersInner.to_json())

# convert the object into a dict
placeholders_inner_dict = placeholders_inner_instance.to_dict()
# create an instance of PlaceholdersInner from a dict
placeholders_inner_from_dict = PlaceholdersInner.from_dict(placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


