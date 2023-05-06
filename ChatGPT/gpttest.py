import openai

# Masukkan API key
openai.api_key = "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"

# Buat fungsi untuk mengakses API ChatGPT
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message = response.choices[0].text.strip()
    return message

# Gunakan fungsi generate_text untuk menghasilkan teks dari input prompt
text = generate_text("apa itu planet?")
print(text)
