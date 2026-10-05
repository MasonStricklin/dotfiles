## macOS settings

- System Settings > Desktop & Dock > Mission Control > Hot Corners…: disable all four hot corners
- System Settings > Mouse:
  - Turn off “Natural scrolling”
  - Set “Tracking speed” to one or two ticks below maximum
- System Settings > Desktop & Dock > Windows: turn on “Hold ⌥ key while dragging windows to tile”
- System Settings > Desktop & Dock: set “Click wallpaper to reveal desktop” to “Only in Stage Manager”
- System Settings > Displays:
  - Arrangement: match physical positions and pointer transitions
  - Resolution: match external monitors; the Mac display may differ
  - Main display: consider the center monitor or MacBook display
- System Settings > Desktop & Dock: set “Dock position on screen” to “Right”
- Finder > Home (`~`) > Pictures: create a `Screenshots` folder
  - Control-click `Screenshots` > Customize Folder…: add the picture symbol
- Physical Dock:
  - Add Downloads, Home (`~`), and Screenshots below the divider, ordered top to bottom
  - Control-click each folder > “Display as” > “Folder”
  - Control-click Home (`~`) > “Sort by” > “Name”
  - Control-click Downloads and Screenshots > “Sort by” > “Date Created”
- Press ⌘⇧5 > Options:
  - “Save to” > “Other Location…”: select `~/Pictures/Screenshots`
  - Turn off “Show Floating Thumbnail”
- System Settings > Appearance: set “Appearance” to “Dark”
- System Settings > Appearance: set “Show scroll bars” to “Always”
- System Settings > Wallpaper: select a solid-color wallpaper; get the hex color from `kiln` (use the eyedropper)
- System Settings > Appearance: set “Folder color” to a custom color that matches the solid-color wallpaper
- System Settings > Menu Bar:
  - Ensure Clock, Battery, Bluetooth, Sound, and Now Playing are shown
  - Set Sound and Now Playing to “Always Show”
  - Battery > Battery Options…: turn on “Show Percentage”
  - Clock > Clock Options…: turn on “Show AM/PM”
  - Clock > Clock Options…: turn on “Display the time with seconds”
  - Set “Automatically hide and show the menu bar” to “Never”
  - Turn on “Show menu bar background”
  - Set “Recent documents, applications, and servers” to “None”
  - Menu Bar > Add Controls…: remove all controls (out of protest)
  - [Suggested] Reorder menu bar items by holding ⌘ while dragging, from left to right: company VPN/company-specific app, Rectangle, Bluetooth, Wi-Fi, Sound, Now Playing, Battery
  - [Suggested] “Allow in the Menu Bar” > installed-app controls: show only the company VPN/company-specific app and Rectangle
- System Settings > Users & Groups > click ⓘ next to the user > click the profile picture: choose “Emoji,” select a standard emoji, and set a solid-color background
- System Settings > Touch ID & Password: add both index fingers
- Finder > Settings > Advanced: turn on “Show all filename extensions”

## Software

- Install Firefox, Brave, and Chrome
  - Firefox: [Download](https://www.firefox.com/)
  - System Settings > Desktop & Dock > Default web browser: select Firefox
  - Each browser > Settings > Search engine: set the address-bar search engine to Google
  - Each browser > Help: enable “Warn Before Quitting” (⌘Q) where supported
  - Firefox > Settings > Account and sync:
    - Personal machine: sign in with the primary email, turn on Sync (bookmarks, history, open tabs, passwords, addresses, payment methods, add-ons, settings)
    - Work machine: do not sign in / do not sync. Set everything below by hand instead.
  - Firefox manual settings (work machine, or any machine not using Sync):
    - Home and startup
      - Startup: “open previous windows and tabs” off, “open automatically on login” off
      - Homepage + new tabs: Firefox Home (Default)
      - Firefox Home: Search on, Weather on; Shortcuts off, Stories off, Recent activity off
    - Search
      - Default engine: Google; show search terms in address bar: on
      - Suggestions: all on (general, before-history, private windows, trending); Firefox Suggest (history, bookmarks): on
    - Privacy and security
      - Enhanced Tracking Protection: Strict
      - Data collection: send technical/interaction data to Mozilla — off; personalized extension recommendations — off; feature studies — off
    - Passwords and autofill
      - Bitwarden controls password management (see below); native save-password prompt off
      - Require device sign-in to manage passwords: off
      - Save/autofill payment info: off
      - Save/autofill addresses: on
    - Appearance
      - Website appearance: System; window density: Automatic
      - Browser theme: “Biscuit {Mojas84}” (custom, from addons.mozilla.org) if available, else closest default
    - Downloads
      - Save to Downloads, don’t ask each time
      - Open in Firefox: AV1, JPEG XL, PDF, WebP. Save File: XML, SVG. mailto: Use Mail.
      - Other files: automatically save
    - Tabs and browsing
      - Browser layout: Vertical tabs
      - Open links in tabs not new windows: on
      - Image preview on tab hover: on; AI tab/tab-group suggestions: on; drag tabs to create groups: on
      - Use Container Tabs: on
      - Ask before quitting with ⌘Q: on; ask before closing multiple tabs: off
      - Link previews: on (AI key points: off; long-press shortcut: on)
    - Accessibility
      - Font family: Optima; font size: 16; website contrast override: off
    - Languages
      - Browser language: English (US); full page translation: on; spell check as you type: on
    - AI controls
      - AI enhancements: not blocked; on-device AI (translations, speech recognition, alt text, tab-group suggestions, link-preview key points): available; chatbot in sidebar: available
    - Permissions and data
      - Block pop-ups and third-party redirects: on; warn before installing extensions: on
    - Firefox Labs
      - Media: JPEG XL: on; address-bar IME and tab notes: off
    - Extensions: Bitwarden Password Manager, uBlock Origin

- Install either Bitwarden or 1Password
  - Install the desktop app
  - Brave, Chrome, and Firefox > Extensions: install the corresponding extension in each browser

- Install Ghostty: [Download](https://ghostty.org/download)
  - `brew install --cask font-dm-mono`
  - Config lives at `~/.config/ghostty/config`, symlinked to this repo's `config.ghostty`
  - `theme = Gruvbox Material Dark`; `font-family = DM Mono`

- Install Zed: [Download](https://zed.dev/download)
  - All settings live in this repo's `zed-settings.json`, symlinked to `~/.config/zed/settings.json`
  - Open code files in Zed: `brew install duti`, then run `duti default-apps.duti` from this repo; accept each macOS pop-up

- Shell: `~/.zshrc`, `~/.vimrc`, and `~/.hushlogin` are symlinked to this repo's copies

- Install Claude Code CLI: [Installation instructions](https://code.claude.com/docs/en/setup)

- Install Codex: [Desktop app setup](https://developers.openai.com/codex/app)

- Install Rectangle and configure it to open at login
  - Rectangle > Settings: turn on “Green stoplight button maximizes instead of Full Screen”
  - Rectangle > Settings: turn on “Check for updates automatically”
  - Rectangle > Settings: set “Repeated commands” to “cycle sizes on side actions”
    - Enable all repeated-command sizes: ½, ⅔, ¾, ¼, and ⅓

- Install Logi Options+: [https://www.logitech.com/en-us/software/logi-options-plus.html](https://www.logitech.com/en-us/software/logi-options-plus.html)
  - Logi Options+ > select the mouse > Buttons: verify that the Mission Control button works as desired
  - Logi Options+ > select the mouse > Buttons > Gesture Button > Custom:
    - Assign the left gesture to “Desktop Left”
    - Assign the right gesture to “Desktop Right”
  - Logi Options+ > select the mouse > Point & Scroll: set horizontal scroll direction to “Inverted”

- Install Spotify (Personal)
  - Spotify > Settings > Startup and window behaviour: set “Open Spotify automatically after you log into the computer” to “No”
