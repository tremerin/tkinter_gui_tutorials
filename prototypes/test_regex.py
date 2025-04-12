import re

def get_between(text, start_word, end_word):
    pattern = re.escape(start_word) + r"(.*?)" + re.escape(end_word)
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return None

argv1 = f"\033[41mtexto\033[0m"
argv2 = f"otro \033[41mtexto2\033[0m mas"
texto = "Aquí va la palabra INICIO y aquí está el contenido que quiero, luego viene FIN y ya."
print(texto)
print(get_between(texto, "INICIO", "FIN"))
print(argv2)
print(get_between(argv2, "\033[41m", "\033[0m"))
print(get_between(argv2, "", "\033[41m"))
print(get_between(argv2, "\033[0m", "\0"))


match = re.search("\\033\[41m", argv2)
match2 = re.search("\\033\[0m", argv2)
#match = re.search("texto", argv2)
if match and match2:
    print(match.group())     # Devuelve el texto que coincidió con el patrón
    print("\033[0m")
    print(match.start())     # Índice de inicio
    print(match.end())       # Índice de fin
    print(match.span())      # (inicio, fin)
    print(argv2[match.end():match2.start()])