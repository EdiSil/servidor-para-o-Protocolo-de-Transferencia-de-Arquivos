# servidor-para-o-Protocolo-de-Transferencia-de-Arquivos
Trabalho da referente a SISTEMAS DE INFORMAÇÃO NA INTERNET

As bibliotecas que foram utilizadas:

- **os**: Esta lib é utilizada para facilitar as operações que são executadas pelo sistema operacional. É utilizanda para pegar informações relativas aos paths dos arquivos e 
diretórios e ou recuperar informações sobre os arquivos.

- **socket**: Esta é utilizada para criar a conexão TCP/IP entre o cliente e o servidor.

A organização do projeto ([pta-server/]):
- **modules/**: Foi criada para modularizar e organizar o projeto em objetos menores assim como foi criada o módulo [FileReader].

- **file_reader.py**: Esse é o módulo para capturar as informações do arquivo. Ele será usado quando o cliente enviar um comando [PEGA].

- **files/**: Esta contém os arquivos que foram consultados pelo cliente com os comandos [PEGA] e [TERM].

- **exceptions/**: É onde contém as exceções para os tratamentos de erros do servidor.

- **pta-server.py**: Faz a referência ao arquivo do servidor.

- **user.txt**: Faz a referência lista de usuários que possuem acesso ao PTA.
