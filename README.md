# Ataque de Adulteração de Criptograma e Hash

Este script Python demonstra um ataque de adulteração de criptograma e hash, explorando a propriedade do XOR. O ataque permite que um adversário modifique uma mensagem criptografada sem conhecer a chave secreta, resultando na recuperação de uma mensagem adulterada.

## Como funciona:

1. **Criptografia:** A mensagem original (m) é criptografada com uma chave secreta (k) usando a operação XOR: `c = m xor k`.
2. **Adulteração:** O adversário, que conhece a mensagem original (m) e tem acesso ao criptograma (c), calcula uma adulteração maliciosa (x) fazendo o XOR entre a mensagem original e a mensagem adulterada desejada (n): `x = m xor n`.
3. **Criptograma Adulterado:** O adversário calcula o criptograma adulterado (y) fazendo o XOR entre o criptograma original e a adulteração maliciosa: `y = c xor x`.
4. **Descriptografia:** A vítima, ao receber o criptograma adulterado (y) e usar a chave secreta (k) para descriptografar, obtém a mensagem adulterada (n).

## Código:

O script `decode.py` implementa esse ataque usando a biblioteca `pwntools`. Ele inclui:

* Funções para calcular o XOR entre strings, garantindo que a chave seja repetida para cobrir toda a mensagem.
* Demonstração do ataque com mensagens e chave de exemplo.

## Observações:

* Este é um exemplo simplificado para fins educacionais. Em sistemas reais, a chave secreta seria mais complexa e a adulteração da mensagem poderia ser mais sutil.
* O ataque explora a propriedade do XOR: `(a xor b) xor b = a`.
* Este script destaca a importância de usar algoritmos de criptografia robustos e implementar medidas de segurança adicionais, como autenticação e integridade de mensagens.

## Requisitos:

* Python 3
* Biblioteca `pwntools` (instale com `pip install pwntools`)

## Como executar:

1. Salve o código como `decode.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
3. Execute o script com o comando `python decode.py`.

## Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença:

Este projeto é licenciado sob a licença MIT 
