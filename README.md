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


## 疑问 ##

- makemigration和migrate分别有什么区别？ 



