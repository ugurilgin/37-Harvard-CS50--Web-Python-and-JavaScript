# 37-Harvard-CS50--Web-Python-and-JavaScript
## CS50's Web Programming with Python and JavaScript
## Lecture 02 HTML CSS
### Provided by Harvard University (HarvardX)

## Lecture 02 Git
## Environment Setup
### Case 01 Clone GitHub repository with HTTPS
### Use Git or checkout with SVN using the web URL
01. `git clone https://github.com/ygautomo/37-Harvard-CS50--Web-Python-and-JavaScript.git`

### Case 02 Simulate git branch command on local computer (06:20)
01. [master] create [001-index.html](/lecture02-htmlcss/001-index.html) in local machine
02. [master] `git add lecture02-htmlcss/001-index.html`
03. [master] `git commit -m 'Added 001-index.html'`
04. [master] `git branch`
05. [master] `git branch feature`
06. [master] `git branch`
07. [feature] `git checkout feature`
08. [feature] edit [001-index.html](/lecture02-htmlcss/001-index.html) in local machine
09. [feature] add line 'Here is a new feature!' and save [001-index.html](/lecture02-htmlcss/001-index.html)
10. [feature] `git commit -am 'Added another line on 001-index.html'`
11. [master] `git checkout master`
12. [master] `git branch`
13. [master] open [001-index.html](/lecture02-htmlcss/001-index.html) and you'll see original file without second line 'Here is a new feature!'
14. [feature] `git checkout feature`
15. [feature] `git branch`
16. [feature] open [001-index.html](/lecture02-htmlcss/001-index.html) and you'll see file with second line 'Here is a new feature!'
17. [master] `git checkout master`
18. [master] `git branch`
19. [master] open [001-index.html](/lecture02-htmlcss/001-index.html) and you'll see original file without second line 'Here is a new feature!'
20. [master] `git log` to see commit on master branch
21. [feature] `git checkout feature`
22. [feature] `git branch`
23. [feature] `git log` to see commit on feature branch
24. [feature] `git status`
25. [feature] `git commit -am 'Update feature branch'` if any changes in the working tree status

### Case 03 Simulate git merge command on master and feature branch on local computer (10:50)
01. [master] `git checkout master`
02. [master] `git merge feature`
03. [master] `git status`
04. [master] `git commit -am 'Merge feature branch'` if any changes in the working tree status
05. [master] `git push`

### Case 04 Repeart simulation git branch command and store to GitHub repository (12:00)
01. [master] `git branch -d feature`
02. [master] `git push origin --delete feature`
03. [master] `git status`
04. [master] create [002-index.html](/lecture02-htmlcss/002-index.html) in local machine
05. [master] `git add lecture02-htmlcss/002-index.html`
06. [master] `git commit -m 'Added 002-index.html'`
07. [master] `git push`
08. [master] `git branch`
09. [master] `git branch feature`
10. [feature] `git checkout feature`
11. [feature] edit [002-index.html](/lecture02-htmlcss/002-index.html) in local machine
12. [feature] change title 'Feature Branch' and add line 'Here is the branch contents.' then save [002-index.html](/lecture02-htmlcss/002-index.html)
13. [feature] `git add lecture02-htmlcss/002-index.html`
14. [feature] `git commit -m 'Added another line on 002-index.html'`
15. [feature] `git push`
16. return error 'fatal: The current branch feature has no upstream branch.'
17. [feature] `git push --set-upstream origin feature`
18. [feature] `git status`

### Case 05 `git fetch`, `git merge origin/master`, `git pull` and pull request command (16:50)
01. open GitHub then go to master branch repository
02. click new pull request button to merge the repository
03. [master] `git pull`
04. [master] open [002-index.html](/lecture02-htmlcss/002-index.html) in local machine and you'll see title has change to 'Feature Branch' and additional line 'Here is the branch contents.'

## Lecture 02 HTMLCSS- HTML session
### Subject 01 anchor HTML tag and href HTML attribute (23:20)
01. open [003-links0.html](/lecture02-htmlcss/003-links0.html) in local machine and view as webpage in browser
02. open [003-links1.html](/lecture02-htmlcss/003-links1.html) in local machine and view as webpage in browser and try to resize the webpage

### Subject 02 datalist HTML tag (33:00)
01. open [004-form.html](/lecture02-htmlcss/004-form.html)
02. fill the form and try auto complete on combo box country

## Lecture 01 Git- CSS session
### Subject 03 HTML tag as CSS selector (39:30)
01. open [005-multiple.html](/lecture02-htmlcss/005-multiple.html)
02. open [006-descendant.html](/lecture02-htmlcss/006-descendant.html)
03. open [007-descendant.html](/lecture02-htmlcss/007-descendant.html)
04. open [008-child.html](/lecture02-htmlcss/008-child.html)
05. open [009-attribute.html](/lecture02-htmlcss/009-attribute.html)

### Subject 04 pseudo class CSS and pseudo element CSS (50:30)
A pseudo-class is used to define a special state of an element
A CSS pseudo-element is used to style specified parts of an element
01. open [010-hover.html](/lecture02-htmlcss/010-hover.html)
02. open [011-before.html](/lecture02-htmlcss/011-before.html)
03. open [012-selection.html](/lecture02-htmlcss/012-selection.html)

### Subject 05 Mobile responsive web design (57:00)
01. open [013-print.html](/lecture02-htmlcss/013-print.html) example pseudo element CSS
02. open [014-responsive0.html](/lecture02-htmlcss/014-responsive0.html) example pseudo class CSS
03. open [015-responsive1.html](/lecture02-htmlcss/015-responsive1.html) example pseudo element CSS
04. open [016-flexbox.html](/lecture02-htmlcss/016-flexbox.html) example pseudo class CSS
05. open [017-grid.html](/lecture02-htmlcss/017-grid.html) example pseudo class CSS

### Subject 06 Boostrap CSS layout library (01:14:00)
01. open [018-nobootstrap.html](/lecture02-htmlcss/018-nobootstrap.html) example without Boostrap CSS library
02. open [019-bootstrap.html](/lecture02-htmlcss/019-bootstrap.html) example with Boostrap CSS library
03. open [020-columns0.html](/lecture02-htmlcss/020-columns0.html)
04. open [021-columns1.html](/lecture02-htmlcss/021-columns1.html)
04. open [022-columns2.html](/lecture02-htmlcss/022-columns2.html)
04. open [023-buttons.html](/lecture02-htmlcss/023-buttons.html)
05. open [024-alert.html](/lecture02-htmlcss/024-alert.html)

### Subject 07 Sass (Syntactically Awesome Style Sheets) as CSS preprocessor (01:23:40)
01. open [023-variables.html](/lecture02-htmlcss/023-variables.html) and their depedencies without Sass CSS preprocessor
02. open [024-variables.html](/lecture02-htmlcss/024-variables.html) and their depedencies with Sass CSS preprocessor
03. sass <sourcefile.scss> <resultfile.css>
04. sass --watch <sourcefile.scss>:<resultfile.css>
05. open [025-nesting.html](/lecture02-htmlcss/025-nesting.html) and their depedencies with Sass CSS preprocessor
06. open [026-inheritance.html](/lecture02-htmlcss/026-inheritance.html) and their depedencies with Sass CSS preprocessor


### Git Command
- `git add <filename>`			# Add file contents to the index
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