import click
from modules.tags import TagParser
from pathlib import Path

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory):
  """Search DIRECTORY for doc tags"""
  parser = TagParser(Path(directory), ignore=[r'.*\/ignoreme.*'], file_types=['.py', '.txt'])
  tags = parser.locate_tags() 

  for tag in tags:
    tag.print()

if __name__ == "__main__":
  main()
