# Source Code for the CS2103 Module Website
This repo hosts the source code for the CS2103 (Software Engineering) module at [SoC (NUS)](http://www.comp.nus.edu.sg)

## Released version
The **released version** of this website is available [here](http://www.comp.nus.edu.sg/~cs2103/). 
The released version may be behind the latest version in this repo.

## Contributing
**We welcome contributions from current/past CS2103 students**. 

The easiest way to contribute is to post bugs and suggestion in our issue tracker.

If you would like to contribute code, here is the procedure:

1. Fork this repo.
2. Make sure what you want to contribute is already listed as an open issue in our issue tracker. 
   If it is not, post it as an issue first and wait for it to get accepted (an issue is considered 
   'accepted' when it is assigned a `priority.*` label).
2. You may choose an issue labeled `forFirstTimers` as your first issue, if there are any. 
   But do not do more than one `forFirstTimers` issues.
3. Clone your fork onto your Computer.
4. Create a branch. The branch name should be in the format `issue-number-some-key-words`
   i.e. issue number followed by 2-4 key words related to the issue description
   e.g. `12-broken-link-week1-schedule`
5. Implement your fix in the new branch.
   * Use 2 spaces for indenting (not `tab`, not 4 or 8 spaces)
   * Minimize inline styles. 
   * When in doubt, you can refer to these style guides from the 
     TEAMMATES project:
     [JavaScript](https://docs.google.com/document/d/1gZ6WG6HBTJYHAtVkz9kzi_SUuzfXqzO-SvFnLuag2xM/pub?embedded=true),
     [CSS](https://docs.google.com/document/d/1wA9paRA9cS7ByStGbhRRUZLEzEzimrNQjIDPVqy1ScI/pub), 
     [HTML](https://cdn.rawgit.com/nus-cs2103/website/master/contents/coding-standards-html.html)
6. Test the code in your computer. <br>
   Tip: When testing local html files, some JavaScripts might not work
   in Firefox or Chrome. In that case you can use IE. Alternatively, you can [start a web server
   in your Computer](https://gist.github.com/willurd/5720255)
7. When the fix is ready, 
   1. Ensure that your fork has the latest code from this repo (the repo you forked from is called
      the 'upstream` repo). The code in the upstream repo may have been updated while you were fixing the issue. 
      If that is the case, [sync your fork with upstream repo](https://help.github.com/articles/syncing-a-fork/)
   2. Stage your changes:<br>
      Your reviewer might want to see how your changes look like to a viewer of the website. To create a [*staging 
      site*](https://en.wikipedia.org/wiki/Staging_site) using [*GitHub Pages* feature](https://help.github.com/categories/github-pages-basics/), create a branch called `gh-pages`, merge your branch to the `gh-pages` branch 
      and push the `gh-pages` branch to your fork. A running version of the website should now be available from
      the corresponding `github.io` URL. Here is an example [http://bobby-lin.github.io/website/](http://bobby-lin.github.io/website/).
   3. Push the code to your fork and create a pull request (PR) against the master 
      branch of this repo.<br>
      When naming the PR, copy paste the name of the issue you are fixing, including the original issue number.<br>
      e.g. `Handbook TOC links are not working in iPhone browser #19` <br>
      In the PR description, mention `Fixes #IssueNumber` (e.g. `Fixes #24` so that the corresponding issue
      is closed automatically when the PR is merged.<br>
      Remember to mention the URL of the staging site in your PR description. [Here](https://github.com/nus-cs2103/website/pull/78)
      is an example.
   3. Check the diff view of the PR to ensure it contains the intended changes only.
8. Your code will be reviewed by someone from the dev team. If the reviewer requests changes,
   revise the code, push the new commits to your branch, and post a comment to say the pull request
   is ready for review again.
9. When your code is acceptable, it will be merged to this repo. Your fix will be included in the 
   next release of the website.
10. After your fix is merged, you may wish to create another PR to add your name to the [`CONTRIBUTORS.md`](CONTRIBUTORS.md) file. 
    There is no need to create a corresponding issue for that PR.

## Acknowledgements
Many thanks to our [contributors](CONTRIBUTORS.md). 
