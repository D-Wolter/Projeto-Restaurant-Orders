# Boas-vindas ao repositório do Restaurant Orders!

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#construido-com">Construido Com</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#ambiente-virtual">Ambiente virtual</a></li>
        <li><a href="#tests">Tests</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#contato">Contato</a></li>
    <li><a href="#agradecimentos">Agradecimentos</a></li>
  </ol>
</details>

## Sobre o Projeto



### Habilidades trabalhadas
- Praticar o conceito de `Hashmaps` através das estruturas de dados `Dict` e `Setdo` Python;
- Praticar a ferramenta `Pandas` junto a sua estrutura de dados `DataFrame`;
- Praticar os conhecimentos de testes de software;
- Praticar os conhecimentos de orientação a objetos.

### Construido Com

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![pytest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=ffdd54)
* ![pandas](https://img.shields.io/badge/pandas-3670A0?style=for-the-badge&logo=pandas&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Começando

### Instalação

1. Clonar o repositorio

        git clone git@github.com:D-Wolter/Projeto-Restaurant-Orders.git

2. Entrar na pasta project-restaurant-orders

        cd ./trybe-restaurant-orders

### Ambiente virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

        python3 -m venv .venv

2. **ativar o ambiente virtual**

        source .venv/bin/activate

3. **instalar as dependências no ambiente virtual**

        python3 -m pip install -r dev-requirements.txt

> Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

### Tests

 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

    python3 -m pytest

  <details>
  <summary>Mais comandos</summary>
  
   O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Uso

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
