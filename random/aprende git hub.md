## Part 1: Get your bearings

### 1. What is version control (and why does it matter)?

**Version control is a system that tracks changes to your files over time, and Git is the most widely used version control system in the world.**

If you’ve ever saved `brand_guide_v2`, `brand_guide_final`, and `brand_guide_FINAL_actually`, you’ve already felt the problem that version control solves. Git records every change you make, so you can see what changed, when, and why. If you need to go back to an earlier version, it can handle that, too. You never need a folder full of “final” files again.

Git works through three zones: your **working directory** (where you edit), the **staging area** (where you review what’s ready), and the **local repository** (where your saved history lives). Three commands move work between them (i.e., `git status`, `git add`, and `git commit`) and you’ll use them so often they become muscle memory.

**Read more: [What is Git? Our beginner’s guide to version control](https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/)**

 _ **Tip:** When someone says “push your code,” they mean you should use Git to upload your local commits to GitHub._

### 2. How do I set up and secure my GitHub account?

**Your GitHub account is your** **developer** **identity_._ _**You should make sure** **it’s** **well protected**_.**

Turning on two-factor authentication (2FA) adds a second layer of protection that keeps your account safe even if your password is stolen. Passwords alone are vulnerable to phishing and reuse, so enable 2FA from **Settings → Password and authentication**.

While you’re here, give yourself a profile **README**. This is a living portfolio of your skills, projects, and interests. Create a public repository with the same name as your username, add a README, and whatever you write shows up on your profile page.

**Read more: [Beginner’s guide to GitHub: Setting up and securing your profile](https://github.blog/developer-skills/github/beginners-guide-to-github-setting-up-and-securing-your-profile/)**

__ _Tip: Download your recovery codes and store them in a password manager. They’re your only way back in if you lose your device._

### 3. Which Git commands do I actually need?

**A small set of Git commands covers the daily workflow of nearly every developer.**

The commands you want to become familiar with are .config, init, clone, add, commit, push, pull, branch, and switch.

You don’t need to memorize all of Git. Here are the ones you can use to get started:

|**Command**|**What it does**|
|---|---|
|git config –global user.name “…”|Set the name attached to your commits|
|git init|Turn the current folder into a Git repository|
|git clone <url>|Make a local copy of a remote repository|
|git status|See what’s changed in your local environment and what’s staged|
|git add .|Stage all your changes for the next commit|
|git commit -m “message”|Save a snapshot of your staged changes|
|git switch -c <branch>|Create a new branch and switch to it|
|git push|Upload your local commits to GitHub|
|git pull|Download and merge the latest changes from GitHub|
|git merge <branch>|Integrate another branch into your current one|

**Read more: [Top 12 Git commands every developer must know](https://github.blog/developer-skills/github/top-12-git-commands-every-developer-must-know/)**

## Part 2: Build your first project

### 4. How do I create my first repository?

**A repository (or “repo”) is a project folder that tracks changes, stores history, and lets multiple people seamlessly work together.**

This is your project’s home base. Start from your **dashboard**, the page you land on when you sign in to [github.com](https://github.com/), which shows your repositories and activity feed.

- Click the green **New** button
- Give your repo a name
- Choose public or private
- Check the box to add a README. This is the first thing visitors see and should act as the front door to your project.

That’s it! You have a repository. You can optionally add a `.gitignore` to keep junk files out of version control and a license to tell others what they’re allowed to do with your code.

What’s a `.gitignore` for? As you work, your project folder fills up with files you never actually wrote. These are things your computer or tools automatically create (e.g. system files, folders of downloaded dependencies, temporary build output). You don’t want to track or share those, so a `.gitignore` file lists them and tells Git to leave them alone. It keeps your repository clean and focused on the code that actually matters.

**Read more: [Beginner’s guide to GitHub repositories: How to create your first repo](https://github.blog/developer-skills/github/beginners-guide-to-github-repositories-how-to-create-your-first-repo/)**

### 5. What is Markdown and how do I use it?

**Markdown is a lightweight language for formatting plain text**. I**t’s how you write READMEs, issues, pull requests, and comments across GitHub.**

Markdown turns simple symbols into clean formatting. A few keystrokes give you documentation that’s a pleasure to read, which can make all the difference. You can use Markdown syntax, along with some HTML tags, to format your writing on GitHub.

**Read more: [GitHub for Beginners: Getting started with Markdown](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-markdown/)**

### 6. What is the GitHub flow?

**The GitHub flow is the repeatable loop for safely adding work to a shared progress: branch, commit, push, open a pull request, merge.**

Here’s the rhythm you’ll keep on repeating:

1. Clone the repo to your machine
2. Create a branch for your work
3. Make changes
4. Commit them
5. Push them to GitHub
6. Open a pull request.

You can collaborate on anything you store in a repository. For example, imagine your team keeps its reusable AI prompts in a shared repo. You rework the prompt to improve the output. You make that change on a branch, open a pull request, and a colleague checks the new output before it’s approved. Once it’s merged, the next teammate who refreshes the repo is automatically writing from the improved prompt. There’s no need to send out an announcement to use the new prompt and no attachment drifting around inboxes. It’s the same branch-review-merge loop developers use, applied to words instead of code.

**Read more: [Beginner’s guide to GitHub: Adding code to your repository](https://github.blog/developer-skills/github/beginners-guide-to-github-setting-up-and-securing-your-profile/)**

 _![💡](https://s.w.org/images/core/emoji/17.0.2/svg/1f4a1.svg) **Tip:** Give branches descriptive names like `fix-login-bug` or `add-dark-mode` so everyone knows what they’re for at a glance._

## Part 3: Collaborate with other people

### 7. What is a pull request?

**A pull request is a proposal to merge a set of changes from one branch into another, with a built-in space for teammates to review and discuss.**

A pull request is where collaboration happens. It shows a visual diff of exactly what you changed and gives reviewers a place to comment . Write a clear title and description, link any related issues, and review your own pull request first to catch obvious mistakes.

 _![💡](https://s.w.org/images/core/emoji/17.0.2/svg/1f4a1.svg) **Tip:** Smaller pull requests are easier and faster to review and merge, provide less room to introduce bugs, and provide a clearer history of changes._

**Read more: [Beginner’s guide to GitHub: Creating a pull request](https://github.blog/developer-skills/github/beginners-guide-to-github-creating-a-pull-request/)**

### 8. How do I merge a pull request and fix a merge conflict?

**Merging integrates reviewed changes into your target branch. A merge conflict is simply Git asking for your help when two changes touch the same lines of code and it doesn’t know how to integrate both changes at the same time.**

Most merges are one green button: click **Merge pull request**, confirm, done. ![🎉](https://s.w.org/images/core/emoji/17.0.2/svg/1f389.svg) Sometimes two branches edit the same lines of a file and Git can’t decide which version wins. In this case, GitHub marks the conflicting sections. You use the browser editor or VS Code to choose what to keep, mark it resolved, and merge. With a little practice, it feels as natural as any other push.

**Read more: [Beginner’s guide to GitHub: Merging a pull request](https://github.blog/developer-skills/github-education/beginners-guide-to-github-merging-a-pull-request/)**

### 9. What are GitHub Issues and Projects?

**Issues track individual tasks, bugs, and ideas, while projects organize those issues into a visual board so nothing slips through the cracks.**

Issues are shared, trackable notes. Each one is a task, bug, or idea you can assign, label, and discuss. Projects pull those issues onto a Kanban-style board so you can see the status of all the issues at a glance. Here’s a small piece of magic that ties it all together. Every issue gets its own number. You’ll see it after the title as a hashtag and then a number (e.g., Let’s call a sample issue `The answer to everything #42`). When you open a pull request to fix that issue, you can type a closing keyword into the pull request description (e.g., Closes `#42`, Fixes `#42`, or Resolves `#42`).

GitHub recognizes that phrase as a link between the two: the pull request and the issue now reference each other. Then, the moment that pull request is merged, GitHub automatically marks issue `#42` as closed for you. If the issue is on a project board, it slides over to the “Done” column on its own. It’s a simple habit that keeps your code changes and your task tracking in sync without any extra effort.

**Read more: [GitHub for Beginners: Getting started with GitHub Issues and Projects](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-issues-and-projects/)**

## Part 4: Level up your projects

### 10. What is GitHub Actions?

**GitHub Actions is a CI/CD and automation platform built into GitHub that automatically runs tasks (e.g., tests, deployments, labeling) when events happen in your repo.**

Once your project is moving, use GitHub Actions to let GitHub do the repetitive work. Write a workflow as a YAML file in `.github/workflows/`, tell it what event should trigger it, and define the steps to run. From then on, GitHub follows those steps on its own.

**Read more: [GitHub for Beginners: Getting started with GitHub Actions](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-actions/)**

### 11. How do I publish a website for free?

Got a portfolio, a project page, or documentation? GitHub Pages can host it for free at `username.github.io/repo-name` with no servers to manage. Enable it from **Settings → Pages**, choose to deploy from a branch, and you’re live in minutes. Even private repositories can publish a public site. This is great for showcasing work with code you’d rather keep to yourself.

**Read more: [GitHub for Beginners: Getting started with GitHub Pages](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-pages/)**

 _![💡](https://s.w.org/images/core/emoji/17.0.2/svg/1f4a1.svg) **Tip:** Use Pages to promote your projects, share what you’re building, and grow your portfolio._

### 12. How do I secure my code on GitHub?

Security isn’t a final step; it’s a habit. **GitHub Advanced Security is a built-in suite that automatically finds and helps you fix vulnerabilities. It includes secret scanning, Dependabot, and CodeQL code scanning, and it’s free for public repositories.**

**Secret scanning** catches API keys you accidentally commit. **Dependabot** watches your dependencies for known vulnerabilities and opens pull requests to update them. **CodeQL** analyzes how data flows through your code to spot risky patterns and explains how to fix what it finds. Turn it all on from your repository settings.

**Read more: [GitHub for Beginners: Getting started with GitHub security](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-security/)**

 _![💡](https://s.w.org/images/core/emoji/17.0.2/svg/1f4a1.svg) **Tip:** You inherit any risk from a library the moment you import it into your project, even though you didn’t write the vulnerable code yourself._

### 13. How do I contribute to open source?

**Open source software has freely available code that anyone can study and improve, and GitHub is its home.**

How do you find the perfect project to contribute to? First, look for projects with a clear README, a `CONTRIBUTING.md`, an open source license, and issues tagged `good first issue`. That label is maintainers’ way of waving beginners in.

Contributing to real projects is one of the fastest ways to grow, and a fork makes it safe to do so. A **fork** is your own personal copy of someone else’s repository where you can experiment freely, then propose your changes back with a pull request.

So how is a fork different from a branch? A **branch** is a parallel workspace _inside_ a repository you already have permission to change. A **fork** copies an entire repository into _your_ account, which is what you need when you don’t have permission to edit the original (like most open source projects). A common workflow combines both: you fork the project, create a branch in your fork for your changes, and then open a pull request back to the original.