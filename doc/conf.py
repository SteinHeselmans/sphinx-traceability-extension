# -*- coding: utf-8 -*-
#
# Example documentation build configuration file, created by
# sphinx-quickstart on Sat Sep  7 17:17:38 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import errno
import os
import subprocess
import sys
from collections import OrderedDict

import mlx.traceability
from pkg_resources import get_distribution

pkg_version = get_distribution('mlx.traceability').version

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../mlx'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'mlx.traceability',
    'sphinx_selective_exclude.eager_only',
    'sphinx_selective_exclude.modindex_exclude',
    'sphinx_selective_exclude.search_auto_exclude',
    'sphinxcontrib.plantuml',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Traceability'
copyright = u'2017, Stein Heselmans'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pkg_version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [os.path.join(os.path.dirname(mlx.traceability.__file__), 'assets')]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Traceability'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'traceability.tex', u'Traceability sphinx plugin documentation',
     u'Stein Heselmans', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'traceability', u'Traceability for sphinx documentation',
     [u'Stein Heselmans'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'traceability', u'Traceability for sphinx documentation',
     u'Stein Heselmans', 'traceability', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Traceability'
epub_author = u'Stein Heselmans'
epub_publisher = u'Stein Heselmans'
epub_copyright = u'2017, Stein Heselmans'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# -- Options for traceability extension ----------------------------------------

# Relationships dictionary. You'll usually need to fit it to your needs.
# Key is the relationship you'll generally set and value is the reverse.
# Use same key/value for bidirectional relationships.
traceability_relationships = {
    'trace': 'traced_by',
    'depends_on': 'impacts_on',
    'fulfills': 'fulfilled_by',
    'implements': 'implemented_by',
    'validates': 'validated_by',
    'ext_toolname': ''
}

traceability_render_relationship_per_item = True

traceability_relationship_to_string = {
    'trace': 'Traces',
    'traced_by': 'Traced by',
    'depends_on': 'Depends on',
    'impacts_on': 'Impacts on',
    'fulfills': 'Fulfills',
    'fulfilled_by': 'Fulfilled by',
    'implements': 'Implements',
    'implemented_by': 'Implemented by',
    'validates': 'Validates',
    'validated_by': 'Validated by',
    'ext_toolname': 'Reference to toolname'
}

traceability_external_relationship_to_url = {
    'ext_toolname': 'http://toolname.company.com/field1/field2/workitem?field3'
}

traceability_json_export_path = '_build/exported_items.json'

# OrderedDict([('regex', (default, :hover+:active, :visited)), ...])
# OrderedDict generates a dict with a deterministic order, used to prioritize the regexes, top to bottom
traceability_hyperlink_colors = OrderedDict([
    (r'^RQT|r[\d]+', ('#7F00FF', '#b369ff')),
    (r'^[IU]TEST_REP', ('rgba(255, 0, 0, 1)', 'rgba(255, 0, 0, 0.7)', 'rgb(200, 0, 0)')),
    (r'^[IU]TEST', ('goldenrod', 'hsl(43, 62%, 58%)', 'darkgoldenrod')),
    (r'^SYS_', ('', 'springgreen', '')),
    (r'^SRS_', ('', 'orange', '')),
])

# traceability_item_no_captions = True
# traceability_list_no_captions = True
# traceability_matrix_no_captions = True
# traceability_tree_no_captions = True
# traceability_render_attributes_per_item = False
# traceability_collapse_links = True

# -- Options for checklist feature ----------------------------------------
from decouple import config

traceability_checklist = {
    'private_token': config('PRIVATE_TOKEN', ''),
    'api_host_name': config('API_HOST_NAME', 'https://api.github.com'),
    'project_id': config('PROJECT_ID', 'melexis/sphinx-traceability-extension'),
    'merge_request_id': config('MERGE_REQUEST_ID', '121,138'),
    'attribute_name': config('ATTRIBUTE_NAME', 'checked'),
    'attribute_to_str': config('ATTRIBUTE_TO_STRING', 'Answer'),
    'attribute_values': config('ATTRIBUTE_VALUES', 'yes,no'),
}

# Point to plantuml jar file
# confirm we have plantuml in the path
if 'nt' in os.name:
    plantuml_path = subprocess.check_output(["where", "/F", "plantuml.jar"])
    if not plantuml_path:
        print("Can't find 'plantuml.jar' file.")
        print("You need to add path to 'plantuml.jar' file to your PATH variable.")
        sys.exit(os.strerror(errno.EPERM))
    plantuml = plantuml_path.decode("utf-8")
    plantuml = plantuml.rstrip('\n\r')
    plantuml = plantuml.replace('"', '')
    plantuml = plantuml.replace('\\', '//')
    plantuml = 'java -jar' + ' ' + plantuml
else:
    plantuml_path = subprocess.check_output(["whereis", "-u", "plantuml"])
    if not plantuml_path:
        print("Can't find 'plantuml.jar' file.")
        print("You need to add path to 'plantuml.jar' file to your PATH variable.")
        sys.exit(os.strerror(errno.EPERM))

def setup(app):

    from traceability import ItemDirective
    # New directive types: treated exactly as ``item`` directive, but
    # using a different name. Item template can be customized for
    # these types
    app.add_directive('requirement', ItemDirective)
