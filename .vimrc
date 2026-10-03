" Language — detect filetype; load its settings/indent rules; color syntax
filetype indent plugin on
syntax on

" Search — preview/highlight matches; capitals make searches case-sensitive.
" Example: /hello ignores case; /Hello respects it.
set incsearch
set hlsearch
set ignorecase
set smartcase
" Ctrl-L clears search highlights and redraws the screen.
nnoremap <silent> <C-L> :nohlsearch<CR><C-L>

" Indentation — carry indent to new lines; use four spaces instead of tabs
set autoindent
" Example: >> and << indent/unindent by four spaces.
set shiftwidth=4
set softtabstop=4    " Tab/Backspace move in four-space steps while typing.
set expandtab
set nostartofline   " Keep cursor column on moves that otherwise jump to line start.

" Feedback — completion choices, unfinished commands, and cursor position
" Example: :colorscheme <Tab> shows completion choices.
set wildmenu
" Example: the first d of dd appears while the command is unfinished.
set showcmd
set ruler           " Show cursor line/column.
set number          " Show line numbers beside the text.
set mouse=a         " Enable mouse interaction in all modes.
set visualbell      " Visual feedback instead of an audible error bell.
set colorcolumn=120 " Draw a column guide; does not wrap or limit line length.

" Undo — u still works after reopening a file; store history outside projects
if has('persistent_undo')
    let &undodir = expand('~/.vim/undo')
    call mkdir(&undodir, 'p', 0700) " Create missing parents; owner-only access.
    set undofile
endif
