# AutomacoesAbref

Esta automação foi desenvolvida para gerar carteirinhas personalizadas de atletas, utilizando o módulo **Pillow** para manipulação de imagens. A funcionalidade principal consiste em criar a frente e o verso das carteirinhas, inserindo informações como nome, data de nascimento, unidade, validade e foto do atleta, além do contato da escola no verso.

## Funcionalidades

### Geração da Frente da Carteirinha:
- Insere o **nome**, **data de nascimento**, **unidade** e **validade**.
- Adiciona a **foto do atleta** redimensionada para o layout correto.
- Simula texto em **negrito** para destacar as informações.

### Geração do Verso da Carteirinha:
- Insere o **contato da escola** no modelo do verso.
- Simula texto em **negrito** para maior legibilidade.

### Integração com Banco de Dados (futuro):
- Os dados atualmente estão **mockados** no código, mas serão obtidos diretamente de uma **conexão com o banco de dados do site**, permitindo a geração automatizada de carteirinhas para múltiplos atletas.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para a automação.
- **Pillow**: Biblioteca para manipulação de imagens.
- **Datetime**: Para cálculo automático da validade da carteirinha.
- **Banco de Dados** (planejado): Para integração com os dados do site.

## Como Funciona
1. O script carrega modelos de imagem (frente e verso) e insere as informações personalizadas.
2. A foto do atleta é redimensionada e posicionada no local correto.
3. As carteirinhas geradas são salvas em arquivos de saída, prontas para impressão ou distribuição digital.

Esta automação simplifica o processo de criação de carteirinhas, reduzindo o trabalho manual e garantindo consistência no layout.