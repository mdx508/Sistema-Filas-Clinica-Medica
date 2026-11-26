
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

O projeto utiliza:

- **Deque:** para organizar as filas de pacientes.
- **Listas:** para armazenar o histórico de atendimentos.
- **Dicionários:** para organizar as especialidades e os registros.

## 4. Regra de Prioridade

O sistema utiliza duas categorias de atendimento:

- **Preferencial:** possui prioridade no atendimento.
- **Normal:** é atendida quando não existem pacientes aguardando na fila preferencial.

Dentro de cada categoria, os pacientes são atendidos por ordem de chegada (FIFO).

A fila preferencial é atendida primeiro. Após ficar vazia, os pacientes da fila normal começam a ser chamados.


## 5. Organização dos Arquivos

- `main.py`: inicia o sistema.
- `filas.py`: controla as filas e as senhas.
- `sistema.py`: gerencia as especialidades e os atendimentos.
- `interface.py`: apresenta a interface gráfica do sistema.

## 6. Tecnologias Utilizadas

- Python
- Tkinter
- Visual Studio Code
- Git e GitHub

## 7. Como Executar o Projeto

1. Instale o Python.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal.
4. Execute o comando:

```bash
python src/main.py
```

## 8. Considerações Finais

O sistema foi desenvolvido como atividade acadêmica da disciplina de Estrutura de Dados, com o objetivo de aplicar conceitos de filas, listas, dicionários e organização de dados em uma aplicação prática.
 

## 9. Imagens do Sistema

### 9.1 Tela principal do sistema

![Tela principal do sistema](./imagens/tela-principal.png)

### 9.2 Histórico de atendimentos

![Histórico de atendimentos](./imagens/historico.png)