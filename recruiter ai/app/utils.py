from typing import List, Dict

BIASED_KEYWORDS = [
    "rockstar", "ninja", "master", "guru", "wizard", "dominant",
    "crush it", "kill it", "naturally", "young", "fresh",
    "digital native", "fit", "energetic", "drive", "aggressive",
    "competitive", "hustle", "grind", "passionate"
]

INCLUSIVE_ALTERNATIVES = {
    "rockstar": "expert",
    "ninja": "skilled",
    "master": "experienced",
    "guru": "specialist",
    "wizard": "proficient",
    "dominant": "leading",
    "crush it": "excel",
    "kill it": "succeed",
    "naturally": "ideally",
    "young": "enthusiastic",
    "fresh": "new",
    "digital native": "tech-savvy",
    "fit": "suitable",
    "energetic": "motivated",
    "drive": "motivation",
    "aggressive": "proactive",
    "competitive": "ambitious",
    "hustle": "dedication",
    "grind": "commitment",
    "passionate": "committed"
}

def detect_bias(text: str) -> Dict[str, any]:
    """
    Detect biased language in text using keyword matching.
    
    Args:
        text: The text to check for biased language
        
    Returns:
        Dictionary with bias_found flag and suggestions
    """
    text_lower = text.lower()
    found_biases = []
    
    for keyword in BIASED_KEYWORDS:
        if keyword in text_lower:
            alternative = INCLUSIVE_ALTERNATIVES.get(keyword, "consider more neutral language")
            found_biases.append({
                "word": keyword,
                "suggestion": alternative
            })
    
    return {
        "bias_found": len(found_biases) > 0,
        "suggestions": found_biases
    }

def validate_bullet_points(points: List[str]) -> bool:
    """
    Validate that exactly 5 bullet points are provided.
    
    Args:
        points: List of bullet points
        
    Returns:
        True if valid, False otherwise
    """
    return len(points) == 5

def sanitize_text(text: str) -> str:
    """
    Sanitize text by removing extra whitespace.
    
    Args:
        text: Text to sanitize
        
    Returns:
        Sanitized text
    """
    return " ".join(text.split())
