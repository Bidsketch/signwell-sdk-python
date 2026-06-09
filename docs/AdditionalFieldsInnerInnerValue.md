# AdditionalFieldsInnerInnerValue

Varies according to the field type. Text fields accept strings or numbers. Date fields accept Iso8601 date strings. CheckBoxes accept booleans. Signature and Initials fields can't be signed through API requests. Autofill text fields accept strings or numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from signwell_sdk.models.additional_fields_inner_inner_value import AdditionalFieldsInnerInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalFieldsInnerInnerValue from a JSON string
additional_fields_inner_inner_value_instance = AdditionalFieldsInnerInnerValue.from_json(json)
# print the JSON string representation of the object
print(AdditionalFieldsInnerInnerValue.to_json())

# convert the object into a dict
additional_fields_inner_inner_value_dict = additional_fields_inner_inner_value_instance.to_dict()
# create an instance of AdditionalFieldsInnerInnerValue from a dict
additional_fields_inner_inner_value_from_dict = AdditionalFieldsInnerInnerValue.from_dict(additional_fields_inner_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


