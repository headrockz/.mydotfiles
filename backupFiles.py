from datetime import date
import platform
import os

"""
I use two different operating systems, Linux and macOS, basically the dotfiles are the same, but there may be differences in each one, so it is necessary to check which system the script is running on
"""

date = date.today()

if (platform.system() == 'Linux'):

    # copy my dotfiles to repository folder
    os.system('cat ~/.zshrc > .zshrc')

    #commit the changes
    os.system('echo "Commit dotfiles"')
    os.system(f'git commit -am "update {date}"')
    os.system('git push')
    os.system('echo "Have a nice day!"')

else:
    # copy my dotfiles to repository folder
    os.system('cat ~/.zshrc > ./macos/.zshrc')



    #commit the changes
    os.system('git add .')
    os.system('echo "Commit dotfiles"')
    os.system(f'git commit -am "update {date} MacOS"')
    os.system('git push')
    os.system('echo "Have a nice day!"')