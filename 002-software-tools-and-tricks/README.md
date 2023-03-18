# 💾 Software
![CyberPi](../cyber-pi-github-profile.png)

This tutorial is **optional** but highly recommended! It covers the ways to theme and stylize your terminal and text editor -- the two most important tools in your arsenal!


## Setting up your Terminal on macOS
The terminal for macOS is a command-line interface that provides access to the underlying operating system of a Mac computer. It allows users to execute a variety of commands, such as running scripts, managing files and directories, installing packages and applications, and controlling system settings. In other words, the terminal serves as a powerful tool for users who want to interact with their computer in a more direct and precise way. It can be particularly useful for developers, system administrators, and power users who need to perform complex tasks quickly and efficiently.


## macOS Terminal
The macOS terminal is what allows you to interact with the Operating System.  
The most important commands to know are in the table below, in particular the `man` command

| Command |             Description             |
|---------|-------------------------------------|
| `ls`    | List contents of current directory  |
| `cd`    | Change to a different directory     |
| `mkdir` | Create a new directory              |
| `touch` | Create a new file                   |
| `cp`    | Copy a file or directory            |
| `mv`    | Move or rename a file or directory  |
| `rm`    | Remove a file or directory          |
| `echo1` | Print a message to the console      |
| `man`   | Display manual pages for a command  |
| `pwd`   | Print the current working directory |   

Each of those commands allows for different "arguments" (also known as flags). For example with the `rm` command

|           Flag           |                                Description                                 |
|--------------------------|----------------------------------------------------------------------------|
| `rm [file]`              | Remove a file                                                              |
| `rm -r [directory]`      | Remove a directory and its contents recursively                            |
| `rm -f [file/directory]` | Force removal of a file or directory without prompting for confirmation    |
| `rm -i [file/directory]` | Prompt before removing each file or directory                              |
| `rm -v [file/directory]` | Verbose output, prints the name of each file or directory as it is removed |
| `rm -d [directory]`      | Remove an empty directory                                                  |

> **⚠️ Note:** It is worth taking some time to learn what the **man** and **help** commands do.   

The man command and help command are like instruction manuals for how to use different commands on a computer. man shows instructions for commands that are built into the computer system, while help shows instructions for commands that you can use in the command line.

| Command |         Flag        |                     Description                      |
|---------|---------------------|------------------------------------------------------|
| man     | `man [command]`     | Display the manual page for a specific command       |
| man     | `man -k [keyword]`  | Search the manual pages for a specific keyword       |
| man     | `man -f [command]`  | Display the one-line description of a command        |
| man     | `man -a [command]`  | Display all the available manual pages for a command |
| help    | `help`              | Display a list of built-in shell commands            |
| help    | `help [command]`    | Display information about a specific shell command   |
| help    | `help -m [command]` | Display the manual page for a specific shell command |

## Installing Homebrew
Homebrew is a package manager for macOS that will come in handy throughout this tutorial.

1. Open the Terminal app on your Mac. You can find it in the Utilities folder within the Applications folder, or use Spotlight Search to find it.  
2. In the Terminal window, paste the following command and press Enter:  

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```  

3. The installation script will start running, and you will be prompted to enter your password. This is the password you use to log in to your Mac. Type it in and press Enter.
4. The installation script will then download and install Homebrew on your Mac. This process may take several minutes, depending on your internet connection speed.
5. Once the installation is complete, you can test that Homebrew is installed by typing the following command in the Terminal window and pressing Enter:

```bash
brew --version
```
6. Homebrew is installed correctly, the version number should be displayed in the Terminal window.

That's it! Homebrew is now installed on your Mac, and you can use it to install a wide variety of command-line tools and software packages.


### Adding Plugins & Themes to Terminal
The terminal is better when you stylize it! 

**Changing the Theme**
1. Open the Terminal app on your Mac. You can find it in the Utilities folder within the Applications folder, or use Spotlight Search to find it.
2. In the menu bar at the top of the screen, click on Terminal > Preferences. Alternatively, you can use the keyboard shortcut `Command + ,` to open the preferences window.
3. In the Preferences window, click on the `Profiles` tab.
4. Select the profile that you want to change the theme for by clicking on it in the list on the left-hand side of the window.

**Adding Terminal Plugins**

1. Install [Zsh4Humans](https://github.com/romkatv/zsh4humans) by running `brew install zsh4humans` in the terminal
2. Install [Powerlevel10K](https://github.com/romkatv/powerlevel10k) by entering `brew install romkatv/powerlevel10k/powerlevel10k` into your terminal
3. Add **Powerlevel10K** to your shell configuration, so it's easier to use `echo "source $(brew --prefix)/opt/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc`

## Sublime Text 4
Next we are going to install a simple text editor

1. Go to [Sublime Text 4](https://www.sublimetext.com/download) to [download](https://www.sublimetext.com/download) the latest version
2. In Sublime click View > Show Console
3. Paste the code from Package Control (also below) into console and press Enter

```
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
**Adding Sublime Packages**
Let's install our first package, the [Dracula Theme](https://draculatheme.com/). To do this

1. Press `Command + Shift + P` it will bring up Package control. 
2. Search for `Dracula Color Scheme` and press enter
3. Go to Sublime Text > Preferences > Color Scheme > Select `Dracula`

# Install the Markdown Preview package for Sublime Text
This will make it very easy for you to be able to write in markdown and preview it.

1. Open Sublime Text 4 on your computer.
2. Open the Package Control panel by pressing Ctrl+Shift+P (Windows) or Cmd+Shift+P (macOS).
3. In the panel, type `Install Package` and press `Enter`. This will bring up a search bar where you can search for packages.
4. Type "Markdown Preview" in the search bar and press Enter. This will search for the package in the Package Control repository.
5. When the search results appear, select `Markdown Preview` from the list of packages and press Enter. This will begin the installation process.
6. Wait for the package to download and install. This process may take a few seconds or minutes, depending on your internet connection speed.
7. Once the package is installed, you should be able to use it to preview Markdown files in Sublime Text 4.
8. Open a Markdown file in Sublime Text 4, and then open the Markdown Preview panel by pressing `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (macOS) and selecting `Markdown Preview: Preview in Browser`"` from the list of commands.
9. A new browser tab will open, displaying a preview of the Markdown file.



