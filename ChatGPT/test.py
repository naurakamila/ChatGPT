import openai

openai.api_key = "sk-9cBnuDhKlxziP3bi8u3UT3BlbkFJSxuRqU12LxEuDhJZ41qea"

# Menggunakan fungsi get_chatbot_response() seperti yang dijelaskan sebelumnya
def get_chatbot_response(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

# Looping untuk pertanyaan berulang dari pengguna
while True:
    # Mengambil input dari pengguna
    user_input = input("Anda: ")
    
    # Menanyakan pertanyaan ke chatbot
    prompt = "Pengguna: " + user_input + "\nChatbot:"
    chatbot_response = get_chatbot_response(prompt)
    
    # Menampilkan respon chatbot
    print(chatbot_response)
    
    # Looping untuk meminta persetujuan pengguna
    for i in range(3):
        user_input = input("Lanjut bertanya? (ya/tidak) ")
        if user_input.lower() == "ya":
            break
        elif user_input.lower() == "tidak":
            exit()
        else:
            print("Maaf, saya tidak mengerti. Tolong jawab dengan 'ya' atau 'tidak'")
    
    # Keluar dari loop jika pengguna tidak ingin melanjutkan bertanya
    if user_input.lower() != "ya":
        break
