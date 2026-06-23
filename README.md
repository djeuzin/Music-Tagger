# Music tagger
Adiciona tags a arquivos de áudio.

# Uso

Clone o repositório no diretório desejado.

No diretório `Music-Tagger` inicie o ambiente virtual e instale as dependências:

```Bash
.../Music-Tagger $ python3 -m venv .venv
.../Music-Tagger $ source .venv/bin/activate
(.venv) .../Music-Tagger $ pip install -r requirements.txt
```

##  Funcionalidades

- **Upload de Músicas**: Aceita arquivos de música enviados pelo usuário.
- **Integração MusicBrainz**: Busca automática de metadados via API oficial.
- **Edição de Tags**: Interface amigável para alterar títulos, artistas, álbuns e anos.
- **Salvar/Exportação**: Atualização dos metadados no arquivo ou banco de dados.

## Tecnologias Utilizadas

- **Backend**: Python (Flask) + biblioteca `musicbrainzngs`
- **Frontend**: HTML5, CSS3, JavaScript 


# Integrantes

- Rafael Freire
- Tamires Morais
