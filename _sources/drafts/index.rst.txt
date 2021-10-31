==========
缓存区
==========

有待探讨的 Python 模块：

- `feedgen`__
- `Invoke`__ 
- `Jinja`__

__ https://github.com/lkiesow/python-feedgen
__ https://www.pyinvoke.org/
__ https://jinja.palletsprojects.com/

python setup.py extract_messages -o ablog/locales/sphinx.pot
python setup.py init_catalog -l zh_CN -i ablog/locales/sphinx.pot -o ablog/locales/zh_CN/LC_MESSAGES/sphinx.po
python setup.py update_catalog -l zh_CN -i ablog/locales/sphinx.pot -o ablog/locales/zh_CN/LC_MESSAGES/sphinx.po

python setup.py compile_catalog --directory ablog/locales/ --domain sphinx --locale zh_CN