
Sphinx
======

.. post:: Oct 26, 2021
   :tags:
   :category:


"打开 *命令提示符* （:kbd:`⊞Win-r` 并输入 :command:`cmd`）并运行相同的命令。"

Sphinx 的主要目标之一是在任何 :term:`域` 中轻松记录 :term:`对象` （在一个非常普遍的意义上）。
一个域是属于一起的对象类型的集合，有完整的标记来创建和引用这些对象的描述。

For a great "introduction" to writing docs in general -- the whys and hows, see
also `Write the docs`__, written by Eric Holscher.

.. __: https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/


:program:`sphinx-quickstart`

:rst:role:`ref`

.. todo:: 待更新

:option:`-b <sphinx-build -b>`

|more| 符号

:file:`make.bat`

:command:`make`

:rst:dir:`py:class`

:rst:dir:`py:method`

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)

:func:`enumerate`

:confval:`extensions` 

:py:data:`sys.path`

.. rubric:: Footnotes

.. |more| image:: /_static/more.png
          :align: middle
          :alt: more info

.. program:: sphinx-build

.. option:: -b buildername

   The most important option: it selects a builder.  The most common builders
   are:

   **html**
      Build HTML pages.  This is the default builder.

.. autofunction:: io.open
