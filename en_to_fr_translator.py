#Make sure that you have installed:
# pip install transformers torch sentencepiece gradio
from transformers import MarianMTModel, MarianTokenizer

MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

print("🎉 Bienvenue! Welcome to the English → French Translator! 🇫🇷🥖🗼")
print("Loading the French model... (first run may take a minute)")

tokenizer = MarianTokenizer.from_pretrained(
    MODEL_NAME,
    use_fast=False,
    legacy=True
)
model = MarianMTModel.from_pretrained(MODEL_NAME)

print("✅ Model loaded successfully!\n")


def translate(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True)
    output = model.generate(**tokens, max_length=512)
    return tokenizer.decode(output[0], skip_special_tokens=True)


# ---------------------- Interface choice ----------------------
print("How would you like to use the translator?")
print("1️⃣ Text-based (Terminal)")
print("2️⃣ Graphical (Web Interface)")

choice = input("Enter 1 or 2: ").strip()

# ---------------------- TEXT MODE ----------------------
if choice == "1":
    history = []
    print("\n📝 Text-based Translator 🇫🇷")
    print("Type 'quit' to exit, 'history' to see past translations.\n")

    while True:
        text_input = input("📝 English text: ").strip()

        if text_input.lower() == "quit":
            print("👋 Au revoir! Merci! 🇫🇷")
            break

        if text_input.lower() == "history":
            if not history:
                print("📚 No translations yet!\n")
            else:
                print("📚 Translation History:")
                for i, (en, fr) in enumerate(history, start=1):
                    print(f"{i}. {en} → {fr}")
                print()
            continue

        if not text_input:
            print("⚠️ Please enter some text.\n")
            continue

        french = translate(text_input)
        history.append((text_input, french))
        print(f"🇫🇷 French: {french}\n")


# ---------------------- GRAPHICAL MODE ----------------------
elif choice == "2":
    import gradio as gr

    print("\n🌐 Launching graphical interface... 🇫🇷🗼")

    iface = gr.Interface(
        fn=translate,
        inputs=gr.Textbox(label="🇬🇧 Enter English text"),
        outputs=gr.Textbox(label="🇫🇷 French translation"),
        title="🇫🇷 English → French Translator",
        description="Translate English to French with a touch of Paris 🥖🍷🗼"
    )

    iface.launch(share=True)

else:
    print("❌ Invalid choice. Please restart and enter 1 or 2.")