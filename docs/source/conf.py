# -*- coding: utf-8 -*-

project = u'flask_mod_struct'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.3.0'
release = u'https://github.com/vroncevic/flask_mod_struct/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'flask_mod_structdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'flask_mod_struct.tex', u'flask\\_mod\\_struct Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'flask_mod_struct', u'flask_mod_struct Documentation',
    [author], 1
)]
texinfo_documents = [(
    master_doc, 'flask_mod_struct', u'flask_mod_struct Documentation',
    author, 'flask_mod_struct', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
