# Conversor de Moedas

Esta é uma API de conversão monetária que suporta moedas fiduciárias, criptomoedas e moedas fictícias.

## Como executar

### Usando Docker
docker build -t currency-converter .
docker run -p 8080:5000 currency-converter

# Escolhas Técnicas
1. Flask
Flask é um microframework para Python, projetado para facilitar a criação de aplicativos web e APIs.

Principais Funcionalidades:

Roteamento: Permite definir rotas que mapeiam URLs para funções Python, facilitando a construção de endpoints RESTful.
Manuseio de Requisições: Oferece uma maneira fácil de acessar e manipular dados de requisições HTTP (como parâmetros, cabeçalhos e corpo).
Respostas: Fornece uma maneira conveniente de enviar respostas JSON, HTML, ou outros formatos de resposta para os clientes.
Por que Foi Escolhido:

Simplicidade: É fácil de aprender e usar, com uma curva de aprendizado baixa.
Flexibilidade: Permite adicionar facilmente extensões e customizações.
Popularidade: Tem uma vasta base de usuários e recursos, o que facilita encontrar suporte e documentação.

2. Requests
Requests é uma biblioteca para fazer requisições HTTP em Python.

Principais Funcionalidades:

Envio de Requisições: Permite enviar requisições HTTP usando métodos como GET, POST, PUT, DELETE, etc.
Manipulação de Respostas: Facilita o acesso ao conteúdo das respostas HTTP e cabeçalhos.
Facilidade de Uso: A API é simples e intuitiva, tornando a interação com serviços web mais fácil.
Por que Foi Escolhido:

Simplicidade e Usabilidade: Facilita a realização de requisições HTTP com uma API muito mais simples do que a biblioteca padrão do Python (urllib).
Popularidade: É amplamente utilizada e bem suportada, o que garante estabilidade e facilidade de encontrar documentação e exemplos.


# Segurança
1. Validação de Dados
Potencial Vulnerabilidade:

Falta de Validação: A API não valida suficientemente os dados recebidos nas requisições. Por exemplo, não há checagem rigorosa dos tipos e formatos dos parâmetros recebidos, o que pode levar a erros ou a comportamentos inesperados.
Sugestão de Mitigação:

Validação Rigorosa: Adicione validação detalhada para garantir que os dados recebidos estejam no formato esperado e dentro dos limites permitidos.

2. Gerenciamento de Moedas
Potencial Vulnerabilidade:

Adição/Remoção de Moedas: O endpoint /currencies permite adicionar e remover moedas sem autenticação, o que pode ser um risco se usuários mal-intencionados explorarem isso.
Sugestão de Mitigação:

Autenticação e Autorização: Adicione mecanismos de autenticação para garantir que apenas usuários autorizados possam adicionar ou remover moedas.

3. Segurança em Requisições Externas
Potencial Vulnerabilidade:

Requisições para APIs Externas: O código faz requisições para APIs externas (se necessário), o que pode ser explorado se não for tratado corretamente.
Sugestão de Mitigação:

Tratamento de Exceções: Certifique-se de tratar exceções ao fazer requisições a APIs externas e verifique se as respostas são válidas.

4. Exposição de Dados Sensíveis
Potencial Vulnerabilidade:

Dados Sensíveis em Respostas: Se a API expõe informações sensíveis ou detalhes sobre sua implementação, isso pode ser um risco.
Sugestão de Mitigação:

Exclusão de Informações Sensíveis: Evite expor dados sensíveis ou detalhes internos sobre a aplicação nas respostas de erro ou sucesso.

5. Para garantir a segurança da API:

Valide e sanitize todos os dados recebidos.
Implemente autenticação e autorização adequadas.
Trate exceções e proteja contra falhas em requisições externas.
Evite expor informações sensíveis.
Adote medidas para proteção contra ataques DDoS e configure corretamente o ambiente de produção.






