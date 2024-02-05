
# Ransomware Simples em Python
Este é um projeto proposto pela plataforma DIO (Digital Innovation One) para criar um ransomware simples em Python. Um ransomware é um tipo de malware que criptografa os arquivos de um sistema e exige um resgate (geralmente em criptomoedas) para descriptografá-los.

## Descrição do Projeto
Este projeto consiste em dois scripts em Python: encrypt.py e decrypt.py. O encrypt.py é responsável por criptografar um arquivo especificado e armazenar o conteúdo criptografado em um novo arquivo. O decrypt.py é responsável por descriptografar o arquivo criptografado e restaurá-lo ao seu estado original.

## Como Usar
### 1. Clonando o Repositório
Clone este repositório para o seu ambiente local usando o seguinte comando:

``` bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Instalando Dependências
Certifique-se de ter a biblioteca cryptography instalada. Caso não tenha, você pode instalá-la via pip:

``` bash
pip install cryptography
```

### 3. Executando o Ransomware
Encrypt.py: Execute este script para criptografar um arquivo. Ele solicitará as chaves de criptografia que você deve guardar com segurança.

Decrypt.py: Execute este script para descriptografar um arquivo que foi criptografado com o encrypt.py.

### 4. Segurança das Chaves
Guarde as chaves de criptografia (chave1.txt e chave2.txt) em um local seguro. A perda dessas chaves pode resultar na impossibilidade de descriptografar os arquivos.

## Sugestões de Aprimoramento
- Implementação de um Sistema de Chaves Seguro: Considere implementar um sistema de gestão de chaves mais robusto, como o uso de sistemas de gerenciamento de chaves (KMS).

- Melhorias na Interface do Usuário: Adicione uma interface de usuário mais amigável e segura para interagir com o ransomware.

- Testes de Unidade: Implemente testes de unidade para garantir que o código funcione conforme o esperado em diferentes cenários.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs, ou novos recursos.

## Licença
Este projeto está licenciado sob a MIT License.
