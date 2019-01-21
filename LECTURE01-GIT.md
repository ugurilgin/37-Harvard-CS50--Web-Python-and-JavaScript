# 37-Harvard-CS50--Web-Python-and-JavaScript
## CS50's Web Programming with Python and JavaScript
### Provided by Harvard University (HarvardX)

## Environment Setup
Clone with HTTPS
Use Git or checkout with SVN using the web URL

`git clone https://github.com/ygautomo/37-Harvard-CS50--Web-Python-and-JavaScript.git`

## Lecture 01 Git
### Case 01 Create [001hello.html](/lecture01-git/001hello.html) and push into github sites
01. create [001hello.html](/lecture01-git/001hello.html) in local machine (11:30)
02. `git add 001hello.html`
03. `git commit -m 'Added 001hello.html'`
04. `git status`
05. `git push`

### Case 02 Simulate if other member team has modify [002hellogitmodified.html](/lecture01-git/002hellogitmodified.html) on github sites and pull to local machine (20:00)
01. open [001hello.html](/lecture01-git/001hello.html) in local machine
02. save as [002hellogitmodified.html](/lecture01-git/002hellogitmodified.html) in local machine
03. `git add 002hellogitmodified.html`
04. `git commit -m 'Added 002hellogitmodified.html'`
05. `git status`
06. `git push`
07. edit [002hellogitmodified.html]((/lecture01-git/002hellogitmodified.html)) on github sites
08. add line 'Hello, world! again second line' on github sites
09. click commit button
10. `git pull`

### Case 03 Simulate if conflict while other member team has modify [003hellogitconflict.html](/lecture01-git/003hellogitconflict.html) on github sites and you already modify the same file in local machine (22:20)
01. open [001hello.html](/lecture01-git/001hello.html) in local machine
02. save as [003hellogitconflict.html](/lecture01-git/003hellogitconflict.html) in local machine
03. `git add 003hellogitconflict.html`
04. `git commit -m 'Added 003hellogitconflict.html'`
05. `git status`
06. `git push`
07. edit [003hellogitconflict.html]((/lecture01-git/003hellogitconflict.html)) in local machine
08. add line 'Hello, world! again second line from local computer' in local machine
09. `git add 003hellogitconflict.html`
10. `git commit -m 'Updated 003hellogitconflict.html'`
11. changes has been saved but not implemented yet on github sites
12. edit [003hellogitconflict.html]((/lecture01-git/003hellogitconflict.html)) on github sites
13. add line 'Hello, world! again second line from github sites' on github sites
14. click commit button
15. changes has been saved and implemented on github sites
16. `git pull` will return error conflict
17. edit again [003hellogitconflict.html]((/lecture01-git/003hellogitconflict.html)) in local machine
18. resolve the conflict line then save
19. `git commit -am 'Updated 003hellogitconflict.html'`
20. `git push`

### Case 04 `git log`, `git reset` and `git reflog` command (27:20)
01. open [001hello.html](/lecture01-git/001hello.html) in local machine
02. save as [004hellogitreset.html](/lecture01-git/004hellogitreset.html) in local machine
03. add line 'Hello, world! again second line from local computer first commit' in local machine
04. `git commit -am 'Added 004hellogitreset.html'`
05. `git push`
06. modify line 'Hello, world! again second line from local computer second commit' in local machine
07. `git commit -am 'Modified 004hellogitreset.html'`
08. `git push`
09. modify line 'Hello, world! again third line from local computer third commit' in local machine
10. `git commit -am 'Modified 004hellogitreset.html'`
11. `git push`
12 git reset --hard <commit> # back to hash commit line 03
13. add line 'Hello, world! again third line from local computer to update first commit'
16. `git pull` will return error conflict
17. edit again [004hellogitreset.html]((/lecture01-git/004hellogitreset.html)) in local machine
18. resolve the conflict line then save
10. `git commit -am 'Modified after reset 004hellogitreset.html'`
11. `git push`