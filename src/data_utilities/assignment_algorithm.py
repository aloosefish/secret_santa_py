import random

from src.data_utilities.contact_types import Contact


def assign_secret_santa(list_of_contacts: list[Contact]):
    """
    Legacy implementation for backward compatibility.
    Uses the optimized validate_secret_santa internally.
    """
    return validate_secret_santa(list_of_contacts)


def validate_secret_santa(contacts: list[Contact]) -> list[Contact]:
    """
    Assigns unique secret santas to all contacts using a backtracking algorithm.
    This guarantees a solution without infinite retries.
    
    Algorithm:
    1. Shuffle contacts for randomness
    2. Build a valid derangement (permutation where no element appears in its original position)
    3. Respect spouse constraints
    4. Use backtracking if we hit a dead end
    """
    n = len(contacts)
    if n < 2:
        raise ValueError("Need at least 2 contacts for Secret Santa")
    
    # Create a copy to avoid modifying the original
    result: list[Contact] = [contact.copy() for contact in contacts]
    
    # Create an assignment array to track who gives to whom
    assignment = _find_valid_assignment(contacts)
    
    # Apply the assignments
    for i, target_idx in enumerate(assignment):
        target = contacts[target_idx]
        result[i]["secret_santa"] = {
            "name": target["name"],
            "phone": target["phone"],
        }
    
    return result


def _find_valid_assignment(contacts: list[Contact]) -> list[int]:
    """
    Find a valid assignment using backtracking with constraint satisfaction.
    Returns a list where assignment[i] = j means person i gives to person j.
    """
    n = len(contacts)
    
    # Create indices and shuffle for randomness
    indices = list(range(n))
    random.shuffle(indices)
    
    # Build constraint graph: who can give to whom
    valid_targets = _build_constraint_graph(contacts)
    
    # Try to find assignment using backtracking
    assignment = [-1] * n
    used = [False] * n
    
    if _backtrack(0, indices, assignment, used, valid_targets):
        return assignment
    
    # If backtracking fails, try with a different shuffle (very rare)
    for _ in range(10):
        random.shuffle(indices)
        assignment = [-1] * n
        used = [False] * n
        if _backtrack(0, indices, assignment, used, valid_targets):
            return assignment
    
    raise ValueError("Unable to find valid Secret Santa assignment. Check constraints.")


def _build_constraint_graph(contacts: list[Contact]) -> list[set[int]]:
    """
    Build a graph where valid_targets[i] contains all valid indices that person i can give to.
    """
    n = len(contacts)
    valid_targets = [set(range(n)) for _ in range(n)]
    
    for i, contact in enumerate(contacts):
        # Remove self
        valid_targets[i].discard(i)
        
        # Remove spouse
        if contact["spouse"]:
            for j, other in enumerate(contacts):
                if other["name"] == contact["spouse"]:
                    valid_targets[i].discard(j)
                    break
    
    return valid_targets


def _backtrack(
    person_idx: int,
    order: list[int],
    assignment: list[int],
    used: list[bool],
    valid_targets: list[set[int]]
) -> bool:
    """
    Backtracking algorithm to find a valid assignment.
    """
    if person_idx == len(order):
        return True  # Successfully assigned everyone
    
    person = order[person_idx]
    
    # Try each valid target for this person
    possible_targets = list(valid_targets[person])
    random.shuffle(possible_targets)  # Randomize for variety
    
    for target in possible_targets:
        if not used[target]:
            # Try this assignment
            assignment[person] = target
            used[target] = True
            
            # Recursively assign the rest
            if _backtrack(person_idx + 1, order, assignment, used, valid_targets):
                return True
            
            # Backtrack
            assignment[person] = -1
            used[target] = False
    
    return False  # No valid assignment found for this person


def remove_me(me: str, possible_combos: list[dict]):
    """Helper function kept for backward compatibility with tests."""
    return [s for s in possible_combos if s["name"] != me]


def remove_already_selected(list_to_query: list[dict], selected: list[dict]):
    """Helper function kept for backward compatibility with tests."""
    without_already_selected = list_to_query.copy()
    for selected_item in range(len(selected)):
        for listed_item in list_to_query:
            if selected_item == listed_item:
                without_already_selected.remove(listed_item)
    return without_already_selected


def remove_spouse(me: dict, possible_combos: list[dict]):
    """Helper function kept for backward compatibility with tests."""
    return [s for s in possible_combos if s["name"] != me["spouse"]]
