# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# OLIV.IA - Plataforma de Inteligência Artificial Modular (MVP: JURIX)

## Grupo 7

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/amanda-damasceno-martins/">566598 - Amanda Damasceno Martins</a>
- <a href="https://www.linkedin.com/in/cauasantoslt">566599 - Cauã Santos</a>
- <a href="https://www.linkedin.com/in/fabio-baldo-7959a22a/">567851 - Fabio Baldo</a> 
- <a href="https://www.linkedin.com/in/giovanna-gomes-82b993372/">567169 - Giovanna Gomes Oliveira</a> 
- <a href="https://www.linkedin.com/in/roberto-alvares-785059215/">568265 - Roberto Almeida Alvares</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b/">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>

## 📜 Descrição

Este projeto foi desenvolvido no âmbito da **Global Solution 2025.2** com o tema **"O Futuro do Trabalho"**.

O projeto **Oliv.ia** é uma Engine de IA agnóstica e modular, desenhada para atuar como uma camada inteligente de triagem entre clientes e especialistas em setores de alta complexidade. Para este MVP, apresentamos o módulo **JURIX**, focado na triagem jurídica automatizada.

**O Problema:**
O futuro do trabalho jurídico exige eficiência. Advogados perdem até 40% do tempo produtivo tentando decifrar relatos confusos, áudios longos e informações desestruturadas enviadas por clientes.

**A Solução:**
O JURIX utiliza Processamento de Linguagem Natural (NLP) e Engenharia de Prompt para:
1.  Realizar uma anamnese interativa com o cliente (Chatbot).
2.  Estruturar dados não-estruturados em JSON (Área do Direito, Resumo dos Fatos, Urgência, Sentimento).
3.  Gerar inteligência de dados para gestão do escritório.

A solução integra **Python** (Backend e IA) e **Linguagem R** (Analytics), promovendo um ambiente de trabalho mais humano (Human-in-the-loop), onde a tecnologia absorve a burocracia e o profissional foca na estratégia.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens e logos.

- <b>config</b>: Posicione aqui arquivos de configuração (ex: variáveis de ambiente, templates de prompt).

- <b>document</b>: aqui estão todos os documentos do projeto, incluindo o PDF oficial da Global Solution ("Oliv.ia_Project_Doc.pdf").

- <b>scripts</b>: Scripts auxiliares para instalação de dependências ou setup de banco de dados.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto:
    - `main.py`: Código Python contendo o Chatbot e a Engine geradora de JSON.
    - `analytics.R`: Script em R para geração de gráficos e insights estatísticos.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Pré-requisitos
* Python 3.8 ou superior.
* R e RStudio (para o analytics).
* Chave de API válida (OpenAI ou Groq).

### Passo 1: Configuração do Ambiente Python
1.  Clone este repositório em sua máquina local.
2.  Instale as dependências listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configure suas chaves de API (Variáveis de Ambiente) no sistema ou diretamente no `src/main.py` (apenas para testes locais).

### Passo 2: Executando o Chatbot (JURIX)
1.  Navegue até a pasta `src`.
2.  Execute o arquivo principal:
    ```bash
    python main.py
    ```
3.  Interaja com o terminal simulando um cliente. Digite `x` para encerrar a conversa e gerar o JSON estruturado.

### Passo 3: Executando a Análise de Dados (R)
1.  Abra o arquivo `src/analytics.R` no RStudio.
2.  Instale as bibliotecas necessárias (`ggplot2`, `dplyr`) caso não as tenha.
3.  Execute o script completo (Run All) para visualizar os gráficos de "Sentimento vs. Tempo de Resolução" e "Urgência por Área".

## 🗃 Histórico de lançamentos

* 0.1.0 - 13/11/2025
    * Lançamento do MVP Módulo Jurix (Global Solution).
    * Implementação do Chatbot em Python.
    * Integração de script de Analytics em R.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p># GlobalSolution-Oliv.ia
