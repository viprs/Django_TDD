# Django_TDD
使用TDD测试驱动web开发


## 需要安装的软件 ##

- Firefox web浏览器
- Git版本工具，推荐使用Github
- pip包管理工具

## 需要安装的Python模块 ##

安装Django模块

	pip3 install django==1.7

安装Selenium模块
	
	pip3 install selenium==2.53.6


## 运行第一个项目 ##

你可以使用`django-admin.py`或者`django-admin`新建一个工程：

	django-admin.py startproject superlists

这个命令会创建一个名为superlists的文件夹，并在其中创建一些文件和文件夹：
（在`PowerShell`里运行 `tree /f`）

	  .gitignore
	  README.md
	  requirements.txt
	  
	  superlists
	    │  db.sqlite3
	    │  function_tests.py
	    │  manage.py
	    └─superlists
	        │  settings.py
	        │  urls.py
	        │  wsgi.py
	        │  __init__.py
	        │
	        └─__pycache__
	                settings.cpython-34.pyc
	                urls.cpython-34.pyc
	                wsgi.cpython-34.pyc
	                __init__.cpython-34.pyc

运行服务器：

	python3 manage.py runserver

创建第一个应用：

	python3 manage.py startapp lists

现在的目录结构是：


	  .gitignore
	  README.md
	  requirements.txt
	  
	  superlists
	    │  db.sqlite3
	    │  function_tests.py
	    │  manage.py
	    │
	    ├─lists
	    │  │  admin.py
	    │  │  models.py
	    │  │  tests.py
	    │  │  views.py
	    │  │  __init__.py
	    │  │
	    │  └─migrations
	    │          __init__.py
	    │
	    └─superlists
	        │  settings.py
	        │  urls.py
	        │  wsgi.py
	        │  __init__.py
	        │
	        └─__pycache__
	                settings.cpython-34.pyc
	                urls.cpython-34.pyc
	                wsgi.cpython-34.pyc
	                __init__.cpython-34.pyc

功能测试：站在用户的角度从外部测试应用。（高层驱动开发）

单元测试：站在程序员的角度从内部测试应用。（底层驱动开发）


## 数据库迁移 ##

	python3 manage.py makemigrations

	生成测试数据库迁移


## 使用迁移创建生产数据库 ##

	python3 manage.py migrate [--noinput]

	--noinput 标志是说“不输入任何东西”


## 确保功能测试之间相互隔离 ##

单元测试时，Django的测试运行程序会自动创建一个全新的测试数据库（和应用真正使用的数据库不同），运行每个测试之前都会清空数据库，等所有测试都运行完之后，再删除这个数据库。

但是功能测试目前使用的是应用真正使用的数据库db.sqlite3。

从Django 1.4开始，提供了一个新类 LiveServerTestCase，它可以代我们完成这一任务。这个类会自动创建一个测试数据库（跟单元测试一样），并启动一个开发服务器，让功能测试在其中运行。虽然这个功能有一定的局限性（稍后解决），不过在现阶段十分有用。


	superlists
	├─function_tests
	├─lists
	│  ├─migrations
	│  │  └─__pycache__
	│  ├─templates
	│  └─__pycache__
	└─superlists
	    └─__pycache__

运行功能测试：
	
	python3 manage.py test functional_tests

运行单元测试：
	
	python3 manage.py test lists

## 疑问 ##

- makemigration和migrate分别有什么区别？ 



