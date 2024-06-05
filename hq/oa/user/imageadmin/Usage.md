To run the `qwalk.py` script from the Qumulo filesystem walk repository and modify the ACLs for the "imageadmin" user to remove "delete" and "rename" permissions from the "testimagedata" directory and all its subdirectories and files on a Windows OS SMB-mounted 'Z' drive, follow these steps:

1. **Download the repository**:
   - Clone the repository from GitHub:
     ```bash
     git clone https://github.com/Qumulo/qumulo-filesystem-walk.git
     ```
   - Navigate into the directory:
     ```bash
     cd qumulo-filesystem-walk
     ```

2. **Set up your environment**:
   - Ensure you have the required dependencies installed. You might need to install the `qumulo-api` package:
     ```bash
     pip install qumulo-api
     ```

3. **Create a custom task for ACL updates**:
   - Create a new Python file, e.g., `remove_acl_permissions.py`, inside the `qtasks` directory:
     ```python
     from qumulo.rest_client import RestClient

     class RemoveACLPermissions:
         def __init__(self, in_args):
             pass

         @staticmethod
         def remove_permissions(rc, path):
             acl = rc.fs.get_acl_v2(path=path)
             new_entries = []
             for entry in acl['acl']:
                 if entry['principal'] == 'user:imageadmin':
                     entry['permissions'] = [perm for perm in entry['permissions'] if perm not in ['fs_delete', 'fs_rename']]
                 new_entries.append(entry)
             rc.fs.set_acl_v2(path=path, acl={'acl': new_entries})

         def every_batch(self, file_list, work_obj):
             for file_info in file_list:
                 self.remove_permissions(work_obj.rc, file_info['path'])

         @staticmethod
         def work_start(work_obj):
             pass

         @staticmethod
         def work_done(work_obj):
             pass
     ```

4. **Edit `qwalk.py` to include your custom task**:
   - Open `qwalk.py` and add your custom task to the `QTASKS` dictionary:
     ```python
     from qtasks.remove_acl_permissions import RemoveACLPermissions

     QTASKS = {
         # ... other tasks ...
         'RemoveACLPermissions': RemoveACLPermissions,
     }
     ```

5. **Run the `qwalk.py` script**:
   - Now you can run the `qwalk.py` script specifying the new task `RemoveACLPermissions` to walk through the directory and update the ACLs:
     ```bash
     python qwalk.py -s <QUMULO_HOSTNAME> -u <USERNAME> -p <PASSWORD> -d Z:/testimagedata -c RemoveACLPermissions -g
     ```
   Replace `<QUMULO_HOSTNAME>`, `<USERNAME>`, and `<PASSWORD>` with your actual Qumulo cluster details.

This script will walk through the "testimagedata" directory and apply the specified ACL updates recursively to all subdirectories and files. The `remove_acl_permissions.py` script ensures that "delete" and "rename" permissions are removed for the "imageadmin" user from each file and directory.

For more details, you can refer to the original repository [here](https://github.com/Qumulo/qumulo-filesystem-walk)【20†source】【21†source】.