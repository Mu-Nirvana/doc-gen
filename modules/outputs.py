from modules.tags import Tag
from pathlib import Path
HTML_CONVERSION = True
try:
  import markdown
except ImportError:
  HTML_CONVERSION = False

def generate_text(tags: list[Tag]):
  output = ''
  for tag in tags:
    output += tag.print()

  return output

def generate_markdown(tags: list[Tag]):
  output = ''
  for tag in tags:
    output += f'## Docs From {tag.get_file()}\n'
    for tag_body in tag.tags:
      output += f'{tag_body}<br>\n'
  
  return output

def convert_markdown_to_html(md: str):
  if not HTML_CONVERSION:
    raise Exception('markdown module required to convert to html')

  return markdown.markdown(md)

def write_output(output: str, file: Path):
  with file.open(mode='w') as f:
    f.write(output)

