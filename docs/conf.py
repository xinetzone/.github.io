#!/usr/bin/env python

# xinetzone 构建的配置文件，
# 由 `ablog start` 在 2021 年 10 月 24 日星期日 22:28:16 创建。
#
# 注意不是所有可能的配置值都出现在这个文件中。
# 所有的配置值都有一个默认值；被注释掉的值是用来显示默认值的。

import os
import sys
import ablog
import alabaster

# -- ABlog 的常规选项 ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
# 一个相对于配置目录的博客档案页的路径。
blog_path = 'blog'

# The "title" for the blog, used in active pages.  Default is ``'Blog'``.
# 博客的 “标题”，在活动页面中使用。默认为 ``'Blog'``。
blog_title = "xinetzone Blog"

# 网站的基本 URL，生成 feeds 时需要。
# 例如，blog_baseurl = "http://example.com/"
blog_baseurl = "https://xinetzone.github.io/"

# 选择只对帖子标题进行存档。只归档标题可以加快项目建设的速度。
# blog_archive_titles = False

# --    博客作者、语言和位置 -------------------------------------------------

# 一个作者名字的字典，映射到作者的完整显示名称和链接。
# 字典的键值应该在 ``post`` 指令中使用，以指代作者。默认是 ``{}``。
blog_authors = {
    "lxw": ("刘新伟", None),
}

# 语言代码名称的字典，映射到这些语言的完整显示名称和链接。
# 类似于 :confval:`blog_authors`，
# 字典的键应该在 `post` 指令中使用，以指代位置。默认是 `{}`。
blog_languages = {
    'zh': ('Chinese', None),
    'en': ('English', None)
}

# 一个位置名称的字典，映射到这些位置的完整显示名称和链接。
# 类似于 :confval:`blog_authors`，字典的键应该在 ``post`` 指令中使用，以引用位置。
# 默认是 ``{}``.
blog_locations = {
    # 'Earth': ('The Blue Planet', 'https://en.wikipedia.org/wiki/Earth'),
    "daobook": ("Daobook", "https://daobook.github.io")
}

# -- 博客帖子相关 --------------------------------------------------------

# 帖子的日期格式。
# post_date_format = '%%b %%d, %%Y'

# 将作为文章摘录显示的段落数（默认为 ``1``）。 
# 设置此 ``0`` 将导致在存档页面中不显示帖子摘录。可以使用每个帖子设置此选项
# post_auto_excerpt = 1

# 图片的索引，将显示在文章的摘录中。
# 默认是 ``0``，意味着没有图片。
# 设置为 ``1`` 将包括第一张图片（如果有的话）到摘录中。
# 这个选项可以在每个帖子的基础上使用 :rst:dir:`post` 指令选项 ``image`` 来设置。
post_auto_image = 1

# 重定向页面在刷新页面之前等待的秒数（默认为 ``5``），以重定向到帖子。
# post_redirect_refresh = 5

# 当 ``True`` 时，帖子的标题和摘要总是从包含 :rst:dir:`post` 指令的部分，
# 而不是从文档中提取。这是当 :rst:dir:`post` 在一个文档中被多次使用时的行为。
# 默认是`False`。
# post_always_section = False

# 当 ``False`` 时，:rst:dir:`orphan` 指令不会为每个帖子自动设置。
# 如果没有这个指令，Sphinx 会对没有通过另一个文件明确引用的帖子发出警告。
#  :rst:dir:`orphan` 如果是 false，也可以在每个帖子的基础上设置。
# 默认是`True'。
# post_auto_orphan = True

# -- ABlog 侧边栏 -------------------------------------------------------

# 在你的 HTML 输出中，有七个侧边栏可以包括。postcard.html 提供有关当前帖子的信息。
# recentposts.html 列出最近的五个帖子。
# 其他的侧边栏提供了一个链接到为每个标签、类别和年份生成的档案页。
# 此外，还有 authors.html, languages.html, and locations.html 侧边栏，
# 链接到作者和位置的档案页。
html_sidebars = {
    '**': ['about.html',
           'postcard.html', 'navigation.html',
           'recentposts.html', 'tagcloud.html',
           'categories.html',  'archives.html',
           'searchbox.html',
           ],
}

# -- Blog Feed 选项 --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
# 通过设置 :confval:`blog_baseurl` 配置变量来转动 feeds。
# 选择按作者、地点、标签、类别和年份创建 feeds，默认为 ``False``。
blog_feed_archives = True

# 选择在博客 feeds 中显示全文，默认为 ``False``。
# blog_feed_fulltext = False

# 博客 feed 的副标题，默认为 ``None``。
# blog_feed_subtitle = None

# 选择只 feed 文章标题，默认为 ``False``。
# blog_feed_titles = False

# Specify custom Jinja2 templates for feed entry elements:
#     `title`, `summary`, or `content`
# 为饲料条目元素指定自定义的 Jinja2 模板：
# `title`、`summary` 或 `content`
# 例如，添加一个额外的 feed，用于发布到社交媒体：
# blog_feed_templates = {
#     # 使用默认值，不使用模板
#     "atom": {},
#     # 创建适合在社交媒体上发布的内容文本
#     "social": {
#         # 将 tags 格式化为 hashtags，并附加到内容上
#         "content": "{ title }{% for tag in post.tags %}"
#         " #{ tag.name|trim()|replace(' ', '') }"
#         "{% endfor %}",
#     },
# }
# 默认情况下。创建一个没有任何模板的 `atom.xml` feed
# blog_feed_templates = {"atom": {} }

# 指定在 feeds 中包含的最近帖子的数量，默认为所有帖子都是 ``None``。
# blog_feed_length = None

# -- Font-Awesome 选项 -----------------------------------------------------

# ABlog 模板将使用 Font Awesome 图标，如果以下情况之一是 ``True``的话：

# 链接到 `Bootstrap CDN`_ 的 `Font Awesome`_，在侧边栏和文章页脚使用图标。
# 默认: ``None``.
# fontawesome_link_cdn = None

# Sphinx_ 主题已经链接到 `Font Awesome`_。 
# 默认值：``False``
# fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# 或者，你可以用配置选项 fontawesome_css_file 提供 `Font Awesome`_ :file:`.css` 的路径。
# （默认是`None`），它将被 ABlog 在 HTML 输出中链接到。
# fontawesome_css_file = None

# -- Disqus 集成 -------------------------------------------------------

# 你可以通过设置 ``disqus_shortname`` 变量来启用 Discuz_。
# Disqus_ 是博客的短名称。
# disqus_shortname = None

# 选择 disqus 是非帖子的页面，默认为 ``False``。
# disqus_pages = False

# 选择将 disqus 的帖子作为草稿（没有发布日期）。
# 默认为 ``False``。
# disqus_drafts = False

# -- Sphinx 选项 -----------------------------------------------------------

# 如果你的项目需要一个最小的 Sphinx 版本，在这里说明。
needs_sphinx = '1.6'

# 在这里添加任何 Sphinx 插件模块的名字，以字符串的形式。
# 它们可以是 Sphinx 自带的插件（命名为 `sphinx.ext.*`）或你自定义的。
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'alabaster',
    'ablog',
]

# 相对于这个目录，添加任何包含模板的路径。
templates_path = ["_templates", ablog.get_html_templates_path()]

# 源文件名的后缀。
source_suffix = ".rst"

# 源文件的编码方式。
# source_encoding = 'utf-8-sig'

# 主 toctree 文档。
master_doc = "index"

# 项目的一般信息
project = "xinetzone"
copyright = "2021, Xinwei Liu"
author = "Xinwei Liu"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# 你所记录的项目的版本信息，作为 |version| 和 |release| 的替代，
# 也用于整个构建的文档的其他地方中使用。
#
# 简短的 X.Y 版本。
version = "0.0"
# 完整版本，包括 alpha/beta/rc 标签。
release = "alpha"

# 由 Sphinx 自动生成的内容的语言。支持的语言列表请参考文档。
#
# 如果你通过 gettext catalogs 做内容翻译，也会用到这个。
# 通常你在这些情况下从命令行设置 ``language``。
language = "zh_CN"

# 替换 |today| 有两种选择：一种是，你把 today 设置为某个非 false 的值，
# 然后就用它：
# today = ''
# 否则，today_fmt 被用作调用 strftime 的格式。
# today_fmt = '%%B %%d, %%Y'

# 模式列表，相对于源目录，匹配文件和目录的列表，
# 这些文件和目录在寻找源文件时要被忽略。
exclude_patterns = [""]

# 用于所有文档的 reST 默认角色（用于此标记：`text`）。
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'github_button': False,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%%b %%d, %%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh
html_search_language = 'zh'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "xinetzonedoc"
