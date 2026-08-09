# Day 3

Today I learned how to use `and` and `or` in a statement, and I tried them in the final boss.

In the final boss, I had a problem where even though the code said to do something only if a condition was met, it still continued to the next line.

I got a hint that I needed to put all of that code inside the `if` statement so it would only run if certain conditions were met.

I also learned a few basic commands in Git.

`git --version`
Checks whether Git is installed and shows the version installed on the computer.

`git init`
Turns the current folder into a Git repository. Git creates a hidden `.git` folder that it uses to keep track of the project's history.

`git status`
Shows the current state of your repository.

`git add + folder name`
Puts the selected changes into the staging area.

Example:
`git add Day03`

`git commit -m "message"`
Takes everything I staged with `git add` and creates a permanent checkpoint in my Git history.

Example:
`git commit -m "Complete Day 3 logical operators"`

`git log --oneline`
Shows my previous commits in a compact format.

I'm a little overwhelmed with everything, but hopefully the more I do it, the more I will learn and it will eventually become second nature.

The good thing is that I can learn at my own pace.


Your normal workflow from now on

When you finish some meaningful work:

git status
git add <file-or-folder>
git commit -m "Describe what I changed"
git push