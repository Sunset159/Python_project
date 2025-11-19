import re
from collections import Counter

PROMPT = "Введите текст для анализа (не менее 100 символов):\n> "

def normalize(text: str) -> list[str]:
    text = text.lower()

    text = re.sub(r"[^\w\s\-’']", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = re.findall(r"[А-Яа-яЁё]+(?:[-’'][А-Яа-яЁё]+)*", text)
    tokens = [w for w in tokens if len(w) > 1]

    return tokens

def statistic():
    raw = ""
    while len(raw) < 100:
        raw = input(PROMPT)

    total_chars_with_spaces = len(raw)
    total_chars_without_spaces = len(re.sub(r"\s+", "", raw))

    tokens = normalize(raw)

    freq = Counter(tokens)

    top5_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:5]
    top5_long = sorted(freq.keys(), key=lambda w: (-len(w), w))[:5]

    avg_len = (sum(len(w) for w in tokens) / len(tokens)) if tokens else 0.0

    print("\nРезультаты анализа:")
    print(f"- Общее количество символов: {total_chars_with_spaces} (без пробелов: {total_chars_without_spaces})")
    print(f"- Количество словоформ: {len(tokens)}")

    print("- Самые частые словоформы:")
    for w, c in top5_freq:
        times = "раза" if 2 <= c % 10 <= 4 and not 12 <= c % 100 <= 14 else "раз"
        print(f"   - \"{w}\": {c} {times}")

    print("- Самые длинные словоформы:")
    for w in top5_long:
        print(f"   - \"{w}\" ({len(w)} букв)")

    print(f"- Средняя длина словоформ: {avg_len:.1f} символа")

if __name__ == "__main__":
    statistic()
