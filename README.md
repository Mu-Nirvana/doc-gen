# doc-gen
Compile documentation from source files into a single output

## Demo
To demo the parsing on the this tool run:  
`python3 main.py . --text`

See the [Demo Output](#demo-output) section for the markdown output of this command

## Usage
To parse a project for `<DOC>` tags run the script  
`python3 main.py <directory> [--output <output>] [--html] [--text]`

### Options
- `--output` output to file instead of stdout
- `--html` write markdown formatted output as html
- `--text` write output as plain text

# Demo Output
## Docs From main.py
Command line innvocation requires a directory input and has optional flags for an output file (--output) and output format (--html or --text)<br>
## Docs From modules/outputs.py
generate_text() takes a list of Tag objects and creates a formatted plain text output of all the Tag object contents<br>
genreate_markdown() takes a list of Tag objects and creates a formatted markdown output of all the Tag object contents<br>
convert_markdown_to_html() takes a markdown formatted string and converts it to the appropriate html format
NOTE: Can only be invoked if the markdown module is installed<br>
write_output() takes an output string and a target file as a Path object and writes the text in the string to the file<br>
## Docs From modules/tags.py
The tag locator has the following defaults:
- DOC_TAG = 'DOC'
- DEFAULT_IGNORE = []
- DEFAULT_FILE_TYPES = ['*']<br>
The Tag object is constructed with a Path object for the file the tags orignated from and a list of strings for the tag contents
The Tag object has a print() method that returns a plain text formatted representation of the tag contents
The get_file() method returns the full file path as a string<br>
The TagLocator class takes a Path object for the directory and optionally a list of path regex patterns to ignore and a list of file extensions to search
The locate_tags() method recursively searches the directory for tagged documentation and returns a list of Tag objects<br>
The clean_tag_bodies() function takes a Tag object and strips leading and trailing whitespace from the tag bodies as well as removing extra comment symbols from the interior of the tag bodies<br>
