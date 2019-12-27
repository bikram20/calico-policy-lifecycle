from schema import Schema, And, Or, Use, Optional

def validate_input_networkpolicy(value):
    schema = Schema({'PolicyName': str,
                     'PolicyOrder': int,
                     'ObjectType': str,
                     Optional('PolicyNamespace'): str,
                     'AppliesToSelector': str,
                     'AppliesToNamespaceSelector': str,
                     'AppliesToSvcActSelector': str,
                     'Direction': list,
                     'EGRESS': list,
                     'INGRESS': list
                    })
    return (schema.is_valid(value))


def validate_input_networkset(value):
    schema = Schema({'ObjectType': str,
                     'NetworkSetName': str,
                     'kind': str,
                     'Labels': dict,
                     'CIDR': list,
                    })
    return (schema.is_valid(value))

