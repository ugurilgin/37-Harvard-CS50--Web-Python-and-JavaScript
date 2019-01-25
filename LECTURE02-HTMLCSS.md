# 37-Harvard-CS50--Web-Python-and-JavaScript
## CS50's Web Programming with Python and JavaScript
## Lecture 02 HTML CSS
### Provided by Harvard University (HarvardX)

## Environment Setup
Clone with HTTPS
Use Git or checkout with SVN using the web URL

`git clone https://github.com/ygautomo/37-Harvard-CS50--Web-Python-and-JavaScript.git`

## Lecture 02 Git
### Case 01 Simulate git branch command (06:20)
01. [master] create [001-index.html](/lecture02-htmlcss/001-index.html) in local machine
02. [master] `git add 001-index.html`
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

### Case 02 Simulate git merge command on master and feature branch (10:50)
01. [master] `git checkout master`
02. save as [002-hellogitmodified.html](/lecture01-git/002-hellogitmodified.html) in local machine
03. `git add 002-hellogitmodified.html`
04. `git commit -m 'Added 002-hellogitmodified.html'`
05. `git status`
06. `git push`
07. edit [002-hellogitmodified.html]((/lecture01-git/002-hellogitmodified.html)) on github sites
08. add line 'Hello, world! again second line' on github sites
09. click commit button
10. `git pull`

### Case 03 Simulate if conflict while other member team has modify [003-hellogitconflict.html](/lecture01-git/003-hellogitconflict.html) on github sites and you already modify the same file in local machine (22:20)
01. open [001-hello.html](/lecture01-git/001-hello.html) in local machine
02. save as [003-hellogitconflict.html](/lecture01-git/003-hellogitconflict.html) in local machine
03. `git add 003-hellogitconflict.html`
04. `git commit -m 'Added 003-hellogitconflict.html'`
05. `git status`
06. `git push`
07. edit [003-hellogitconflict.html]((/lecture01-git/003-hellogitconflict.html)) in local machine
08. add line 'Hello, world! again second line from local computer' in local machine
09. `git add 003-hellogitconflict.html`
10. `git commit -m 'Updated 003-hellogitconflict.html'`
11. changes has been saved but not implemented yet on github sites
12. edit [003-hellogitconflict.html]((/lecture01-git/003-hellogitconflict.html)) on github sites
13. add line 'Hello, world! again second line from github sites' on github sites
14. click commit button
15. changes has been saved and implemented on github sites
16. `git pull` will return error conflict
17. edit again [003-hellogitconflict.html]((/lecture01-git/003-hellogitconflict.html)) in local machine
18. resolve the conflict line then save
19. `git commit -am 'Updated 003-hellogitconflict.html'`
20. `git push`

### Case 04 `git log`, `git reset` and `git reflog` command (27:20)
01. open [001-hello.html](/lecture01-git/001-hello.html) in local machine
02. save as [004-hellogitreset.html](/lecture01-git/004-hellogitreset.html) in local machine
03. add line 'Hello, world! again second line from local computer first commit' in local machine
04. `git commit -am 'Added 004-hellogitreset.html'`
05. `git push`
06. modify line 'Hello, world! again second line from local computer second commit' in local machine
07. `git commit -am 'Modified 004-hellogitreset.html'`
08. `git push`
09. modify line 'Hello, world! again third line from local computer third commit' in local machine
10. `git commit -am 'Modified 004-hellogitreset.html'`
11. `git push`
12 git reset --hard <commit> # back to hash commit line 03
13. add line 'Hello, world! again third line from local computer to update first commit'
16. `git pull` will return error conflict
17. edit again [004-hellogitreset.html]((/lecture01-git/004-hellogitreset.html)) in local machine
18. resolve the conflict line then save
10. `git commit -am 'Modified after reset 004-hellogitreset.html'`
11. `git push`

## Lecture 01 Git- HTML session
### Subject 01 HTML tag (35:40)
01. open [001-hello.html](/lecture01-git/001-hello.html) in local machine
02. save as [005-hello.html](/lecture01-git/005-hello.html) in local machine
03. view as webpage in browser

### Subject 02 header HTML tag (41:00)
01. open [006-headings.html](/lecture01-git/006-headings.html)
02. right click 'page source' menu on the browser to see actual code html file

### Subject 03 lists HTML tag (43:50)
01. open [007-lists.html](/lecture01-git/007-lists.html)
02. open [008-sublists.html](/lecture01-git/008-sublists.html)

### Subject 04 image HTML tag (46:40)
01. open [009-image0.html](/lecture01-git/009-image0.html)
02. open [010-image1.html](/lecture01-git/010-image1.html) to resize the image
02. try to resize the image
03. try to resize the image responsively

### Subject 05 table HTML tag (53:50)
01. open [011-table.html](/lecture01-git/011-table.html)

### Subject 06 form HTML tag (56:20)
01. open [012-form.html](/lecture01-git/012-form.html)

### Subject 07 DOM (59:00)
![Document Object Model 001](/lecture01-git/DOM-model.svg "Document Object Model")

### Subject 08 color HTML attribute (01:01:00)
01. open [013-style0.html](/lecture01-git/013-style0.html)
02.

## Lecture 01 Git- CSS session
### Subject 09 color HTML attribute (01:01:00)
01. open [013-style0.html](/lecture01-git/013-style0.html)
02. open [014-style0.html](/lecture01-git/014-style0.html)
03. open [015-style1.html](/lecture01-git/015-style1.html)

### Subject 10 CSS (01:11:00)
01. open [016-style2.html](/lecture01-git/016-style2.html) and [styles.css](/lecture01-git/styles.css)

### Subject 11 div HTML tag and background-color, margin, padding CSS properties (01:14:40)
01. open [017-size.html](/lecture01-git/017-size.html)
02. open [018-size.html](/lecture01-git/018-size.html)

### Subject 12 div HTML tag and font-family, font-size, font-weight, and border CSS properties (01:18:00)
01. open [019-font.html](/lecture01-git/019-font.html)
02. open [020-border.html](/lecture01-git/020-border.html)

### Subject 13 table HTML tag, table CSS element, border and border-collapse CSS properties (01:21:50)
01. open [021-tablecss.html](/lecture01-git/021-tablecss.html)

### Subject 14 div, span HTML tag, div name, span class CSS element and CSS properties (01:28:00)
01. open [022-div_span.html](/lecture01-git/022-div_span.html)

### Subject 15 Publish website to GitHub Pages (01:40:50)
01. got to URL: https://blog.ygautomo.com/37-Harvard-CS50--Web-Python-and-JavaScript/lecture01-git/001-hello.html


### Git Command
- `git add <Filename>`			# Add file contents to the index
- `git branch` 					# List all branches
- `git branch <name>`			# Create branch <name>
- `git clone <URL>`				# Clone a GitHub repository in <URL> into a new directory
- `git checkout <name>` 		# Switch to <name> branches or restore working tree files
- `git commit -m <Comment>`		# Record changes to the repository
- `git log`						# Show commit logs
- `git pull` 					# Fetch from and integrate with another repository or a local branch
- `git push`					# Update remote refs along with associtated objects
- `git reflog`					# Manage reflog information
- `git reset --hard <commit>`	# Reset current HEAD to the specified state
- `git status`					# Show the working tree status


### Reference
- [CSS Reference](https://www.w3schools.com/cssref/default.asp)
- [Document Object Model](https://www.digitalocean.com/community/tutorial_series/understanding-the-dom-document-object-model)
- [Git Command](https://git-scm.com/)
- [Google Color Picker](https://www.google.com/)
- [HTML Tag & Attribute Reference](https://www.w3schools.com/tags/default.asp)
- [Web Color](https://en.wikipedia.org/wiki/Web_colors)