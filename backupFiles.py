from datetime import date
import platform
import os

"""
I use two different operating systems, Linux and macOS, basically the dotfiles are the same, but there may be differences in each one, so it is necessary to check which system the script is running on
"""

if (platform.system() == 'Linux'):

    # copy my dotfiles to repository folder
    os.system('cat ~/.zshrc > .zshrc')

    date = date.today()

    # print(platform.system())
    #commit the changes
    os.system('echo "Commit dotfiles"')
    os.system(f'git commit -am "update {date}"')
    os.system('git push')
    os.system('echo "Have a nice day!"')


else:
    # copy my dotfiles to repository folder
    os.system('cat ~/.zshrc > ./macOS/.zshrc')

    date = date.today()

    # print(platform.system())
    #commit the changes
    os.system("echo mac")
    # os.system(f'git commit -am "update {date}"')
    # os.system('git push')
