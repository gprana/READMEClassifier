# wp-github-updater
[![Travis Build Status](https://img.shields.io/travis/medfreeman/wp-github-updater.svg?label=build)](https://travis-ci.org/medfreeman/wp-github-updater)

Wordpress plugin that enables automatic updates of plugins and themes from github

## Installation
Download latest zip archive and decompress into your wordpress plugins folder, then activate.

## Usage
- Host your plugin or theme on github
- Make sure your plugin php file or your theme style.css file has its Plugin URI or Theme URI entry set to a github repository url (e.g. https://github.com/me/my-wp-plugin-or-theme)
- Tag the plugin or theme versions you want to be proposed as updates, *ONLY* use version numbers as tags (e.g. 1.2.0), an update will show if this version is higher than the one currently instaled (as set in current Version tag in plugin php or theme style.css file)
- Make releases from your tags (if done manually, you have to add release notes to your tag on github so it becomes a release)
- If needed you can add a github release asset to your release, it will be installed instead of your plugin or theme source code (e.g. your repository has install tasks, dependencies that have to be built by a CI system or manually)

### For plugins

Add the following code to your plugin main php file (this example is for use with a plugin class, adapt for another structure):
````
...

class myplugin {

...

function __construct() {

...
    add_action( 'admin_init', array( $this, 'handle_github_update' ) );
...

}

...

	/**
	 * Handles github plugin update by using
	 * github updater class from wp-github-updater plugin.
	 */
	function handle_github_update() {
		if ( class_exists( 'GitHubUpdater' ) ) {
		  new GitHubUpdater( 'plugin', __FILE__ );
		}
	}
	
...

}
````

### For themes

Add the following code to your theme functions php file (make sure the second argument to GitHubUpdater class instantiation points to your theme root, e.g. \__DIR\__ if your functions.php file is in the root of your theme, adapt if not):
````
...

add_action( 'admin_init', 'myprefix_handle_github_update' );

...

if ( ! function_exists( 'myprefix_handle_github_update' ) ) {
	/**
	 * Handles github theme update by using
	 * github updater class from wp-github-updater plugin.
	 */
	function myprefix_handle_github_update() {
		if ( class_exists( 'GitHubUpdater' ) ) {
		  new GitHubUpdater( 'theme', __DIR__ );
		}
	}
}
````

That's all folks!
