from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

# Sample words list
words = ["python", "fastapi", "uvicorn", "hangman"]
current_word = random.choice(words)
attempts = 10
guessed_letters = set()
masked_word = "*" * len(current_word)


@app.get("/")
def read_root():
    return {"message": "Welcome to Hangman!"}


@app.get("/start_game/")
def start_game():
    global current_word, attempts, guessed_letters, masked_word
    current_word = random.choice(words)
    attempts = 10
    guessed_letters = set()
    masked_word = "*" * len(current_word)
    return {"message": "Game started!", "word": masked_word, "attempts": attempts}


@app.get("/guess/{letter}")
def guess(letter: str):
    global attempts, guessed_letters, masked_word

    if len(letter) != 1:
        raise HTTPException(status_code=400, detail="Only one letter allowed")

    if letter in guessed_letters:
        return {"message": "Letter already guessed", "word": masked_word, "attempts": attempts}

    guessed_letters.add(letter)

    if letter in current_word:
        masked_word = "".join(
            [l if l in guessed_letters else "*" for l in current_word])
    else:
        attempts -= 1

    if "*" not in masked_word:
        return {"message": "Congratulations! You've guessed the word.", "word": current_word}

    if attempts == 0:
        return {"message": "Game over!", "word": current_word}

    return {"message": "Keep going!", "word": masked_word, "attempts": attempts}
