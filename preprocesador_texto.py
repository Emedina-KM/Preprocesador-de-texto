# Antes de iniciar se trajo tanto raw-text.txt como stop-words.txt.
with open("raw-text.txt", "r", encoding="utf-8") as raw:
    text = raw.read()
with open("stop-words.txt", "r", encoding="utf-8") as file:
    stop_words = file.read().splitlines()

# En el siguiente apartado se definió clase, atributos y metodos.
class TextAnalyzer():
    def __init__(self, text):
# 2. Eliminar saltos de linea y caracteres que no sean letras.
        formatted_text = text.replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("\n", "")
        
# 3. Eliminar cualquier dígito presente en el texto.
        import re
        text_without_digits = re.sub(r'\d', '', formatted_text)
        
# 1. Convertir todo el texto a minúsculas.
        self.fmt_text = text_without_digits.lower()
        
    def clean_text(self, stopwords):
    # 4. Tokenizar el texto.
        wordlist = self.fmt_text.split(" ")
        # print(f"texto tokenizado: {wordlist}")

    # 5. Remover las stopwords más comunes en español.
        self.filtered_wordlist = []

        for word in wordlist:
            if word not in stopwords:
                self.filtered_wordlist.append(word)
        return self.filtered_wordlist
       
# Instancia.
analized = TextAnalyzer(text)

# Resultado después de limpieza.
print(f"Resultado final --> {analized.clean_text(stop_words)}")

# Texto procesado, se guardo en el archivo "processed-text.text".
with open("processed-text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(analized.filtered_wordlist))