<p align="center">
  <h3 align="center">Chat em Python</h3>
  <p align="center">
     <a href="https://github.com/SchneiderrBR/Chat-em-Python">View Demo</a>
     ·
     <a href="https://github.com/SchneiderrBR/Chat-em-Python/issues">Report Bug</a>
     ·
     <a href="https://github.com/SchneiderrBR/Chat-em-Python/issues">Request Feature</a>
  </p></p>

<!-- ABOUT THE PROJECT -->
## About The Project

Chat em desenvolvimento para um trablaho da faculdade de engenheria da computação

### Recursos
* Suporte a IPv4 e IPv6
* Sistema de canais de comunicação
* Protocolo para comunicação com outros servidores

### Procolo
Desenvolvido juntamente com <a href="https://github.com/Fabricio20">Fabricio20</a>, se baseia no JSON para padronizar a comunicação



| OP 		 | ARGUMENTOS                        | Description                                |
|------------|-----------------------------------|------------------------------------------- |
| DISCONNECT | message                           | Fecha a conexao, pode retornar um erro     |
| ERROR      | message                           | envia uma mensagem de erro sem desconectar |
| LOGIN      | name, hash?                       | Define o nickname para o cliente           |
| MESSAGE    | target, message, username?, hash? | Envia uma mensagem (#channel *all &server) |
| JOIN       | channel, username, password?      | Cria/Entra em um canal                     |
| PART       | channel, username                 | Sai de um canal                            |
| ADMIN      | channel, username                 | Da permissoes de admim a um usuario        |
| KICK       | channel, username, message?       | Expulsa um usuario do canal                |
| USERS      | userList, hash, channel?          | Lista todos usuarios                       |
| ACK        | success, hash                     | ACK entre servidores                       |
| CHANNELS   | channelList?                      | Sincroniza canais entre servidores         |