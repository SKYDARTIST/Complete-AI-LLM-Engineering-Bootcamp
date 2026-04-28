import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")


text = "Write a comprehensive blog post about the future of AI and its potential impact on society."


tokens = enc.encode(text)
print(f"Tokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")
print(f"Decoded text: {enc.decode(tokens)}")