<h1>
    <a href="https://www.dio.me/">
     <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png"></a>
    <span>Formação Python Developer</span>
</h1>


# :computer: Desafio de projeto: 

## Descomplicando a Criação de Pacotes

Esse desafio compreende a criação de pacotes python. Eu gerei o pacote usando como base o projeto do desafio bancário em POO:

https://github.com/tsdes-santiago/projetoDIOsistemaBancarioPOO

# :bulb: Solução do desafio

Pacote estruturado da seguinte forma:

<img src="pacote_sistema_bancario.png">

Arquivo para a instalação gerado com o commando, o qual cria o diretório "dist":

<code>$python setup.py sdist bdist_wheel </code>

Instalado para teste, dentro do diretório "dist":

<code> $pip install sistema_bancario-0.0.1-py3-none-any. </code>

O projeto não foi publicado no Test Pypi. 
