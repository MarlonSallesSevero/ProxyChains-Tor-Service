"""
OBS: Algumas situações é bom usar proxychains nao para todas. Geralmente para logar em um servidor,
que aceita somente alguma faixa de IP ou site que tem a mesma questão.

Para alguns alvos é bom, mas NUNCA para força bruta/pentest/varregadura de massa

Para configurarmos o proxychains no Kali Linux, nos vamos até a pasta /etc e abrimos o arquivo de
configuração do proxychains com algum editor de texto.

- nano /etc/proxychains4.conf

O proxychains da basicamente a possibilidade de enchaminharmos todo nosso trafego através de
uma cadeia de servidores. Fazendo assim permanecermos anonimos atras desses servidores.
Ou requisições de conexão por exemplo.

Existem varios servidores proxy gratuitos pelo Mundo. Porém eles não são muitos rapidos e nem estaveis.
Uma maneira ideal seria VPN's

Temos 3 tipos de proxys que podemos utilizar.

    HTTP, SOCKS4 e SOCKS5

        SEMPRE utilize o SOCKS5 é a opção mais segura e que mantem mais anonimo possivel.
        HTTP é para trafego HTTP e SOCKS4 é muito semelhante a SOCKS5 mas ele não suporte protocolo IPv6 e nem UDP.
        Por isso SOCKS4 pode ser um pouco problematico.

Para ativarmos uma opção basta tiramos o hashtag e pronto esta ativado a opção.

-CONFIGURANDO E ATIVANDO O SERVIÇO VIA TERMINAL-

1 - Realizar a instalação do tor
2 - Realizar a instalação do proxychains no seu linux se o mesmo não vem por padrao no OS
	-sudo apt-get update
	-sudo apt-get install proxychains
3 - Navegar ate /etc/proxychains4.conf e abrir com um editor de teste (ex: nano/ vim)
4 - Desativar marcando com # strict_chain e marcar removendo o # do dynamic_chains
5 - Se possivel validar o DNS leak
5 - Navegar ate o final do arquivo e add o proxy socks5 do tor. (socks5 172.0.0.1 9050)
6 - Salvamos o arquivo proxychains4.conf 
7 - Ativamos o serviço do tor digitando : service tor start 
8 - Depois disso ja podemos acessar o browser utilizando o proxychains digitando: proxychains firefox www.duckduckgo.com
        ps: O firefox é o navegador mais recomendado para utilzação de proxychains, por ser o padrao do linux.

Detalhes tor Service:
Ativando o serviço do Tor padrão.

O serviço Tor no Kali Linux, transforma sua maquina em um dos varios endereços na rede Tor.
Fazendo assim, seu endereço ser modificado randonicamente. Utilizamos juntamente com o proxychains
fazendo assim, o anonimato ser 100%.

Para vermos o atual status do serviço digitamos:
    service tor status

Para iniciarmos:
    service tor start

Para parar:
    service tor stop

Para resetar:
    service tor restart


Utilizando proxychains com o serviço tor, nos navegamos em um 3° nivel de rede.

acessando uma pagina pelo firefox:

proxychains firefox www.duckduckgo.com

Podemos utilizar o proxychains para varias ferramentas.
Por exemplo o nmap:

proxychains nmap -v scan.me.com

"""
