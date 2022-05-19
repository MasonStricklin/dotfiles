" Inspired by vimrc taken from this website: https://vim.fandom.com/wiki/Example_vimrc

" Attempt to determine the type of a file based on its name and possibly its contents. Use this to allow intelligent
" auto-indenting for each filetype, and for plugins that are filetype specific
filetype indent plugin on

" Enable syntax highlighting
syntax on

" Better command-line completion
set wildmenu
 
" Show partial commands in the last line of the screen
set showcmd
 
" Highlight searches (use <C-L> to temporarily turn off highlighting; see the mapping of <C-L> below)
set hlsearch

" Use case insensitive search, except when using capital letters
set ignorecase
set smartcase

" When opening a new line and no filetype-specific indenting is enabled, keep the same indent as the line you're
" currently on. Useful for `READMEs, etc.
set autoindent
 
" Stop certain movements from always going to the first character of a line. While this behaviour deviates from that of
" Vi, it does what most users coming from other editors would expect.
set nostartofline

" Display the cursor position on the last line of the screen or in the status line of a window
set ruler

" Use visual bell instead of beeping when doing something wrong
set visualbell

" Enable use of the mouse for all modes
set mouse=a
 
" Display line numbers on the left
set number
 
" Indentation settings for using 4 spaces instead of tabs. Do not change 'tabstop' from its default value of 8 with
" this setup
set shiftwidth=4
set softtabstop=4
set expandtab

" Places a vertical line at the provided charcount. 120 is personal preference
set colorcolumn=120
