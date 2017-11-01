"""
    This module is for using Git.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, IntegerRef, Key, Text)

sublime_context = AppContext(executable="sublime_text")
terminal_context = AppContext(executable="MobaXterm_Personal_7.4")
putty_context = AppContext(executable="putty")
cmder_context = AppContext(executable="Cmder")
grammar = Grammar("git", context=(sublime_context | terminal_context | putty_context | cmder_context))

git_rule = MappingRule(
    name="git",
    mapping={

# Add ----------------------------------------------------------------------------------------             // ADD -------------------------------------------------------------------------------------------
            "[git] add":                       Text("git add "),                                           # git add                      | Stages files, i.e. schedules the addition of an individual file to your next commit. Takes changes in your working directory and stages them.
            "[git] add (A | all)":             Text("git add -A") + Key("enter"),                          # git add -A                   | Stages All. Adds everything plus deletions. It's the equivalent to "git add ." and "git add -u".
            "[git] add (A | all) whole tree":  Text("git add -A :/") + Key("enter"),                       # git add -A :/                | Stages All from whole tree. Adds everything plus deletions. It's the equivalent to "git add ." and "git add -u".
            "[git] add dot":                   Text("git add ."),                                          # git add .                    | Stages new and modified, without deleted. Adds all your files when initializing a repo.
            "[git] add P":                     Text("git add -p") + Key("enter"),                          # git add -p                   | Step through each change, or hunk, and decide if you'd like to commit it. Interactively choose hunks of patch between the index and the working tree and add them to the index.
            "[git] add update":                Text("git add --update"),                                   # git add --update             | Stage all changes in all tracked files (only considers files that are already tracked). All modifications in all known files will be included in the next commit..
            "[git] add U":                     Text("git add -u"),                                         # git add -u                   | Stages modified and deleted, without new.
# SSH ----------------------------------------------------------------------------------------             // SSH -------------------------------------------------------------------------------------------
            "[git] bash key add":              Text("ssh-add ~/.ssh/"),                                    # add ~/.ssh/                  | Add a specific SSH key --> ssh-add ~/.ssh/<key>
            "[git] bash key delete specific":  Text("ssh-add -d ~/.ssh/"),                                 # add -d ~/.ssh/               | Delete a specific key --> ssh-add -d ~/.ssh/<key>
            "[git] bash key generate":         Text("ssh-keygen -t rsa -C \"\""),                          # keygen -t rsa -C ""          | Generate a new SSH key --> ssh-keygen -t rsa -C "<your_email@example.com>"
            "[git] bash keys":                 Text("ssh-add -l"),                                         # add -l                       | List all the keys that ssh-agent knows about.
            "[git] bash keys check":           Text("cd ~/.ssh"),                                          # cd ~/.ssh                    | Check for existing ssh keys on your computer.
            "[git] bash keys delete":          Text("ssh-add -D"),                                         # add -D                       | Delete all the keys that ssh-agent knows about.
            "[git] bash keys list":            Text("ssh-add -l"),                                         # add -l                       | List all the keys that ssh-agent knows about.
# Bisect and Blame ---------------------------------------------------------------------------             // BISECT AND BLAME ------------------------------------------------------------------------------
            "[git] bisect":                    Text("git bisect start "),                                  # git bisect start <start_hash> <end_hash> | Useful function for determining where in history something changed, especially when given a large timeframe.
            "[git] bisect bad":                Text("git bisect bad") + Key("enter"),                      # git bisect bad               | Mark specific hash as Bad. Git now moves backward in time.
            "[git] bisect good":               Text("git bisect good") + Key("enter"),                     # git bisect good              | Mark specific hash as Good. Git returns hash information for bad.
            "[git] blame":                     Text("git blame "),                                         # git blame <file>             | See who was the last person to touch a file.
# Branches -----------------------------------------------------------------------------------             // BRANCHES --------------------------------------------------------------------------------------
            "[git] branch":                    Text("git branch") + Key("enter"),                          # git branch                   | Shows existing branches.
            "[git] branch new":                Text("git branch "),                                        # git branch                   | Creates new branch.
            "[git] branch (A | all)":          Text("git branch -a") + Key("enter"),                       # git branch -a                | Shows all branches, including hidden ones. Can also use --all.
            "[git] branch set upstream":       Text("git branch --set-upstream-to "),                      # git branch --set-upstream-to <remote> | Set up tracking.
            "[git] (branch delete | delete branch)": Text("git branch -d "),                               # git branch -d                | Delete a branch.
            "[git] (branch delete | delete branch) big dee": Text("git branch -D "),                       # git branch -D                | Delete a branch with unmerged changes.
            "[git] branch delete remote":      Text("git push origin :"),                                  # git push <remote_name> :<branch> | Delete a remote branch.
            "[git] branch pull":               Text("git fetch origin :"),                                 # git fetch origin <remote_branch>:<new_local_branch> | Pull a new branch from a remote repository.
            "[git] branch push":               Text("git push origin"),                                    # git push origin <new_remote> | Push a branch to a remote repository.
            "[git] branch rename":             Text("git branch -m "),                                     # git branch -m | git branch (-m | -M) [<old_branch>] <new_branch>
            "[git] (branch V V | tracking branches)": Text("git branch -vv") + Key("enter"),               # git branch -vv               | Shows which upstream branch is being tracked, how many commits your head or behind.
            # Commits
            "[git] show branch":               Text("git show-branch") + Key("enter"),                     # git show-branch              | Shows last commit on each of our branches.
# Check Out ----------------------------------------------------------------------------------             // CHECK OUT -------------------------------------------------------------------------------------
            "[git] checkout [<text>]":         Text("git checkout %(text)s"),                              # git checkout <branch>        | Switch branch and make working directory look like tree.
            "[git] checkout bee":              Text("git checkout -b "),                                   # git checkout -b              | Creates a new branch and checks it out.
            "[git] checkout dev":              Text("git checkout dev"),                                   # git checkout dev             | Switch to branch.
            "[git] checkout ef":               Text("git checkout -f"),                                    # git checkout -f              | Check out the previous commit with -f flag to force overwriting the current changes, i.e. "I screwed up, how do I reset my checkout?"
            "[git] checkout force":            Text("git checkout --force"),                               # git checkout --force         | Check out the previous commit with --force flag to force overwriting the current changes.
            "[git] checkout (hyphen | last [branch])": Text("git checkout -"),                             # git checkout -               | Switch to last branch.
            "[git] checkout hyphen bee":       Text("git checkout -b"),                                    # git checkout -b              | 'Creates a new branch and checks it out.
            "[git] checkout master":           Text("git checkout master") + Key("enter"),                 # git checkout master          | Checks out master.
            "[git] checkout ours":             Text("git checkout --ours"),                                # git checkout --ours          | git checkout --ours PATH/FILE
            "[git] checkout production":       Text("git checkout production"),                            # git checkout production      | Switch to branch.
            "[git] checkout revisions":        Text("git checkout revisions"),                             # git checkout revisions       | Checks out revisions branch.
            "[git] checkout theirs":           Text("git checkout --theirs "),                             # git checkout --theirs        | git checkout --theirs PATH/FILE
# Clean --------------------------------------------------------------------------------------             // CLEAN -----------------------------------------------------------------------------------------
            "git clean [(ef | untracked files)]": Text("git clean -f") + Key("enter"),                     # git clean -f                 | Remove untracked files from the working tree.
            "[git] clean (ef dee | untracked files and directories)": Text("git clean -f -d") + Key("enter"), # git clean -f -d           | Remove untracked files and directories from the working tree.
            "[git] clean (ef ex | untracked and ignored files)": Text("git clean -f -X") + Key("enter"),   # git clean -f -X              | Remove untracked files and also ignored files from the working tree.

            # git clean --dry-run               to blow out anything that isn't tracked by git.

# Clone --------------------------------------------------------------------------------------             // CLONE -----------------------------------------------------------------------------------------
            "[git] clone":                     Text("git clone "),                                         # git clone                       | Gets an existing repo. Will do a git remote add - add a remote; do a fetch on it; then check it out, i.e. copy a directory.
            "[git] clone single branch":       Text("git clone -b  --single-branch"),                      # git clone -b  --single-branch   | To clone a single branch --> git clone -b <branch_name> --single-branch <repo>
# Commits ------------------------------------------------------------------------------------             // COMMITS ---------------------------------------------------------------------------------------
            "[git] (amend commit | commit amend)": Text("git commit --amend"),                             # git commit --amend              | Adds changes to previous commit.
            "[git] amend last [(commit | message)]": Text("git commit --amend -m "),                       # git commit --amend -m ""        | To change previous commit message.
            "[git] amend [(commit | message)] with editor": Text("git commit -a --amend") + Key("enter"),  # git commit -a --amend           | To change previous commit message through editor, displays commited file names.
            "[git] commit":                    Text("git commit"),                                         # git commit                      | Commits staged files. Takes everything you staged with git add, and actually adds it into the repository.
            "[git] commit a":                  Text("git commit -a"),                                      # git commit -a                   | Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.
            "[git] commit all":                Text("git commit -am "),                                    # git commit -am                  | Commit all your local changes with a message.
            "[git] commit all with quotes":    Text("git commit -am \"\"") + Key("left"),                  # git commit -am ""               | Commit all your local changes with a message.
            "[git] commit [allow] empty":      Text("git commit --allow-empty -m \"\""),                   # git commit --allow-empty -m ""  | Create an empty commit.
            "[git] commit (em | with message)": Text("git commit -m "),                                    # git commit -m                   | Commits and specifies your commit message.
            "[git] commit (em | with message) with quotes": Text("git commit -m \"\"") + Key("left"),      # git commit -m ""                | Commits and specifies your commit message.
            "[git] commit vee":                Text("git commit -v"),                                      # git commit -v                   | Commits staged files, but allows you to view the difference as you commit. Takes everything you staged with git add, and actually adds it into the repository.
            "[git] cherry pick":               Text("git cherry-pick"),                                    # git cherry-pick <hash>          | Take a commit from somewhere else, and "play it back" wherever you are right now, i.e. bring changes from another branch into our current branch, without merging everything from the other branch.

            # git show <commit>

# Configuration ------------------------------------------------------------------------------             // CONFIGURATION ---------------------------------------------------------------------------------
            "git alias":                       Text("git config --global alias."),                         # git config --global alias.                   | Set up aliases, e.g. git config --global alias.co checkout
            "git configure":                   Text("git config"),                                         # git config                                   | Sets up our configuration variables.
            "[git] configure [global] email":  Text("git config --global user.email \"\"") + Key("left"),  # git config --global user.email ""            | Sets up global email.
            "[git] configure [global] editor": Text("git config --global core.editor \"\"") + Key("left"), # git config --global core.editor ""           | Sets up global editor - Use: mate -w, subl -w or subl -n -w, atom --wait, emacs, vi or vim, gvim -f, mvim -f
            "[git] configure [global] name":   Text("git config --global user.name \"\"") + Key("left"),   # git config --global user.name ""             | Sets up global name.
            "[git] configure ignore whitespace": Text("git config --global apply.whitespace nowarn"),      # git config --global apply.whitespace nowarn  | To ignore whitespace.
            "[git] configure list":            Text("git config --list"),                                  # git config --list                            | To view all configuration options.
            "[git] configure new lines":       Text("git config core.autocrlf false"),                     # git config core.autocrlf false               | Sets up how Windows handles new lines (LF and CF).
            "[git] configure sublime":         Text("git config --global core.editor \"\'C:/Program Files/Sublime Text 2/sublime_text.exe\' -m\""), # git config... | Sets up Sublime as global editor.
# Diff ---------------------------------------------------------------------------------------             // DIFF ------------------------------------------------------------------------------------------
            "[git] diff":                      Text("git diff") + Key("enter"),                            # git diff                     | Shows a unified diff of two different trees.
            "[git] diff cached":               Text("git diff --cached") + Key("enter"),                   # git diff --cached            | View the changes you staged (cached) for the next commit relative to last commit (HEAD).
            "[git] diff color":                Text("git diff --color=auto") + Key("enter"),               # git diff --color=auto        | Highlights diffs.
            "[git] recorded diff":             Text("git rerere diff") + Key("enter"),                     # git rerere diff              | Shows a unified diff of two different ReReRe trees.

            # git diff --staged
            # git branch --merged
            # git branch --no-merged

# Fetch --------------------------------------------------------------------------------------             // FETCH -----------------------------------------------------------------------------------------
            "[git] fetch":                     Text("git fetch"),                                          # git fetch                    | Fetches objects we do not have from remote, does not merge them.
            "[git] fetch checkout branch":     Text("git fetch origin && git checkout origin/ && git checkout -b"), # git fetch origin && git checkout origin/<branch_name> && git checkout -b <branch_name>
            "[git] fetch upstream":            Text("git fetch upstream"),                                 # git fetch upstream           | Fetch latest changes from upstream.
# Grep ---------------------------------------------------------------------------------------             // GREP -------------------------------------------------------------------------------------
            "git grep":                        Text("git grep -e \"\"") + Key("left"),                     # git grep -e "<search>"                                              | Grep functionality to search code.
            "git grep (structured | clean)":   Text("git grep --line-number --heading --break -e \"\"") + Key("left"),  # git grep --line-number --heading --break -e "<search>" | Returns a more human readable result.
            "git grep line cached":            Text("git grep --cached -e \"\"") + Key("left"),            # git grep --cached -e "<search>"                                     | Only searches in the staging area.
            "git grep line number":            Text("git grep --line-number -e \"\"") + Key("left"),       # git grep --line-number -e "<search>"                                | Includes line number in results.
            "git grep line number cached":     Text("git grep --line-number -cached -e \"\"") + Key("left"), # git grep --line-number --cached -e "<search>"                     | Only searches in the staging area, and includes line number in results.
# Github -------------------------------------------------------------------------------------             // SERVICES --------------------------------------------------------------------------------------
            "github add":                      Text("git remote add origin git@github.com:/.git"),         # git remote add origin git@github.com:<username>/<application>.git
            "github add maxxiimo":             Text("git remote add origin git@github.com:maxxiimo/.git"), # git remote add origin git@github.com:maxxiimo/.git
            "github add viewthought":          Text("git remote add origin git@github.com:viewthought/.git"), # git remote add origin git@github.com:viewthought/.git
            "github add primary code":         Text("git remote add origin git@github.com:primarycode/.git"), # git remote add origin git@github.com:Ward primarycode/.git
            "github delete branch":            Text("git push --tags origin :"),                           # git push --tags origin :<branch_name>
            "github push":                     Text("git push -u origin master"),                          # git push -u origin master
            "github push branch":              Text("git push -u origin "),                                # git push -u origin <feature_branch_name>
            # "git hub shortcuts":               Key("c-slash"),                                             # Open github keyboard shortcuts legend.
# Set Up -------------------------------------------------------------------------------------             // SET UP ----------------------------------------------------------------------------------------
            "git (init | initial commit | initialize)": Text("git init") + Key("enter"),                   # git init                         | Sets up a project with git, initializes a get directory.
            "[git] add dot":                   Text("git add .") + Key("enter"),                           # git add .
            "[git] initial commit message":    Text("git commit -am \"Initial commit.\"") + Key("enter"),  # git commit -am "Initial commit." | git commit -am "Initial commit."
# Logs ---------------------------------------------------------------------------------------             // LOGS ------------------------------------------------------------------------------------------
            "[git] kay":                       Text("gitk") + Key("enter"),                                # git gitk                     | Opens gitk.
            "[git] log (awesome | amazing)":   Text("git log --graph --pretty=format:\'%%Cred%%h%%Creset -%%C(yellow)%%d%%Creset %%s %%Cgreen(%%cr) %%C(bold blue)<%%an>%%Creset\' --abbrev-commit") + Key("enter"),
            "[git] log [branch]":              Text("git log "),                                           # git log <branch_name>        | Show commit history, show log messages in [branch-name] that are not in HEAD (the current commit)
            "[git] log graph":                 Text("git log --graph") + Key("enter"),                     # git log --graph              | Draw a text-based graphical representation of the commit history on the left hand side of the output.
            "[git] log (pee | changes)":       Text("git log -p"),                                         # git log -p                   | Show commit history with lines that changed.
            "[git] log one line":              Text("git log --oneline") + Key("enter"),                   # git log --oneline            | Show commit history in single line format.
            "[git] log one line [<n>]":        Text("git log -n %(n)d --oneline") + Key("enter"),          # git log -n <#> --oneline     | Show commit history in single line format.
            "[git] log pretty one line":       Text("git log --pretty=oneline") + Key("enter"),            # git log --pretty=oneline     | Show commit history in single line format. Shows full sha1.
            "[git] log pretty [<n>]":          Text("git log --pretty=oneline -%(n)d") + Key("enter"),     # git log --pretty=oneline -<#> | Show commit history in single line format. Shows full sha1.
            "[git] log pretty format":         Text("git log --pretty=format:\"%%h %%an %%ar - %%s\""),    # git log --pretty=format:"%h %an %ar - %s" | Show commit history in customized format: partial sha, author, date, message
            "[git] log search":                Text("git log -S"),                                         # git log -S                   | Search commit history for <word>.
            "[git] log tree":                  Text("git log --all --graph --decorate --oneline --simplify-by-decoration"), # git log...  | Show a pretty branch status.
            "[git] log (vee | pagination)":    Text("git log -v"),                                         # git log -v                   | Show commit history with pagination.
            "[git] log visualize":             Text("git gitk --all"),                                     # git gitk --all               | Allows you to visualize git changes.
            "[git] master (carrot | parent)":  Text("git master^"),                                        # git master^                  | Will tell you the parent of the object you are pointing at.
            "[git] master (carrot two | parent two)": Text("git master^2"),                                # git master^2                 | Will tell you the second parent of the object you are pointing at.
            "[git] master (tilde two | grandparent)": Text("git master~2"),                                # git master~2                 | Will tell you the parent of the parent of the object you are pointing at, i.e. the grandparent.
            "[git] ref log":                   Text("git reflog"),                                         # git reflog                   | Show every step you've made with git.
            "[git] short log":                 Text("git shortlog -sn"),                                   # git shortlog -sn             | Get a list of contributors and see how many commits each person has.

            # git log --name-status --follow --oneline hello.template
            # git log diff filter delete     git log --diff-filter=D --oneline -- hello.template
            # git log since
            # git log follow
            # git log grep
            # git log diff filter

# Merge --------------------------------------------------------------------------------------             // MERGE -----------------------------------------------------------------------------------------
            "[git] merge [<text>]":            Text("git merge %(text)s"),                                 # git merge <branch_name>      | Doesn't change anything with existing history, creates a new commit that brings together two parent commits. Merge a branch into currently checked out branch or several branches currently checked out.
            "[git] merge no fast forward [<text>]": Text("git merge --no-ff %(text)s"),                    # git merge --no-ff <branch_name> --no-ff | Merges branch but does not fast-forward, i.e. requires merge commit and thereby keeps branch history.
            "[git] merge abort":               Text("git merge --abort"),                                  # git merge --abort            | To return to the state before you started the merge.
            "[git] merge master":              Text("git merge master") + Key("enter"),                    # git merge master             | Merges master branch into cleanse branch.
            "[git] merge origin master":       Text("git merge origin/master"),                            # git merge origin/master      | git merge origin/master
            "[git] merge reset":               Text("git reset ORIG_HEAD"),                                # git reset ORIG_HEAD          | Reverting changes after merge to state before merge. Preserve any uncommitted changes.
            "[git] merge reset hard":          Text("git reset --hard ORIG_HEAD"),                         # git reset --hard ORIG_HEAD   | Reverting changes after merge to state before merge. Delete any uncommitted changes.
            "[git] merge revisions":           Text("git merge revisions"),                                # git merge revisions          | Merge in revisions branch.
            "[git] merge upstream":            Text("git merge upstream/master"),                          # git merge upstream/master    | Merges upstream.
            "[git] re re re":                  Text("git config rerere.enabled true"),                     # git config rerere.enabled true | Reuse Recorded Resolution. To automate complex merges; super useful in situations where you get a large number of repeated merge conflicts, such as when you're refactoring a codebase while others are still making changes.
# Miscellaneous ------------------------------------------------------------------------------             // MISCELLANEOUS ---------------------------------------------------------------------------------
            "[git] a em":                      Text("git am"),                                             # git am                       | Applies email formatted diff and creates new commit object.
            "[git] apply":                     Text("git apply"),                                          # git apply                    | Applies diff to current tree.
            "[git] contributors":              Text("git shortlog -sn"),                                   # git shortlog -sn             | Get a list of contributors and see how many commits each person has.
            "[git] format-patch":              Text("git format-patch"),                                   # git format-patch             | Email formatted diff.
            "[git] garbage collector":         Text("git gc"),                                             # git gc                       | Patches repetitive blobs to conserve disk space.
            "[git] help":                      Text("git command --help"),                                 # git command --help           | git command --help
            "[git] move":                      Text("git mv"),                                             # git mv                       | Git's version of the Unix mv ("move") command to change a file's name.
            # Plumbing
            "[git] cat file T":                Text("git cat-file -t "),                                   # Inspect objects; type.
            "[git] cat file P":                Text("git cat-file -p "),                                   # Inspect objects; more info.
            "[git] cat show head":             Text("cat .git/HEAD") + Key("enter"),                       # Check the value of HEAD variable; confirm your pointing to the correct branch.
            "[git] show refs":                 Text("git show-ref --heads") + Key("enter"),                # To see which commits your HEADs are pointing to.
            "[git] tag refs":                  Text("git show-ref --tags") + Key("enter"),                 # git show-ref --tags          | To see what commit a tag points to.
            "[git] tag (points at | reverse lookup)": Text("git tag --points-at "),                        # git tag --points-at <sha1>   | To see tag of commit, if any.
            "git L S [files]":                 Text("git ls-files -s") + Key("enter"),                     # To view the contents of the staging area.
# Pull ---------------------------------------------------------------------------------------             // PULL ------------------------------------------------------------------------------------------
            "[git] pull":                      Text("git pull") + Key("enter"),                            # git pull                     | Fetches objects and pulls them into tracking branch, i.e. merges them.
            "[git] pull (ef | with force)":    Text("git pull -f"),                                        # git pull -f                  | Pull changes with force option.
            "[git] pull bitbucket":            Text("git pull bitbucket") + Key("enter"),                  # git pull bitbucket           | To pull from ViewThought account at bitbucket.
            "[git] pull github":               Text("git pull github") + Key("enter"),                     # git pull github              | To pull from ViewThought account at github.
            "[git] pull origin":               Text("git pull origin"),                                    # git pull origin              | Fetches objects and pulls them from sharing branch into tracking branch, i.e. merges them.
            "[git] pull origin dev":           Text("git pull origin dev"),                                # git pull origin dev          | Fetches objects and pulls them from sharing branch into tracking branch, i.e. merges them.
            "[git] pull origin master":        Text("git pull origin master"),                             # git pull origin master       | Fetches objects and pulls them from sharing branch into tracking branch, i.e. merges them.
            "[git] pull origin production":    Text("git pull origin production"),                         # git pull origin production   | Fetches objects and pulls them from sharing branch into tracking branch, i.e. merges them.
            "[git] pull rebase":               Text("git pull --rebase"),                                  # git pull --rebase            | Rebase your changes on top of another commit in order to fast-forward your commit.
# Push ---------------------------------------------------------------------------------------             // PUSH ------------------------------------------------------------------------------------------
            "[git] push":                      Text("git push") + Key("enter"),                            # git push                     | Push changes to origin.
            "[git] push (ef | with force)":    Text("git push -f"),                                        # git push -f                  | Push changes to origin with force option.
            "[git] push bitbucket":            Text("git push bitbucket") + Key("enter"),                  # git push bitbucket           | To push to ViewThought account at bitbucket.
            "[git] push github":               Text("git push github") + Key("enter"),                     # git push github              | To push to ViewThought account at github.
            "[git] push heroku":               Text("git push heroku") + Key("enter"),                     # git push heroku              | To push to heroku.
            "[git] push origin dev":           Text("git push origin dev"),                                # git push origin dev          | Push changes to dev.
            "[git] push origin head":          Text("git push origin HEAD"),                               # git push origin HEAD         | Add a new local branch to repository.
            "[git] push origin master":        Text("git push origin master"),                             # git push origin master       | Push changes to master.
            "[git] push origin production":    Text("git push origin production"),                         # git push origin production   | Push changes to production.
            "[git] push with password":        Text("git push"),                                           # git push                     | Push changes to origin.
# Rebase -------------------------------------------------------------------------------------             // REBASE ----------------------------------------------------------------------------------------
            "[git] rebase":                    Text("git rebase"),                                         # git rebase                   | Takes a range of commits and recommits them on top of a new point. Replays the history as though you are recommitting it again the second time. Same as merge but writes history differently; adds on top for linear history rather than splitting.
            "[git] rebase continue":           Text("git rebase --continue"),                              # git rebase --continue        | Restart the rebasing process after having resolved a merge conflict.
            "[git] (rebase interactive | interactive rebates)":  Text("git rebase --interactive "),        # git rebase --interactive     | Allows you to edit commits prior to the last commit. Makes a list of the commits which are about to be rebased. Lets the user edit that list before rebasing. Include Shaw of parent commit.
            "[git] rebase master":             Text("git rebase master"),                                  # git rebase master            | Makes sure changes on master appear in your branch.
# Remotes ------------------------------------------------------------------------------------             // REMOTES ---------------------------------------------------------------------------------------
            "[git] remote":                    Text("git remote") + Key("enter"),                          # git remote                   | Shows remotes.
            "[git] remote (vee | url)":        Text("git remote -v") + Key("enter"),                       # git remote -v                | Shows remote URLs.
            "[git] remote add":                Text("git remote add "),                                    # git remote add               | Adds remote --> git remote add <remote_name> <url | git://github.com/whoever/whatever.git>
            "[git] remote prune":              Text("git remote prune"),                                   # git remote prune             | Deletes all stale remote-tracking branches under <name>. Prunes pointers deleted on server locally.
            "[git] remote remove":             Text("git remote update --prune"),                          # git remote update --prune    | Remove local branches that have been deleted from your remote.
            "[git] remote remove dry run":     Text("git remote update --dry-run"),                        # git remote update --dry-run  | Dry run of removing local branches that have been deleted from your remote.
            "[git] remote rename":             Text("git remote rename origin upstream") + Key("enter"),   # git remote rename origin upstream | Rename the origin remote to upstream.
            "[git] remote set":                Text("git remote set-url origin "),                         # git remote set-url origin https://github.com/<repo>/<name>.git
            "[git] remote show":               Text("git remote show "),                                   # git remote show              | If you want to see more information about a particular remote, you can use the git remote show [remote-name] command.
            "[git] remote show origin":        Text("git remote show origin") + Key("enter"),              # git remote show origin       | Shows what is tracked and most importantly what is configured for pushes.
# Remove -------------------------------------------------------------------------------------             // REMOVE ----------------------------------------------------------------------------------------
            "[git] remove":                    Text("git rm "),                                            # git rm                       | Scheduling the deletion of a file: git rm [file name]
            "[git] remove are":                Text("git rm -r "),                                         # git rm -r                    | git rm -r
            "[git] remove cached":             Text("git rm --cached "),                                   # git rm --cached              | To keep a file in your working tree but remove it from your staging area. On hard drive but not tracked.
# Reset --------------------------------------------------------------------------------------             // RESET -----------------------------------------------------------------------------------------
            "[git] reset":                     Text("git reset"),                                          # git reset                    | Resets the current branch HEAD and index, but not the working tree, i.e. the changed files are preserved but not marked for commit.
            "[git] reset original head":       Text("git reset ORIG_HEAD"),                                # git reset ORIG_HEAD          | ORIG_HEAD Reverts mistakes made in git reset, keeps a copy of your HEAD in a variable called ORIG_HEAD, to help you get back to where you want to be.
            "[git] reset (hard | uncomitted changes)": Text("git reset --hard"),                           # git reset --hard             | Resets all uncommitted changes made in your working copy. Can also use to point the current branch at a specific commit.
            "[git] (reset hard head | uncommit last commit hard)": Text("git reset --hard \"HEAD^\""),     # git reset --hard "HEAD^"     | Un-commit last commit and throw away changes. Windows needs quotes.
            "[git] (reset soft head | uncommit last commit [soft])": Text("git reset --soft \"HEAD^\""),   # git reset --soft "HEAD^"     | Un-commit last commit without touching working tree. Windows needs quotes.
            "[git] reset [head] mixed":        Text("reset HEAD~1 --mixed"),                               # git reset HEAD~1 --mixed     | Resets the previous commit, but keeps all the changes from that commit in the working directory.
            "[git] (reset head | unstage)":    Text("git reset HEAD "),                                    # git reset HEAD               | Unstages specific files.
            "[git] reset merge":               Text("git reset ORIG_HEAD"),                                # git reset ORIG_HEAD          | Reverting changes after merge to state before merge. Preserve any uncommitted changes.
            "[git] reset merge hard":          Text("git reset --hard ORIG_HEAD"),                         # git reset --hard ORIG_HEAD   | Reverting changes after merge to state before merge. Delete any uncommitted changes.
            # Revert
            "[git] revert":                    Text("git revert"),                                         # Reverts don't look as nice in your history, but are a safer option when working with collaborators.
# Stash --------------------------------------------------------------------------------------             // STASH -----------------------------------------------------------------------------------------
            "[git] stash":                     Text("git stash save"),                                     # git stash save               | Stash your current changes. Creates a stash (like a clipboard) of changes to allow you to switch branches without committing.
            "[git] stash apply":               Text("git stash apply stash@{0}"),                          # git stash apply stash@{0}    | Apply a stash (stash@{0} refers to the last stash you made).
            "[git] stash apply index":         Text("git stash apply --index"),                            # git stash apply --index      | Apply a stash, and reapply the staged changes.
            "[git] stash clear":               Text("git stash clear"),                                    # git stash clear              | Wipe all your stashes away.
            "[git] stash drop":                Text("git stash drop stash@{0}"),                           # git stash drop stash@{0}     | Drop your last stash if you do not need it anymore.
            "[git] stash list":                Text("git stash list") + Key("enter"),                      # git stash list               | List current stashes.
            "[git] stash [with] message":      Text("git stash save \"\"") + Key("left"),                  # git stash save "" %          | Stash your current changes: git stash save "Put a message here to remind you of what you're saving to the clipboard"
            "[git] stash pop":                 Text("git stash pop"),                                      # git stash pop                | Pop off your last stash you saved (stash apply and stash drop in one step).
            "[git] stash show":                Text("git stash show stash@{0}") + Key("enter"),            # git stash show stash@{0}     | View more information about stash.
# Status -------------------------------------------------------------------------------------             // STATUS ----------------------------------------------------------------------------------------
            "[git] status":                    Text("git status") + Key("enter"),                          # git status                   | Shows which files modified and staged in working directory.
            "[git] status es":                 Text("git status -s"),                                      # git status -s                | Shows which files modified and staged in working directory, but with short output flag.
            "[git] status short":              Text("git status --short"),                                 # git status --short           | Shows which files modified and staged in working directory, but with short output flag.
# Tags ---------------------------------------------------------------------------------------             // TAGS ------------------------------------------------------------------------------------------
            "[git] tag (annotated | with message)": Text("git tag -a \"\" -m \"\"") + Key("left:7"),       # git tag -a "<name>" -m "<message>" | Same as regular tag but also stores additional metadata.
            "[git] tag by commit":             Text("git tag -a"),                                         # git tag -a                   | To tag a commit later use all or part of shaw --> git tag -a <tag_name> <commit_checksum>
            "[git] tag delete":                Text("git tag -d"),                                         # git tag -d                   | Delete a tag. --> git tag -d <tag_name>
            "[git] tag [lightweight]":          Text("git tag "),                                          # git tag <name>               | To create new tag. A lightweight tag is very much like a branch that doesn't change -- it's just a pointer to a specific commit.
            "[git] tag list":                  Text("git tag") + Key("enter"),                             # git tag                      | To list available tags.
            "[git] tag push":                  Text("git push origin"),                                    # git push origin              | git push origin <tag_name>
            "[git] tag push all":              Text("git push origin --tags"),                             # git push origin --tags       | To push all your tags at once --> git push origin --tags
            "[git] tag push delete":           Text("git push origin :refs/tags/"),                        # git push origin :refs/tags/  | git push origin :refs/tags/<tag_name>
            "[git] tag show":                  Text("git show "),                                          # git show <tag_name>          | See pertinent information about tag.

            },
    extras=[
            Dictation("text"),
            IntegerRef("n", 1, 20)
           ],
    defaults = {
        "text": "",
        "n": 1,
        }
    )

grammar.add_rule(git_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
