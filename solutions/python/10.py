def remove_url_anchor(url):
  import re
  return re.sub(r'#.*', '', url)