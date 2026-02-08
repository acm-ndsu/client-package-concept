CURRENT_YEAR = 2026
CLIENT_PACKAGE_REPO_URL = 'https://github.com/'
DISCORD_URL = 'https://discord.gg/'
SHOW_ANNOUNCEMENT = True
ANNOUNCEMENT = '(12:38 p.m.) UPDATED <a href="tips.html">TIPS & TRICKS</a> AND ADDED <a href="controls.html#pathfinding">SAMPLE A* CODE</a>'

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = f'Byte-le Royale {CURRENT_YEAR}'
copyright = f'1974-{CURRENT_YEAR}, NDSU ACM'
author = f'NDSU ACM Byte-le {CURRENT_YEAR} Dev Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = [
    '_static'
]
html_css_files = [
    'styles/custom.css'
]

html_title = f'{CURRENT_YEAR} Byte-le Royale Documentation'
html_logo = '_static/images/bytele-logo.png'
html_theme = 'shibuya'
html_theme_options = {
    'accent_color': 'indigo',
    'github_url': CLIENT_PACKAGE_REPO_URL,
    'discord_url': DISCORD_URL,
    'announcement': ANNOUNCEMENT if SHOW_ANNOUNCEMENT else ''
}
