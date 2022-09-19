# < Bem-vindo(a) ao repositório do projeto Inventory Report! />

## Contexto:

**Este é o trigésimo quarto projeto desenvolvido por Laura Ramos no curso de Desenvolvimento Web da Trybe - Escola de Programação.**

> *Nível: Iniciante*<br/>
> *Objetivo: Familiarizar-me com entrada e saída de dados em Python aplicando POO.*

> Implementar um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.
> Esses dados de estoque são obtidos de diversas fontes: importação de um arquivo `CSV` ou `JSON` ou `XML`.
> Além disso, o relatório final possui duas versões: *simples* e *completa*.

## Tecnologias usadas

*OBS: O projeto não possui integração front-end.*

> Desenvolvido utilizando: Python

## Para executar a aplicação...

  1. Clone o repositório: `git clone git@github.com:devalaura/inventory-report.git`
  2. Entre na pasta do projeto que você acabou de clonar: `cd inventory-report`
  3. Crie e ative o ambiente virtual:
    
    # Com Docker:
      $ docker-compose run --rm inventory pytest

    # Sem Docker:
      $ python3 -m venv .venv && source .venv/bin/activate
  
  4. Instale as dependências: `python3 -m pip install -r dev-requirements.txt`
  5. Execute o projeto: <br/>
    - `pip install .` <br/>
    - `python3 -m inventory_report.main argumento1 argumento2`<br/>
      - `argumento1`: recebe uma String que indica o caminho para um arquivo `JSON`, `CSV` ou `XML`<br/>
      - `argumento2`: recebe uma String que indica o tipo de relatório esperado: `simples` ou `completo`
<br/><br/>
## < Até mais! />
