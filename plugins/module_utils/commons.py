from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any


# Build and Return Payload from Dict Object
# Filter All NONE Fields
def dataclass_to_payload(instance: Any) -> Dict[str, Any]:
    """
    Converts a dataclass instance to a dictionary payload.
    
    Only includes fields that are not None and handles nested dataclasses and lists.

    Args:
        instance (Any): The dataclass instance to convert.

    Returns:
        Dict[str, Any]: The resulting dictionary payload.
    """

    # Payload to return
    payload = {}

    # Ierate on instance Field
    for field_name, field_value in asdict(instance).items():

        # If Value is not NONE
        if field_value is not None:

            # Add Value to the resulting Dict
            payload[field_name] = field_value

    # Return Payload
    return payload
