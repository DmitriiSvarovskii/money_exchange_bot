from typing import Dict, Optional


def get_translation(
    language: str, dictionary: Dict[str, str]
) -> Optional[str]:
    if language == 'en' and 'text_en' in dictionary:
        return dictionary['text_en']
    else:
        return dictionary['text_ru']
