from typing import Optional, Tuple

from .constants import QUESTION_RETIRED


def get_display(choices, label) -> Optional[str]:
    """Returns the display value of a choices tuple for label."""
    for choice in choices:
        store_value, display_value = choice
        if label == store_value:
            return display_value
    return None


def append_question_retired_choice(choices) -> Tuple[Tuple[str, str], ...]:
    choices = list(choices)
    choices.append((QUESTION_RETIRED, QUESTION_RETIRED))
    choices = tuple(choices)
    return choices
