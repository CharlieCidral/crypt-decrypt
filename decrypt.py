from cryptography.fernet import Fernet
import os

# Chaves para decriptar
key_level1 = input("Digite a chave para o primeiro nível de criptografia: ")
key_level2 = input("Digite a chave para o segundo nível de criptografia: ")

# Inicializar os objetos Fernet com as chaves
cipher_level1 = Fernet(key_level1)
cipher_level2 = Fernet(key_level2)

# Abrir e ler o conteúdo do arquivo criptografado
with open('test_encrypted.txt', 'rb') as file:
    encrypted_content = file.read()

# Decriptar o conteúdo do arquivo em dois níveis
decrypted_content = cipher_level1.decrypt(cipher_level2.decrypt(encrypted_content))

# Escrever o conteúdo decriptado no arquivo
with open('test_file.txt', 'wb') as file:
    file.write(decrypted_content)

# Remover o arquivo criptografado
os.remove('test_encrypted.txt')

# Remover as chaves
os.remove('chave1.txt')
os.remove('chave2.txt')

print("Arquivo test_encrypted.txt decriptado com sucesso!")
