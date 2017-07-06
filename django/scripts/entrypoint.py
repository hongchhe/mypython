#!/usr/bin/env python

import sys
import os
import subprocess

def main(path):

    manage_cmd = "python " + os.path.join(path,"manage.py")
    updateUserPassword = "import uicloud.management.setPassword as setPassword; setPassword.run();"
    createPermission = "import uicloud.management.addViewPermissions as perm; perm.add_view_permissions();"
    cmd_args_list = [
        "makemigrations polls",
        "sqlmigrate polls 0001",
        "migrate",
        "createsuperuser --username django --email test@test.com --noinput",
        "shell -c {}".format(updateUserPassword),
        "shell -c {}".format(createPermission),
        "runserver 0:8000"
        ]

    for args in range(len(cmd_args_list)):
    	subprocess.Popen("{0} {1}".format(manage_cmd, args))

    os.wait();

if __name__ == "__main__":
    root_path= "/home/django/projects/uicloud"
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    main(root_path)
