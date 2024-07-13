# doc-gen
Compile documentation from source files into a single output

## Demo
To demo the parsing on the `test` directory run:  
`python3 main.py test --text`

## Usage
To parse a project for `<DOC>` tags run the script  
`python3 main.py <directory> [--output <output>] [--html] [--text]`

### Options
- `--output` output to file instead of stdout
- `--html` write markdown formatted output as html
- `--text` write output as plain text
