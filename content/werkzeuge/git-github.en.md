+++
title = "Git & GitHub"
weight = 4
+++

**GitHub** is where your [learning journal]({{% relref "projekte/lernjournal" %}}) and later your teams' code live. **Git** is the tool behind it that records every change as a **commit**. In week 1 you work in the browser only. Working with Git locally comes as soon as you share code in a team.

## Part 1 · Create an account

1. Open [github.com/signup](https://github.com/signup).
2. Choose an email address (school address if you have one), a password and a **username**. The username is publicly visible: no full real name required, but such that your teacher can identify you, e.g. `firstname-lastname-initials` or as agreed in class.
3. Enter the confirmation code from the email.

{{% notice style="warning" title="Password" %}}
Write the password down in a safe place. A forgotten GitHub password costs half an hour. If the school has a password manager, use it.
{{% /notice %}}

## Part 2 · Create the learning journal repository

{{< tabs groupid="repo" >}}
{{% tab title="With invitation link (Classroom 50)" %}}
The class uses **Classroom 50**, a free tool that creates a private repository for each person in the school's organisation.

1. **Report your username:** tell your teacher your GitHub username (list on the board or a form). Only then can they enable you.
2. Open [classroom50.org](https://classroom50.org/), click **Sign in with GitHub** and allow Classroom 50 in the window (**Authorize**).
3. Open the teacher's **classroom link** (accept the organisation invitation if asked).
4. Open the **assignment link** `lernjournal`. The page shows your username and the name of the repository you will get.
5. Click **Accept assignment**. A checklist shows the progress, it takes up to a minute.
6. Click **Open repository** and **bookmark** the page.

Your repository is named after the pattern `<class>-lernjournal-<username>`. **Do not rename it**, otherwise Classroom 50 no longer finds it. It is private: only you and your teacher see it. The folder structure and a template are already inside.
{{% /tab %}}
{{% tab title="Create it yourself" %}}
1. Top right **+ → New repository**.
2. Repository name: `lernjournal`. Visibility: **Private**.
3. Tick **Add a README file**. Then **Create repository**.
4. Add your teacher as a reader: **Settings → Collaborators → Add people**, enter the teacher's GitHub username.
5. Create the folder structure: **Add file → Create new file**, type `p1/woche-01.md` as the file name (the slash creates the folder), paste the content of the [template]({{% relref "projekte/lernjournal" %}}), **Commit changes**.
{{% /tab %}}
{{< /tabs >}}

## Part 3 · Edit a file in the browser and commit

1. In the repository click the file, e.g. `README.md`.
2. Top right the **pencil icon** (Edit this file).
3. Change the text. Use the **Preview** tab to check how the Markdown looks.
4. Top right **Commit changes…**
5. Enter a short **commit message** that says what you changed, e.g. `README: added name and class`. Then **Commit changes**.

That is the whole cycle: **edit → preview → commit**. Every commit is a point on the timeline. Under **Commits** (or the clock icon) you see all previous versions and can look at any old state.

### Create a new file

**Add file → Create new file**. Put a folder with a slash into the file name: `p1/woche-02.md`.

### Upload an image

1. **Add file → Upload files**.
2. Drag the screenshot in. Name it sensibly first, e.g. `p1-w01-switch.png`.
3. At the bottom **Commit changes**. The image is now in the repository (put it into the `images/` folder by navigating into that folder first).
4. Embed it in the journal entry: `![My switch](../images/p1-w01-switch.png)`

{{% notice style="info" title="Taking a screenshot" %}}
Windows: **Win+Shift+S** · macOS: **Cmd+Shift+4** · Linux (GNOME): **Print** key. The image lands in the clipboard or in the Pictures folder.
{{% /notice %}}

## The three terms you need today

| Term | Meaning |
|------|---------|
| **Repository** (repo) | A project folder with the complete history of all changes. |
| **Commit** | A saved state with message, time and author. Immutable. |
| **Commit message** | One sentence saying what changed. For you in three months and for your teacher. |

## Later: Git locally

As soon as teams write code together (from P1 sprint 1), you work with Git on your own computer: clone, change, commit, push, and work in parallel with **branches**. This guide will be extended then. Until then the browser is enough.
