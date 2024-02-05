from cryptography.fernet import Fernet
import os

# Gerar uma chave para o primeiro nível de criptografia
key_level1 = Fernet.generate_key()
cipher_level1 = Fernet(key_level1)

# Gerar uma chave para o segundo nível de criptografia
key_level2 = Fernet.generate_key()
cipher_level2 = Fernet(key_level2)

# Abrir e ler o conteúdo do arquivo
with open('test_file.txt', 'rb') as file:
    original_content = file.read()

# Criptografar o conteúdo do arquivo em dois níveis
encrypted_content = cipher_level2.encrypt(cipher_level1.encrypt(original_content))

# Escrever o conteúdo criptografado no arquivo
with open('test_encrypted.txt', 'wb') as file:
    file.write(encrypted_content)

# Salvar as chaves em arquivos separados
with open('chave1.txt', 'wb') as chave1_file:
    chave1_file.write(key_level1)

with open('chave2.txt', 'wb') as chave2_file:
    chave2_file.write(key_level2)

# Remover o arquivo original
os.remove('test_file.txt')

print("Arquivo test_file.txt encriptado com sucesso!")
print("Chave para o primeiro nível de criptografia salva em chave1.txt")
print("Chave para o segundo nível de criptografia salva em chave2.txt")
