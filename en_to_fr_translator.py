from transformers import MarianMTModel, MarianTokenizer

# Model for English → French
MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

# Load the model and tokenizer
print("🎉 Bienvenue! Welcome to the English → French Translator! 🇫🇷")
print("Loading the French model... (first run may take a minute) 🥖🍷🗼")

tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME, use_fast=False, legacy=True)
model = MarianMTModel.from_pretrained(MODEL_NAME)
print("✅ French model loaded! Let’s start translating! 🇫🇷\n")

# Store translation history
history = []

def translate(text):
    """Translate English text to French."""
    tokens = tokenizer(text, return_tensors="pt", truncation=True)
    output = model.generate(**tokens, max_length=512)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# ---------------------- Interactive loop ----------------------
print("Type your English text, and see the French translation appear! 🇫🇷")
print("Type 'quit' to exit. Type 'history' to see your previous translations.\n")

while True:
    text_input = input("📝 Enter English text: ").strip()
    
    if text_input.lower() == "quit":
        print("👋 Au revoir! Thanks for using the translator! 🇫🇷")
        break
    if text_input.lower() == "history":
        if not history:
            print("📚 No translations yet!")
        else:
            print("📚 Translation History:")
            for i, (en, fr) in enumerate(history, start=1):
                print(f"{i}. {en} → {fr}")
        print()
        continue
    if not text_input:
        print("⚠️ Please enter some text to translate.\n")
        continue

    translation = translate(text_input)
    history.append((text_input, translation))
    print(f"🇫🇷 French translation: {translation}\n")
