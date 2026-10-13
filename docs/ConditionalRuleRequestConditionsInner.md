# ConditionalRuleRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | How the field_api_ids combine within a condition: &#x60;any_of&#x60;, &#x60;all_of&#x60;, &#x60;none_of&#x60;, or &#x60;not_all_of&#x60;. | 
**status** | **str** | The field state the condition tests for: &#x60;completed&#x60; or &#x60;not_completed&#x60;. | 
**join_operator** | **str** | How this condition joins the next one in the rule: &#x60;and_operator&#x60; or &#x60;or_operator&#x60;. The first condition&#39;s value is ignored. | [optional] 
**field_api_ids** | **List[str]** | api_ids of the trigger fields the condition watches. | 
**position** | **int** | 1-indexed order of the condition within the rule. | [optional] 

## Example

```python
from signwell_sdk.models.conditional_rule_request_conditions_inner import ConditionalRuleRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalRuleRequestConditionsInner from a JSON string
conditional_rule_request_conditions_inner_instance = ConditionalRuleRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(ConditionalRuleRequestConditionsInner.to_json())

# convert the object into a dict
conditional_rule_request_conditions_inner_dict = conditional_rule_request_conditions_inner_instance.to_dict()
# create an instance of ConditionalRuleRequestConditionsInner from a dict
conditional_rule_request_conditions_inner_from_dict = ConditionalRuleRequestConditionsInner.from_dict(conditional_rule_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


