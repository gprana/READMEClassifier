takeown: delegate file ownership takeover to unprivileged users
===============================================================

Brief usage:

    takeown [-T] [-r] [-s] PATH
    takeown [-T] -a USER PATH...
    takeown [-T] -l PATH...
    takeown [-T] -d USER PATH...

INTRO
-----

`takeown` allows administrators to delegate taking ownersip ownership of files
and directories to non-administrators.  It uses the set-uid bit to gain the
necessary privileges to do so.

Example: the administrator wants to let the user `pablo` take over ownership
of files in `/var/shared/Incoming`.  To that effect, the administrator runs:

    takeown -a pablo /var/shared/Incoming

Once he has done so, the user `pablo` can run the command:

    takeown /var/shared/Incoming/some-file.txt

and `takeown` will change the owner of the file `some-file.txt` to `pablo`.

Each delegation is recorded in a file `.takeown.delegations` stored in the
root directory of the volume containing the delegated file / directory.

Delegations recorded on a volume only apply to files and directories
stored in the volume.  Delegations do not propagate across mount points.
If a user has been granted a delegation on a directory, he will be
authorized to take ownership of any files contained in that directory,
so long as said files are in the same volume.

The flag `-r` in the takeown command induces takeown to grant ownership to the
invoking user recursively across all files and subdirectories of the specified
paths.  The caveat about not crossing mount points applies -- if another
volume is mounted within the path specified to a `takeown -r` command, that
volume will be skipped silently.

For security reasons, attempts by an authorized user to take ownership of
a volume or ownership of the delegation record file will be silently ignored.

DELEGATING OWNERSHIP TO AN USER
-------------------------------

To allow a user to take ownership of files under a directory, or specific
files, run:

    takeown username /path/to/directory/or/file...

This will delegate the taking of ownership to the user, allowing him to run
`takeown` to take ownership of any file within the specified paths.

WARNING: if you delegate the taking of ownership of a volume to a user,
that user may take ownership of the volume itself, and then remove the
delegation store.  This is not a security issue -- it does not grant the
user any extra privileges -- but it does prevent future uses of `takeown`
by unprivileged users in that volume.

REVOKING DELEGATIONS
--------------------

To revoke an established delegation, use the following command:

    takeown -d username /delegated/path

This removes the specific delegation established for that user name.

LISTING DELEGATIONS
-------------------

Any user may list established delegations with the command:

    takeown -l [PATH]

However, only the administrator may list delegations for all users.  Other
users will only get to see the delegations assigned to him.

SIMULATING TAKING OWNERSHIP
---------------------------

The action of taking ownership can be simulated with flag `-s`.  In this mode,
`takeown` will print what it would do rather than changing the file system.

TRACING
-------

If a file `/.trace` exists in the root directory, the user is allowed to
specify the flag `-T`, which causes the program to print tracing information,
useful to debug problems with the program.

LICENSE
-------

This program is published under the GNU GPL version 3 or later.
