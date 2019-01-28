# 37-Harvard-CS50--Web-Python-and-JavaScript
## CS50's Web Programming with Python and JavaScript
## Lecture 03 Flask
### Provided by Harvard University (HarvardX)

## Lecture 03 Flask
## Environment Setup
### Case 01 Clone GitHub repository with HTTPS
### Use Git or checkout with SVN using the web URL
01. `git clone https://github.com/ygautomo/37-Harvard-CS50--Web-Python-and-JavaScript.git`
02. run FileZilla "DO python.ygautomo.com 2019" session
03. copy exercise file to "/home/python/work/37 Harvard CS50 Web Python/lecture03-flask" directory
04. run PuTTY "DO python.ygautomo.com 2019" session
05. `cd "/home/python/work/37 Harvard CS50 Web Python/lecture03-flask"`
06. `python --version` should return "Python 3.5.6 :: Anaconda custom (64-bit)"
07. this course uses Python 3.6 so you have to create new environment

### Subject 01 Python simple program and variable (01:30)
01. open [001-hello.py](/lecture03-flask/001-hello.py) and upload to server
02. `python 001-hello.py` on server
03. open [002-name.py](/lecture03-flask/002-name.py) and upload to server
04. `python 002-name.py` on server
05. open [003-variables.py](/lecture03-flask/003-variables.py) and upload to server
06. `python 003-variables.py` on server
07. open [004-conditions.py](/lecture03-flask/004-conditions.py) and upload to server
08. `python 004-conditions.py` on server
09. open [005-sequences.py](/lecture03-flask/005-sequences.py) and upload to server
10. `python 005-sequences.py` on server

### Subject 02 Python interpreter demo (15:00)
01. `python` to open python interpreter
02. run following code
	`>>> x = 28`
	`>>> x`
	return `28`
	`>>> if x > 0:`
	`... 	print("x is positive")`
	`... ` 	<CR>
	return `x is positive`
03. run following code for name string variable demo
	`>>> name = "Alice"`
	`>>> name[0]`
	return `'A'`
	`>>> name[1]`
	return `'l'`
04. run following code for coordinates tuple variable demo
	`>>> coordinates =(10.0, 20.0)`
	`>>> coordinates[0]`
	return `10.0`
	`>>> coordinates[1]`
	return `20.0`
05. run following code for names list variable demo
	`>>> names = ["Alice", "Bob", "Charlie"]`
	`>>> names[0]`
	return `'Alice'`
	`>>> names[1]`
	return `'Bob'`
	`>>> names[2]`
	return `'Charlie'`
	`>>> names[3]`
	return error `IndexError: string index out of range`
06. `quit()` use quit() or Ctrl-D (i.e. EOF) to exit from python interpreter

### Subject 03 Pyhton loop (18:40)
01. open [006-loops0.py](/lecture03-flask/006-loops0.py) and upload to server
02. `python 006-loops0.py` on server
03. open [007-loops1.py](/lecture03-flask/007-loops1.py) and upload to server
04. `python 007-loops1.py` on server
05. open [008-loops2.py](/lecture03-flask/008-loops2.py) and upload to server
06. `python 008-loops2.py` on server

### Subject 04 Python set dan dictionaries datatype (23:30)
01. open [009-sets.py](/lecture03-flask/009-sets.py) and upload to server
02. `python 009-sets.py` on server 
03. open [010-dictionaries.py](/lecture03-flask/010-dictionaries.py) and upload to server
04. `python 010-dictionaries.py` on server 

### Subject 05 Python function (28:00)
01. open [011-functions.py](/lecture03-flask/011-functions.py) and upload to server
02. `python 011-functions.py` on server
03. open [011-functionsmodified.py](/lecture03-flask/011-functionsmodified.py) and upload to server
04. `python 011-functionsmodified.py` on server
05. try to import function from other file
06. open [012-modules.py](/lecture03-flask/012-modules.py) and upload to server
07. `python 012-modules.py` on server

### Subject 06 Python class 7 decorators (36:00)
01. open [013-classes.py](/lecture03-flask/013-classes.py) and upload to server
02. `python 013-classes.py` on server
03. open [014-decorators.py](/lecture03-flask/014-decorators.py) and upload to server
04. `python 014-decorators.py` on server

## Lecture 03 Flask- HTTP session (39:00)
### Running Flask Application
In order to run Flask Application, you should.
01. `export FLASK_APP=/home/[user_id]/work/[directory]/[filename.py]`
	`flask run --host=0.0.0.0` on server
02. access web server on http://[website]:5000

### Subject 01 Flask hello world simple program (40:20)
01. open [application.py](/lecture03-flask/015-first/application.py) and upload to server

### Subject 02 Flask routing and variable rules (47:00)
01. open [application.py](/lecture03-flask/016-routes0/application.py) and upload to server
02. open [application.py](/lecture03-flask/017-routes1/application.py) and upload to server

### Subject 03 Flask rendering html templates, combine with Flask routing and variable rules (53:20)
01. open [application.py](/lecture03-flask/018-templates/application.py) and upload to server
02. open [application.py](/lecture03-flask/019-variables0/application.py) and upload to server
03. open [application.py](/lecture03-flask/020-variables0/application.py) and upload to server
04. open [application.py](/lecture03-flask/021-variables0/application.py) and upload to server
05. open [application.py](/lecture03-flask/022-variables1/application.py) and upload to server

### Subject 04 Flask rendering html templates with conditions (01:03:00)
01. open [application.py](/lecture03-flask/023-conditions/application.py) and upload to server

### Subject 05 Flask rendering html templates with loops (01:11:30)
01. open [application.py](/lecture03-flask/024-loops/application.py) and upload to server

### Subject 06 Flask rendering html templates with links & html template inheritance (01:14:10)
01. open [application.py](/lecture03-flask/025-urls/application.py) and upload to server
02. open [application.py](/lecture03-flask/026-inheritance/application.py) and upload to server

### Subject 07 Flask rendering html templates with user input form (01:22:30)
01. open [application.py](/lecture03-flask/027-forms/application.py) and upload to server

### Subject 06 Flask session (01:32:40)
01. open [application.py](/lecture03-flask/028-notes/application.py) and upload to server
02. open [application.py](/lecture03-flask/029-notessession/application.py) and upload to server

### Notes
- Error: IndentationError: unindent does not match any outer indentation level
	You should check mixed up tabs and spaces in code editor

### Python Command
- `python <filename>`			# Run python program
- `python --version`
- `git branch` 					# List all branches
- `git branch <name>`			# Create branch <name>
- `git clone <URL>`				# Clone a GitHub repository in <URL> into a new directory
- `git checkout <name>` 		# Switch to <name> branches or restore working tree files
- `git commit -m <comment>`		# Record changes to the repository
- `git log`						# Show commit logs
- `git merge <name>				# Join two or more development histories together
- `git prune <name>				# Manage set of tracked repositories
- `git pull` 					# Fetch from and integrate with another repository or a local branch
- `git push`					# Update remote refs along with associated 
- `git push <origin> --delete <branch>`
- `git push --set-upstream <origin> <branch>`
- `git reflog`					# Manage reflog information
- `git reset --hard <commit>`	# Reset current HEAD to the specified state
- `git status`					# Show the working tree status
- `git --version`				# Show git version


### Reference
- [Is it christmas](https://isitchristmas.com/)


- [Bootstrap](https://getbootstrap.com/)
- [CSS Reference](https://www.w3schools.com/cssref/default.asp)
- [CSS Selector](https://www.w3schools.com/cssref/css_selectors.asp)
- [Document Object Model](https://www.digitalocean.com/community/tutorial_series/understanding-the-dom-document-object-model)
- [Git Command](https://git-scm.com/)
- [Google Color Picker](https://www.google.com/)
- [HTML Tag & Attribute Reference](https://www.w3schools.com/tags/default.asp)
- [Sass](https://sass-lang.com/)
- [Sass vs Less](https://www.keycdn.com/blog/sass-vs-less)
- [Sass Online Converter](https://www.sassmeister.com/)
- [Web Color](https://en.wikipedia.org/wiki/Web_colors)