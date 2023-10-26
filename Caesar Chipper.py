def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if encrypt:
                shifted = ord(char) + shift - ord('a')
            else:
                shifted = ord(char) - shift - ord('a')
            shifted = shifted % 26
            shifted += ord('a')
            if is_upper:
                char = chr(shifted).upper()
            else:
                char = chr(shifted)
        result += char
    
    return result

# Meminta pengguna untuk memilih enskripsi atau deskripsi
choice = input("Pilih 'e' untuk enskripsi atau 'd' untuk dekripsi: ").lower()

if choice == 'e':
    plaintext = input("Masukkan pesan yang akan dienskripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))
    cipher_text = caesar_cipher(plaintext, shift)
    print("Pesan Tersandi:", cipher_text)
elif choice == 'd':
    ciphertext = input("Masukkan pesan yang akan didekripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))
    decrypted_text = caesar_cipher(ciphertext, shift, encrypt=False)
    print("Pesan Terdeskripsi:", decrypted_text)
else:
    print("Pilihan tidak valid. Silakan masukkan 'e' atau 'd'.")

