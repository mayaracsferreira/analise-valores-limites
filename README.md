# Testes Funcionais: Análise de Valores Limites

## Descrição da atividade
https://aluguebug.herokuapp.com/ajuda

## Instituição
[Faculdade de Tecnologia do Estado de São Paulo Professor Jessen Vidal](https://fatecsjc-prd.azurewebsites.net/)

## Aluna
- Mayara Ferreira

## Professor
- Fabricio Galende

## Disciplina 
Laboratório de Desenvolvimento em Banco de Dados VI

## Requisitos
- Python 3.8
- PIP 20.x

## Configuração e execução
Clonar esse repositório
```
git clone https://github.com/mayaracsferreira/analise-valores-limites.git
```

Entrar na pasta do projeto
```
cd analise-valores-limites
```

### Valor nominal
500

### Testes funcionais:

Entrar na pasta da entrega
```
cd entrega_testes_funcionais
```

Instalação das dependências
```
pip install -r requirements.txt
```

#### Analise de valores limites

Execução testes (linha de comando)
```
pytest testes_funcionais.py
```

Gerar relatório em HTML
```
test-report.bat
```

Visualizar arquivo *report.html* no navegador

Video da apresentação [aqui](https://drive.google.com/file/d/1sMjAMuNB9rw12HjDlWG6rC2WBkyojLlF/view?usp=sharing)

#### Testes funcionais parametrizados:
Execução testes (linha de comando)
```
pytest testes_parametrizados.py
```

Gerar relatório em HTML
```
test-param-report.bat
```

Visualizar arquivo *report-parametrized.html* no navegador

Video da apresentação [aqui](https://drive.google.com/file/d/1ViAE6t6Z6rGa-IFLM1Axr4JIOSzMNPvM/view?usp=sharing)
