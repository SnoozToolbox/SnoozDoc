# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Snooz Toolbox'
copyright = '2023, Valorisation Recherche HSCM, Société en Commandite'
author = 'Karine Lacourse, David Lévesque, Mohammad Hasan Azad'

release = 'beta-2.0.0'
version = 'beta-2.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
#import sphinx_pdj_theme
html_theme = 'sphinx_rtd_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# Add custom CSS
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'
