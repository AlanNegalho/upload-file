# Consumindo Arquivo XLSX

  Nesse desafio iremos avaliar suas habilidades em:
* Python
* Django
* Django REST Framework

## Descrição do projeto
Você recebeu um arquivo com dados de alguns clientes que precisam ser
importadas
para um banco de dados. Será necessária a criação de dois endpoints para que os
dados sejam consumidos. O arquivo data.xlsx está disponível para realizar os seus
testes necessários.
Modelagem do banco é livre
## :hammer: Funcionalidades do projeto
* Ter uma tela (via um formulário) para fazer o upload do excel.
* Realizar carga de dados.
* Transformar coluna "nascimento" para data.
## Após a carga de dados você deve criar os dois endpoints abaixo usando DRF:
* GET: retornando mulheres de mereen.
* GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista de
pessoas, ordenanda por idade. 

## 📁 Acesso ao projeto

**É possível baixar ou acessar o código fonte do projeto no [Link](https://github.com/AlanNegalho/apiarquivo.git) ou clone o repositório**
```python
git clone https://github.com/AlanNegalho/apiarquivo.git
```

## 🛠️ Abrir e rodar o projeto

Após acessar o código fonte do projeto faça o download através do git clone ou no formato zip. Podemos agora iniciamos a instalação da aplicação em nossa máquina. Lembrando que utilizaremos o ambiente virtual para criação do projeto.

## Upgrade necessários

Acesse a pasta diretoria da aplicação
```python
cd apifile
```
Atualizar o sistema caso esteja no Linux

```python
sudo apt update 
```


```python
sudo apt -y upgrade
```

Instalar o pip3


```python
sudo apt install python3-pip
```

Instalar ferramentas adicionais


```python
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

Instalando o env e virtualenv


```python
sudo apt install -y python3-venv
```


```python
sudo apt install python3-virtualenv
```
Instalando no Windows

```python
pip install virtualenv
```
Instalando no MacOS

```python
sudo pip uninstall virtualenv

sudo -H pip install virtualenv
```

## Criando o ambiente virtual
Criando seu ambiente virtual. Vamos chamá-lo venv

No Linux
```python
python3 -m venv venv
```

Criando o seu ambiente virtual no Windows 

```python
python -m venv venv
```

Criando seu ambiente virtual no MacOS

```python
virtualenv -p python3 <desired-path>


virtualenv -p python3 env

```

Ative o ambiente virtual 

No Windows
```python
venv\Scripts\activate.bat
```
No linux
```python
. venv/bin/activate
```
Para desativar o ambiente virtual, na pasta


```python
deactivate 
```

```python
quit()
```

## Bibliotecas utilizadas no desenvolvimento da aplicação
- Django==4.1.4
- django-filter==22.1
- django-import-export==3.0.1
- djangorestframework==3.14.0
- django-jazzmin 2.6.0(Utilizada para estilizar o admin)

1.   https://pypi.org/project/Django/
2.   https://pypi.org/project/django-filter/
3.   https://pypi.org/project/django-import-export/
4.   https://pypi.org/project/djangorestframework/
5.   https://pypi.org/project/django-jazzmin/

Instale todas as bibliotecas acima através do requirements.txt arquivo localizado na pasta da aplicação.

```python
pip install -r requirements.txt
```
Realize  as migrations e o migrate:
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
Após realizar as migrações, crie um super usuário pra realizar acesso ao admin do Django. Adicione o nome do usuário logo após o comando.
```python
python manage.py createsuperuser
```
Inicie o servidor:
```python
python manage.py runserver
```
Acesse o link da aplicação:
```python
http://127.0.0.1:8000/
```
Assim será a página com a exibição, dois endpoints abaixo usando
DRF:

* GET: retornando mulheres de mereen.
* GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista
de pessoas, ordenada por idade.

Pode-se observar que ao acessarmos a página pela primeira vez nota-se que não estamos logados e possivelmente não teremos acesso ao formulário para o upload do arquivo XLSX. Para resolvermos isso no link da aplicaçoa http://127.0.0.1:8000/ adiciaonaremos um novo endedreços de pagina chamado admin entao o novo link fica http://127.0.0.1:8000/admin  faça o ligin com os dados superuser criados anteriormente, retorne a página principal de aplicação http://127.0.0.1:8000/
![screen02_cropped](https://user-images.githubusercontent.com/107214420/210414243-85613bfc-5788-4153-be3b-965433c30525.jpg)

Podemos observa no canto superior direito que estamos logados no sistema, assim podemos acessar o endpoint "meeren": "http://127.0.0.1:8000/meeren/", 
![2 end (2)](https://user-images.githubusercontent.com/107214420/209589524-632034eb-824a-4265-b042-90b2ffa0c7a1.png)

Logo após o acesso faça o upload do arquivo data.xlsx através do formulário upload_arquivo.
![Person List – Django REST framework - Google Chrome 26_12_2022 20_42_41 (2)](https://user-images.githubusercontent.com/107214420/209588855-702a9628-2a1c-410c-af1e-bb45687f5249.png)

Depois do arquivo data.xlsx ser carregado o resultado será assim:
![Person List – Django REST framework - Google Chrome 26_12_2022 20_48_07 (3)](https://user-images.githubusercontent.com/107214420/209589602-9a7e209d-ad60-4f3c-b174-b1e7077400f2.png)


⌨️ com ❤️ por [Alan Negalho](https://github.com/AlanNegalho) 😊
