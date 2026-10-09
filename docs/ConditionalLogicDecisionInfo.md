# ConditionalLogicDecisionInfo

Audit record of a signer-side decision about a CL rule that fired against a completed field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | External ID of the conditional rule that fired | 
**field_api_id** | **str** | api_id of the field the decision applies to | 
**decision_type** | **str** | Whether the signer kept the existing signature or the value was cleared | 
**decided_at** | **datetime** | When the decision was recorded | 
**description** | **str** | Human-readable summary of the decision | [optional] 

## Example

```python
from signwell_sdk.models.conditional_logic_decision_info import ConditionalLogicDecisionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalLogicDecisionInfo from a JSON string
conditional_logic_decision_info_instance = ConditionalLogicDecisionInfo.from_json(json)
# print the JSON string representation of the object
print(ConditionalLogicDecisionInfo.to_json())

# convert the object into a dict
conditional_logic_decision_info_dict = conditional_logic_decision_info_instance.to_dict()
# create an instance of ConditionalLogicDecisionInfo from a dict
conditional_logic_decision_info_from_dict = ConditionalLogicDecisionInfo.from_dict(conditional_logic_decision_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


