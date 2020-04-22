## Chat em Python

Chat em desenvolvimento para um trabalho da faculdade de engenheria da computação

### Recursos
* Suporte a IPv4 e IPv6
* Sistema de canais de comunicação
* Protocolo para comunicação com outros servidores

### Protocolo
Desenvolvido juntamente com <a href="https://github.com/Fabricio20">Fabricio20</a>, se baseia no JSON para padronizar a comunicação



| OPERAÇAO   | ARGUMENTOS                        | Description                                |
|------------|-----------------------------------|------------------------------------------- |
| DISCONNECT | message                           | Fecha a conexao, pode retornar um erro     |
| ERROR      | message                           | envia uma mensagem de erro sem desconectar |
| LOGIN      | name, hash                        | Define o nickname para o cliente           |
| MESSAGE    | target, message, username, hash   | Envia uma mensagem (#channel *all &server) |
| JOIN       | channel, username, password       | Cria/Entra em um canal                     |
| PART       | channel, username                 | Sai de um canal                            |
| ADMIN      | channel, username                 | Da permissoes de admim a um usuario        |
| KICK       | channel, username, message        | Expulsa um usuario do canal                |
| USERS      | userList, hash, channel           | Lista todos usuarios                       |
| ACK        | success, hash                     | ACK entre servidores                       |
| CHANNELS   | channelList                       | Sincroniza canais entre servidores         |