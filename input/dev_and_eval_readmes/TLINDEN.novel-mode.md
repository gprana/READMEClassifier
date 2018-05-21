# novel-mode
Emacs Screen Reader

# Demo

![demo](https://raw.githubusercontent.com/TLINDEN/novel-mode/master/demo.gif)

# Introduction

Novel  mode is  a minor  mode which  converts emacs  into a  screen
reader, or in other words,  it enables distraction free reading. It
is however not  suited for distraction free  editing. Try writeroom
mode if you're looking for this.

When turned on, it does the following conversions:

  - disable almost all distractions, as menu, toolbar, scrollbar
  - enlarge font size
  - switch to variable width font
  - enable word wrap (without fringe marker)
  - increase line spacing
  - add a window margin to the left and right (thereby centering the text)
  - disable all input keys (rendering the buffer read-only)
  - disable the cursor
  - switch to buffer-scrolling (like e.g. in Acroread)
  - display current reading position in percent
  - add a couple of convenience one-key commands

Novel mode provides the following one-key commands, when active:

    n           scroll one page down
    p           scroll one page up
    <down>      scroll one line down
    <up>        scroll one line up
    mousewheel  scroll linewise up or down
    SPC         scroll one page down
    <left>      increase margins, makes visible text narrower
    <right>     decrease margins, makes visible text wider
    +           increase font size
    -           decrease font size
    i           invert video display
    q           quit novel mode
    ?           display key mapping

Important: while normal  key input (beside the  ones listed above),
is disabled, Control and Meta still work, of course. Please be also
aware that this mode might conflict with god-mode or evil-mode.

If you use this  mode quite often, then it might be  a good idea to
use save-place mode,  so that a text file will  be opened where you
left last time (just like any  ebook reader would do). Here's how to
do that:

    (if (version< emacs-version "25.0")
        (progn
          (require 'saveplace)
          (setq-default save-place t))
      (save-place-mode 1))


The name  novel mode is  not my idea,  there's a function  on Xah's
ergomacs   page  with   a  function   for  this   kind  of   stuff:
http://ergoemacs.org/emacs/emacs_novel_reading_mode.html.  In fact,
this mode is based on this function, I had it in my .emacs file and
enhanced it  all the  time.  At  some point it  made more  sence to
maintain this baby in its own mode - hence novel-mode.

# Install

To use, save novel-mode.el to a directory in your load-path.

Add something like this to your config:

    (require 'novel-mode)
    (add-hook 'text-mode-hook 'novel-mode)

or load it manually, when needed:

    M-x novel-mode

# Customize

You can customize the following variables:

To setup a default left and right margin, use this:

    (setq novel-default-margin 50)

All available  novel-mode variables  can be  modified interactively
with:

     M-x customize-group RET novel-mode RET

You can also use hooks to novel  mode as a way to modify or enhance
its behavior.  The following hooks are available:

    novel-mode-pre-start-hook
    novel-mode-post-start-hook
    novel-mode-pre-stop-hook
    novel-mode-post-stop-hook

Example:

    (add-hook 'novel-mode-post-start-hook
              (lambda ()
                (set-face-font 'default "DejaVu Sans")))
    (add-hook 'novel-mode-post-stop-hook
              (lambda ()
                (set-face-font 'default "Courier")))

# Meta


Copyright (C) 2016, T.v.Dein <tlinden@cpan.org>

This file is NOT part of Emacs.

This  program is  free  software; you  can  redistribute it  and/or
modify it  under the  terms of  the GNU  General Public  License as
published by the Free Software  Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT  ANY  WARRANTY;  without   even  the  implied  warranty  of
MERCHANTABILITY or FITNESS  FOR A PARTICULAR PURPOSE.   See the GNU
General Public License for more details.

You should have  received a copy of the GNU  General Public License
along  with  this program;  if  not,  write  to the  Free  Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
USA

    - Version: 0.01
    - Author: T.v.Dein <tlinden@cpan.org>
    - Keywords: read books novels
    - URL: https://github.com/tlinden/novel-mode
    - License: GNU General Public License >= 2
