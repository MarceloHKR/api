# API

## O que são APIs?

API é a sigla para Application Programming Interface, que em português significa Interface de Programação de Aplicações. As APIs são um conjunto de regras e definições que permitem a comunicação entre os softwares. Elas são responsáveis por estabelecer a forma como os componentes de software devem interagir entre si.

## Para que servem as APIs?

As APIs são utilizadas para permitir a comunicação entre diferentes softwares. Elas são responsáveis por definir a forma como os componentes de software devem interagir entre si.

## APIs remotas e web services

As APIs remotas são aquelas que estão disponíveis em um servidor remoto, ou seja, fora do ambiente de desenvolvimento. Já os web services são um tipo de API que utiliza a internet para se comunicar.
Pode se dizer que todos os web services são APIs, mas nem todas as APIs são web services.

## Tipos de APIs

### APIs SOAP

SOAP é a sigla para Simple Object Access Protocol, que em português significa Protocolo Simples de Acesso a Objetos. As APIs SOAP são baseadas em XML e são utilizadas para acessar serviços web.
Este tipo de API é mais antigo e menos utilizado atualmente.

### APIs REST

REST é a sigla para Representational State Transfer, que em português significa Transferência de Estado Representacional. As APIs REST são baseadas em HTTP e são utilizadas para acessar serviços web.
Este tipo de API é mais moderno e mais utilizado atualmente.

## APIs públicas e privadas

As APIs públicas são aquelas que estão disponíveis para qualquer pessoa utilizar. Já as APIs privadas são aquelas que estão disponíveis apenas para um grupo restrito de pessoas.
Geralmente as APIs públicas são utilizadas para disponibilizar serviços web, enquanto as APIs privadas são utilizadas para integrar sistemas internos.

## Por que utilizar APIs?

As APIs são utilizadas para permitir a comunicação entre diferentes softwares. Elas são responsáveis por definir a forma como os componentes de software devem interagir entre si.
As APIs são muito utilizadas para integrar sistemas e disponibilizar serviços web.
Usando uma API, é possível acessar um serviço web de forma programática, ou seja, sem a necessidade de interação humana. Também é possível integrar sistemas internos de uma empresa, permitindo que eles se comuniquem entre si.
As APIs também permitem que os desenvolvedores criem novos serviços web, utilizando serviços já existentes como base. Além disso, não se faz necessário saber como o serviço foi implementado, apenas como utilizá-lo.

## Exemplos de APIs

### API do Google Maps

A API do Google Maps é uma API pública que permite acessar os serviços de mapas do Google. Ela é muito utilizada para integrar mapas em sites e aplicativos.

## Tipos de requisições HTTP

### GET

A requisição GET é utilizada para obter informações de um servidor. Ela é a mais comum e é utilizada para acessar páginas web, imagens, arquivos, etc.

### POST

A requisição POST é utilizada para enviar informações para um servidor. Ela é utilizada para enviar formulários, fazer upload de arquivos, etc.

### PUT

A requisição PUT é utilizada para atualizar informações em um servidor. Ela é utilizada para atualizar um recurso existente.

### DELETE

A requisição DELETE é utilizada para excluir informações de um servidor. Ela é utilizada para excluir um recurso existente.

## Códigos de status HTTP

### 200 OK

O código de status 200 OK indica que a requisição foi bem sucedida.

### 201 Created

O código de status 201 Created indica que a requisição foi bem sucedida e um novo recurso foi criado.

### 400 Bad Request

O código de status 400 Bad Request indica que a requisição não pôde ser processada devido a um erro no cliente.

### 401 Unauthorized

O código de status 401 Unauthorized indica que a requisição não pôde ser processada devido a falta de autenticação.

### 403 Forbidden

O código de status 403 Forbidden indica que a requisição não pôde ser processada devido a falta de permissão.

### 404 Not Found

O código de status 404 Not Found indica que o recurso solicitado não foi encontrado.

### 500 Internal Server Error

O código de status 500 Internal Server Error indica que a requisição não pôde ser processada devido a um erro no servidor.

## APIs REST com Python

Para acessar uma API REST com Python, é possível utilizar a biblioteca requests. Ela permite fazer requisições HTTP de forma muito simples.

```python

import requests

response = requests.get('https://api.github.com')

print(response.status_code)

```

### Autenticação e Autorização

Autenticação é o processo de verificar a identidade de um usuário. Autorização é o processo de verificar se um usuário tem permissão para acessar um recurso.

Para acessar uma API REST que requer autenticação, é possível utilizar a biblioteca requests. Ela permite fazer requisições HTTP de forma muito simples.

#### Autenticação básica

Este tipo de autenticação é feito enviando o nome de usuário e a senha no cabeçalho da requisição.

```python

import requests

response = requests.get('https://api.github.com', auth=('user', 'pass'))

print(response.status_code)

```

#### Autenticação por token

Este tipo de autenticação é feito enviando um token no cabeçalho da requisição.
Os tipos de autenticação por token mais comuns são o Bearer, API Key, OAuth, etc.

```python

import requests

headers = {
    'Authorization': 'Bearer

Quanto a autorização, é possível utilizar a biblioteca requests. Ela permite fazer requisições HTTP de forma muito simples.

```python

import requests

headers = {
    'Authorization

response = requests.get('https://api.github.com', headers=