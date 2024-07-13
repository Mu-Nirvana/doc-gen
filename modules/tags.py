import re
from pathlib import Path

DOC_TAG = 'DOC'
DEFAULT_IGNORE: list[str] = []
DEFAULT_FILE_TYPES: list[str] = ['*']

class Tag():
  def __init__(self, path: Path, tags: list[str]):
    self.path = path
    self.tags = tags

  def print(self):
    output = ''
    output += f'Tags in file: {self.path.as_posix()}\n'
    output += '-----------------\n'
    for tag in self.tags: output += (tag + '\n-----------------\n')
    return output

  def get_file(self):
    return self.path.as_posix()


class TagLocator():
  def __init__(self, directory: Path, ignore: list[str] = DEFAULT_IGNORE, file_types: list[str] = DEFAULT_FILE_TYPES):
    self.directory = directory
    self.ignore = ignore
    self.file_types = file_types
    self.files: list[Path] = []

  # Recursively search a directory for files that are allowed by the file type selector and do not match the ignore regex
  # Returns a list of Path objects
  def index_directory(self, directory: Path) -> list[Path]:
    paths = directory.iterdir()

    documentable = list(filter(self.is_documentable, paths))
    documentable_files = list(filter(lambda path: path.is_file(), documentable))
    subdirs = list(filter(lambda path: path.is_dir(), documentable))

    for dir in subdirs:
      documentable_files.extend(self.index_directory(dir))

    return documentable_files
    

  # Check if a Path object is documentable by file extension and ignore patterns
  def is_documentable(self, path: Path) -> bool:
    ignore_patterns = [re.compile(pattern) for pattern in self.ignore]
    if any([pattern.fullmatch(path.as_posix()) for pattern in ignore_patterns]):
      return False
    
    if path.is_file() and '*' not in self.file_types and path.suffix not in self.file_types:
      return False
    
    return True

  
  # Search the file for all occurances of the documentation tag and return the matches
  def search_file_for_tags(self, path: Path):
    pattern = re.compile(f'<{DOC_TAG}>' + r'(?:.|\n)*?'+ f'</{DOC_TAG}>')
    matches = []
    with path.open(mode='r') as file:
      contents = file.read()
      matches = pattern.findall(contents)

    return matches

  # Remove the tags from the tagged documentation
  def rm_tags(self, tags):
    for i, tag in enumerate(tags):
      tag = tag.replace(f'<{DOC_TAG}>', '')
      tag = tag.replace(f'</{DOC_TAG}>', '')
      
      tags[i] = tag

    return tags

  def locate_tags(self):
    documentable_files = self.index_directory(self.directory)
    tags: list[Tag] = []
    
    for file in documentable_files:
      doc_tags = self.rm_tags(self.search_file_for_tags(file))
      if doc_tags:
        tags.append(Tag(file, doc_tags))

    return tags

def clean_tag_bodies(tag: Tag):
  # Remove leading/trailing whitespace
  for i, tag_body in enumerate(tag.tags):
    tag_body = tag_body.strip()

    # Remove any leading comment symbols and spaces from each line
    lines = tag_body.splitlines()
    for j, line in enumerate(lines):
      line = line.lstrip('# ')
      lines[j] = line
  
    # Recombine lines and remove any trailing newlines
    tag.tags[i] = '\n'.join(lines).rstrip('\n')

  return tag
