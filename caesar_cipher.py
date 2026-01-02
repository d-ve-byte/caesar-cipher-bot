
from typing import Literal
Mode = Literal["encrypt", "decrypt"]


def caesar_cipher(message: str, shift: int, mode: Mode) -> str:
    """Encrypt or decrypt a message with a Caesar cipher. 
    The cipher will shift alphabetic characters by ``shift`` positions. 
    Non-alphabetic characters will pass through unchanged. 
    Shift will either be positive or negative and Decryption will make use of the inverse shift."""

    def shift_char(ch: str, offset: int) -> str:
        if "a" <= ch <= "z":
            base = ord("a")
            return chr((ord(ch) - base + offset) % 26 + base)
        if "A" <= ch <= "Z":
            base = ord("A")
            return chr((ord(ch) - base + offset) % 26 + base)
        return ch

    effective_shift = shift if mode == "encrypt" else -shift
    return "".join(shift_char(c, effective_shift) for c in message)


def prompt_user() -> None:
    print("Caesar Cipher — Encrypt/Decrypt")
    message = input("Enter your message: ")

    while True:
        try:
            shift = int(input("Enter shift (integer, can be negative): "))
            break
        except ValueError:
            print("Shift must be an integer. Try again.")

    while True:
        mode_raw = input("Choose mode: [E]ncrypt or [D]ecrypt: ").strip().lower()
        if mode_raw in {"e", "encrypt"}:
            mode: Mode = "encrypt"
            break
        if mode_raw in {"d", "decrypt"}:
            mode = "decrypt"
            break
        print("Please enter E or D.")

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}): {result}\n")


if __name__ == "__main__":
    prompt_user()
