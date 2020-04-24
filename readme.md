# Observatorio COVID-19 UFJ

Este observatório é uma iniciativa do Bacharelado em Ciência da Computação (BCC) da Universidade Federal de Jataí (UFJ).

## Início - Principais características

* Graficos de estatisticas por cidades
* Implementação de sistema em plataforma Web totalmente responsiva;
* Persistência de banco de dados, utilizando modelo relacional;

### Pre-requisitos

Requisitos minimos para utilização do sistema:

```
Python 3.6+
```
```
Django 2.0.2+
```

### Instalação

A seguir um passo a passo para a instalação do sistema e suas dependências

* clone o projeto:
```
git clone https://github.com/bispojr/observatorio-ufj-covid19.git
```
* Certifique-se de que o Python e o Ambiente Virtual( virtualenv ou pipenv) estejam instalados. Caso nao estejam sugiro este [link](https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed) de instalacao.
Crie o ambiente virtual e instale os pacotes.
 ```
 cd observatorio-ufj-covid19
 pipenv shell (ira ativar o ambiente virtual)
 
 pipenv install (para instalar as dependencias)
```
* Execute as migrações do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```
* Start do projeto:

```
python manage.py runserver
```

<!-- ## Executando Testes



### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->

