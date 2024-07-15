import click
from modules.tags import TagLocator, clean_tag_bodies
from modules.outputs import *
from pathlib import Path

# <DOC> Command line innvocation requires a directory input and has optional flags for an output file (--output) and output format (--html or --text) </DOC>
@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--output', type=click.Path(), default=None, help="Output file")
@click.option('--html', is_flag=True, help="Write output as html instead of markdown")
@click.option('--text', is_flag=True, help="Write output as text instead of markdown")
def main(directory, output, html, text):
  """Search DIRECTORY for doc tags"""
  # Create a locator to find tags in the working directory
  locator = TagLocator(Path(directory), ignore=[r'.*\/ignoreme.*'], file_types=['.py', '.txt'])
  # Locate tags
  tags = locator.locate_tags() 

  # Clean tags
  for i, tag in enumerate(tags):
    tags[i] = clean_tag_bodies(tag)

  # Genreate output 
  docs = ''
  if text:
    docs = generate_text(tags)
  else:
    docs = generate_markdown(tags)
    if html:
      docs = convert_markdown_to_html(docs)

  if output != None:
    write_output(docs, Path(output))

  else: print(docs)


if __name__ == "__main__":
  main()
