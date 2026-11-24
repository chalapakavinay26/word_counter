def analyze_text(text):
    total_chars_with_spaces = len(text)
    total_chars_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    words = text.split()
    word_count = len(words)
    sentences = [s.strip() for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    sentence_count = len(sentences)

    longest_word = max(words, key=len) if words else ""

    return {
        "words": word_count,
        "chars_with_spaces": total_chars_with_spaces,
        "chars_no_spaces": total_chars_no_spaces,
        "sentences": sentence_count,
        "longest_word": longest_word,
    }


def word_counter():
    print("\n=== Word Counter ===")
    print("please enter you word or text:")
    text = input("> ").strip()

    if not text:
        print("empty text you entered! please enter any sentence or word enter now.")
        return

    stats = analyze_text(text)

    print("\n---  (Text Analysis) ---")
    print(f" (Words): {stats['words']}")
    print(f" (Chars with spaces): {stats['chars_with_spaces']}")
    print(f"(Chars without spaces): {stats['chars_no_spaces']}")
    print(f" (Sentences): {stats['sentences']}")
    if stats["longest_word"]:
        print(f"(Longest word): {stats['longest_word']}")


if __name__ == "__main__":
    word_counter()
