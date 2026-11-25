# Sistema de Gerenciamento de Filas - Clínica Médica

## Sobre o projeto

O Sistema de Gerenciamento de Filas para Clínica Médica é um projeto acadêmico desenvolvido para a disciplina de **Estrutura de Dados II**, do Centro Universitário UDF.

O objetivo é desenvolver uma aplicação em Python com interface gráfica utilizando a biblioteca Tkinter, permitindo organizar e gerenciar o atendimento de pacientes em diferentes especialidades médicas.

O sistema utiliza estruturas de dados do tipo fila FIFO (First In, First Out) e filas de prioridade para organizar a ordem de atendimento.

**Status do projeto:** Em desenvolvimento.

## Objetivos

- Organizar o atendimento dos pacientes.
- Permitir a emissão de senhas normais e preferenciais.
- Gerenciar filas independentes por especialidade médica.
- Garantir prioridade aos pacientes preferenciais.
- Registrar o histórico de atendimentos.
- Apresentar estimativas de tempo de espera.

## Funcionalidades

- [ ] Cadastro e seleção de especialidades médicas.
- [ ] Emissão de senhas normais e preferenciais.
- [ ] Gerenciamento de filas independentes.
- [ ] Atendimento prioritário.
- [ ] Chamada e registro de senhas.
- [ ] Painel de acompanhamento dos atendimentos.
- [ ] Estimativa de tempo de espera.
- [ ] Tratamento de exceções.

##  Especialidades médicas

O sistema contará inicialmente com três especialidades:

- Clínica Geral
- Cardiologia
- Ortopedia

## Estruturas de dados utilizadas

O projeto aplicará os seguintes conceitos:

- **Fila FIFO:** organiza os pacientes conforme a ordem de chegada.
- **Fila de prioridade:** permite que pacientes preferenciais sejam atendidos antes dos pacientes normais.
- **Estruturas independentes:** cada especialidade terá sua própria fila normal e preferencial.

## Regra de prioridade

O atendimento será organizado por especialidade médica.

A regra adotada será:

1. Os pacientes preferenciais serão atendidos primeiro.
2. Dentro da fila preferencial, será respeitada a ordem de chegada (FIFO).
3. Quando não houver pacientes preferenciais aguardando, serão atendidos os pacientes normais, também respeitando a ordem FIFO.

Essa política será aplicada independentemente em cada especialidade.

## Tempo estimado de espera

O sistema utilizará uma média de 30 minutos por atendimento.

A estimativa será calculada considerando a quantidade de pacientes que estão à frente na ordem de atendimento, respeitando a prioridade e a especialidade selecionada.

O cálculo considera o atendimento sequencial em cada especialidade.

## Tecnologias utilizadas

- Python
- Tkinter
- Git
- GitHub
- Visual Studio Code

## Como executar o projeto

1. Instale o Python em seu computador.
2. Clone este repositório:

   ```bash
   git clone URL_DO_REPOSITORIO
   ```

3. Acesse a pasta do projeto:

   ```bash
   cd Sistema-Filas-Clinica-Medica
   ```

4. Execute a aplicação:

   ```bash
   python src/main.py
   ```

**Observação:** O Tkinter normalmente já acompanha a instalação do Python.

## Imagens do sistema

As imagens da interface gráfica serão adicionadas nesta seção após o desenvolvimento da aplicação.

## Integrantes

- Maria Eduarda Oliveira Pereira
- 
-

## Informações acadêmicas

**Instituição:** Centro Universitário UDF  
**Disciplina:** Estrutura de Dados II  
**Professora:** Karla Sartin  
**Ano:** 2026

---

Desenvolvido como atividade acadêmica para aplicação prática dos conceitos de Estrutura de Dados II.
