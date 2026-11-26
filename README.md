
# Sistema de Gerenciamento de Filas - Clínica Médica

## 1. Objetivo do Projeto

O projeto tem como objetivo desenvolver um sistema de gerenciamento de filas para uma clínica médica, utilizando Python e a biblioteca Tkinter.

O sistema permite emitir senhas, organizar pacientes por especialidade e categoria, chamar o próximo paciente e consultar o histórico de atendimentos.

## 2. Funcionalidades

- Emissão de senhas normais e preferenciais.
- Atendimento em três especialidades:
  - Clínica Geral
  - Cardiologia
  - Ortopedia
- Organização independente das filas por especialidade.
- Chamada do próximo paciente.
- Consulta das filas de espera.
- Exibição da última senha chamada.
- Estimativa do tempo de espera.
- Histórico de atendimentos realizados.
- Aviso quando não existem pacientes aguardando.

## 3. Estruturas de Dados Utilizadas

- **Deque:** organização das filas de pacientes.
- **Listas:** armazenamento do histórico.
- **Dicionários:** organização das especialidades e registros.

## 4. Regra de Prioridade

O sistema atende primeiro os pacientes preferenciais. Quando não existem pacientes preferenciais aguardando, são chamados os pacientes da fila normal.

Dentro de cada categoria, é respeitada a ordem de chegada (FIFO).

## 5. Organização dos Arquivos

- `main.py`: inicia o sistema.
- `filas.py`: controla as filas e as senhas.
- `sistema.py`: gerencia as especialidades e os atendimentos.
- `interface.py`: apresenta a interface gráfica.

## 6. Tecnologias Utilizadas

- Python
- Tkinter
- Visual Studio Code
- Git e GitHub

## 7. Como Executar o Projeto

1. Instale o Python.
2. Baixe ou clone o repositório.
3. Abra a pasta no Visual Studio Code.
4. Execute no terminal:

```bash
python src/main.py
```

## 8. Considerações Finais

O sistema foi desenvolvido como atividade acadêmica da disciplina de Estrutura de Dados, com o objetivo de aplicar conceitos de filas, listas, dicionários e organização de dados em uma aplicação prática.

## 9. Imagens do Sistema

As imagens abaixo apresentam a interface do sistema e o histórico de atendimentos.

### 9.1 Tela principal do sistema

[Visualizar tela principal do sistema](https://drive.google.com/file/d/14lR2FW0P6ffXIak2c-05tbPoQqOjYeFr/view?usp=drive_link)

### 9.2 Histórico de atendimentos

[Visualizar histórico de atendimentos](https://drive.google.com/file/d/1BT02lo0gE4nAA0AVN33jdw25_T5Jucq3/view?usp=drive_link)
