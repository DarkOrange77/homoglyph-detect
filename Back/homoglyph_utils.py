import confusables
import string

def detect_homoglyphs(text):
    suspicious_chars = []
    ascii_chars = string.ascii_letters + string.digits
    for i, char in enumerate(text):
        if ord(char) > 127:
            for ascii_char in ascii_chars:
                if confusables.is_confusable(char, ascii_char):
                    suspicious_chars.append({
                        "original": char,
                        "similar_to": ascii_char,
                        "unicode": f"U+{ord(char):04X}",
                        "position": i
                    })
                    break  # Only report the first match
    return {
        "input": text,
        "is_suspicious": bool(suspicious_chars),
        "suspicious_chars": suspicious_chars
    }