Trac Wikibaseline Plugin
========================

Descrição
=========

Baseline
--------

Baseline é uma marca expressiva no histórico de mudanças dentro de um _item de configuração_ de uma aplicação. 
Um `item de configuração` pode ser tipicamente uma porção de código ou de documentos que sofrem alteração ao 
longo tempo.

Em `VCS` tradicionais esta marca pode ser identificada através do termo tags.

Wiki
----

De acordo com wikipédia, "wiki é um sistema web que permite a criação e edição de páginas web relacionadas entre si
através de um web browser utilizando uma linguagem de marcação simplificada ou um WYSIWIG."

Wikibaseline
------------

Wikibaseline é um plugin do Trac para gerenciar baselines de páginas wiki.

O objetivo principal de wikibaseline é possibilitar que versões de páginas wiki sejam organizadas
e agrupadas dentro de um baseline que possibilite a recuperação e navegação entre essas páginas mesmo
depois da criação de novas versões daquela página. 

A criação de baselines permitiria ainda que tags do sistema de versionamento fossem sincronizadas com o 
sistema de baselines possibilitando total rastreabilidade dos artefatos da aplicação.


Falhas e Funcionalidades
----------------------

Envie solicitações de falhas e novas funcionalidades

Se você tem  qualquer sugestão, crie um ticket


Código fonte
------------

Você pode obter WikibaselinePlugin utilizando subversion ou navegar pelo código fonte no SCM.

Instalação
----------

1. Através dos fontes

    python setup.py bdist_egg 

2. Copie os fontes para o diretório de plugins de seu projeto trac

    $ cp wikibaseline.egg <YOUR-TRAC-ENV>/plugins/

Divirta-se!!!
