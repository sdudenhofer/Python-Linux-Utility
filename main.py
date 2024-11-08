import subprocess

#create class to update the system
def update_system():
    import distro
    distro = distro.name()
    if distro == 'Fedora Linux':
        executable = 'dnf'
    elif distro == 'Ubuntu Linux' or distro == 'Debian Linux':
        executable = 'apt'
    elif distro == 'Arch Linux':
        executable = 'pacman'
    else:
        print("System not compatible at the moment")

    result = subprocess.run(['bash', f'sudo {executable} update -y'], capture_output=True, text=True)
    print(result.stdout)

#start installing my software list
def install_software():
    import distro
    distro = distro.name()
    de = distro.id()
    if distro == 'Fedora Linux':
        executable = 'dnf'
    elif distro == 'Ubuntu Linux' or distro == 'Debian Linux':
        executable = 'apt'
    elif distro == 'Arch Linux':
        executable = 'pacman'
    else:
        print("System not compatible at the moment")
    print("Installing Initial software for the system...")
    initial_apps = subprocess.run(['bash', f'sudo {executable} install neovim git zsh wget curl uv direnv gh -y'], capture_output=True, text=True)
    ollama = subprocess.run(['bash', f'curl -fsSL https://ollama.com/install.sh | sh'], capture_output=True, text=True)
    atuin = subprocess.run(['bash', "curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh"], capture_output=True, text=True)
    github_cli = subprocess.run(['bash', 'gh auth login'], capture_output=True, text=True)
    if de == 'KDE Plasma':
        whitesur = subprocess.run(['bash', 'gh repo clone vinceliuice/WhiteSur-kde'], capture_output=True, text=True)
        whitesur_installation = subprocess.run(['bash', 'cd Whitesur-kde ./install.sh'], capture_output=True, text=True)
        print(whitesur.stdout + " | " + whitesur_installation)
    elif de == 'Gnome':
        whitesur_gtk = subprocess.run(['bash', 'gh repo clone vinceliuice/WhiteSur-gtk-theme'], capture_output=True, text=True)
        whitegtk_installation = subprocess.run(['bash', 'cd Whitesur-gtk ./install.sh'], capture_output=True, text=True)
        print(whitesur_gtk + " | " + whitegtk_installation)

    print(initial_apps.stdout)
    print(ollama.stdout)
    print(atuin.stdout)
    print(github_cli.stdout)

def install_vscode():
    vscode_keys = subprocess.run(['bash', """
                                     sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
                                    echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.
                                     microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=
                                     https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /
                                     etc/yum.repos.d/vscode.repo > /dev/null
                                     """
                                     ], capture_output=True, text=True)
    vscode_install = subprocess.run(['bash', """dnf check-update
                                    sudo dnf install code # or code-insiders
                                    """],capture_output=True, text=True)                                 
    print(vscode_keys.stdout + " | " + vscode_install.stdout)



def flatpak_install():
    print("Installing Flatpak Apps...")
    zen_install = subprocess.run(['bash', "flatpak install flathub io.github.zen_browser.zen"], capture_output=True, text=True)
    dropbox_install = subprocess.run(['bash', "flatpak install flathub com.dropbox.Client"], capture_output=True, text=True)
    github_install = subprocess.run(['bash', 'flatpak install flathub io.github.shiftey.Desktop'], capture_output=True, text=True)
    print(zen_install.stdout + " | " + dropbox_install.stdout + " | " + )github_install.stdout)


if __name__ == "__main__":  
    update_system()
    install_software()
    install_vscode()
    flatpak_install()