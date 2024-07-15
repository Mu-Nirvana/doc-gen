from modules.tags import Tag
from pathlib import Path
HTML_CONVERSION = True
try:
  import markdown
except ImportError:
  HTML_CONVERSION = False

# <DOC> generate_text() takes a list of Tag objects and creates a formatted plain text output of all the Tag object contents </DOC>
def generate_text(tags: list[Tag]):
  output = ''
  for tag in tags:
    output += tag.print()

  return output

# <DOC> genreate_markdown() takes a list of Tag objects and creates a formatted markdown output of all the Tag object contents </DOC>
def generate_markdown(tags: list[Tag]):
  output = ''
  for tag in tags:
    output += f'## Docs From {tag.get_file()}\n'
    for tag_body in tag.tags:
      output += f'{tag_body}<br>\n'
  
  return output

# <DOC> convert_markdown_to_html() takes a markdown formatted string and converts it to the appropriate html format
# NOTE: Can only be invoked if the markdown module is installed </DOC>
def convert_markdown_to_html(md: str):
  if not HTML_CONVERSION:
    raise Exception('markdown module required to convert to html')

  return markdown.markdown(md)

# <DOC> write_output() takes an output string and a target file as a Path object and writes the text in the string to the file </DOC>
def write_output(output: str, file: Path):
  with file.open(mode='w') as f:
    f.write(output)

