#github

Here is a nice [glossary](https://help.github.com/articles/github-glossary/) with the different terms that Github uses.

The important ones are:

- **Repository (or repo):** The folder with your shizzle. The one on github is called the *remote* repo, and the one on your laptop is called the *local* repo.
- **Remote:** This is the version of something that is hosted on a server, most likely GitHub.com. It can be connected to local repositories (on your laptop say) so that changes can be synced. The remote in our case is the knowitwall repository
- **Commit:** A commit is a 'revision' of your local repository (on your laptop) to the remote (on Github). Also works as a verb (ex: "don't forget to commit your changes at the end of the day").
- **Pull:** This means fetching *in* changes from the remote repository on Github to your local repo (on your laptop). If you are the only contributor to a project and are working from a single laptop you don't need to do this but you should get in the habit to always do this because:
	- you might want to work on a project from several computors, so you would need to pull the recent changes to whatever computor you're working on at the moment
	- if you start working in a team you will need to do this. Ex: if I modify something and commit the changes to github, you will need to pull those changes to your local repo before you start working on it.
- **Push:** This is the opposite of a pull. You send the changes that you commited to github. (so to 'save' your changes, you have 2 actions to do: commit, then push). I'm not sure why there are 2 different actions for this. It's probably because of the way git was created; it might allow you to do different things that would require seperating those 2 actions.
- **Clone:** If a repo already exists on github and you want to start working on it for the first time, you have to clone it to your laptop.

Here are the steps to save your work to github:

###1. check the status of your local repo; is it in synch with the remote?

type 'git status'

this will tell you if you have made changes that you need to commit to the remote. (you don't have to do this by the way)

###2. declare that you're going to add some shit:

type 'git add .'


note: If you removed a file or directory since the last commit, you need to type 'git add --all' to commit the fact that you removed something.

###3. commit your shit with a message explaining breifly what you've done since the last commit (useful if you want to backtrack later):

type: "git commit -m 'type your message here' "


###4. pull changes to your local repo (in case someone changes something recently!!). get in the habit of always doing this!

type: 'git pull'

**merges:**
If there is a merge to be made (ie: I made some changes), you need to include a merge message).
The editor that pops up might be 'vim'. look online how to use this.
summary of how to use it: 

- press 'i' (to go in insert mode)
- type the commit message in quotation marks
- press 'esc' (to escape insert mode)
- type :wq (to save and exit)

###5. push to remote:

type: 'git push'


I stopped putting screenshots because something's not working for me got to fix it :p
but that's it!
