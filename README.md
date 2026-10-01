# Sistema de Fila de Atendimento

Sistema web para gerenciamento de fila de atendimento utilizando Python e Flask.

## Funcionalidades

- Cadastro de clientes na fila
- Geração automática de senha
- Visualização da fila de espera
- Chamada do próximo cliente
- Ordem de atendimento FIFO (First In, First Out)
- Alteração de status do atendimento
- Status disponíveis:
  - Aguardando
  - Em atendimento
  - Concluído
  - Cancelado
- Cancelamento de atendimento
- Contadores de clientes por status
- Interface responsiva

## Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3
- JavaScript

## Estrutura do projeto

```text
mini-app/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
