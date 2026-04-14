BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "act as",
    "you are now",
    "bypass",
    "jailbreak",
]

def is_malicious_input(user_input:str) -> bool:
    user_input_lower = user_input.lower()
    return bool(pattern in user_input_lower for pattern in BLOCKED_PATTERNS)

def sanitise_input(user_input:str) -> str:
    return user_input.strip()