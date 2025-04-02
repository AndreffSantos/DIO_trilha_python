# Objetivo Geral

Separar as funções existentes de saque , depósito e extrato em funções separadas.
Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária.

## Separação em funções 

Devemos criar funções para todas as operações do sistema.
Para exercitar tudo o que aprendemos neste módulo, cada função
vai ter uma regra na passagem de argumentos.
O retorno e a forma como serão chamadas, ode ser definida
por você da forma que achar melhor.

### Saque

A função saque deve receber os argumentos apenas por nome.
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno: saldo e extrato.

### Deposito

A função deposito deve receber os argumentos apenas por posição.
Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo, extrato.

### Extrato

A função extrato deve receber os arguntos por posição e nome.
Agumentos posiconais: saldo.
Argumentos nomeados: extrato.

## Novas Funções

Precisamos criar duas novas funções: criar usuário e criar conta corrente.
Fique a vontade para adicionar mais funções.

### Criar Usuário

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf, e endereço
O endereço é uma string no formato "logradouro, número - bairro - cidade/sigla do estado" (Não precisa se preocupar com a validação deste formato).
Devem ser armazenados somente os números dos cpf. Não podem ser cadastrados 2 usuários com mesmo cpf.

### Criar Conta Corrente

O Programa eve armazenar contas em uma lista, uma conta é composta por: agência, número de conta, e usuário.
O numero de conta é sequencial , iniciado por 1.
O número de agência é fixo: "0001".
O usuário pode ter mais de uma conta, mas cada conta tem um usuário.