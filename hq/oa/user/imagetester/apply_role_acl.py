from qumulo.rest_client import RestClient

class ApplyRoleACL:
    def __init__(self, in_args):
        pass

    @staticmethod
    def apply_acl(rc, path):
        # Define the desired ACL based on the specific role
        role_acl = [
            {
                "principal": "user:imagetester",
                "permissions": ["fs_read_data", "fs_write_data", "fs_append_data", "fs_read_attr", "fs_write_attr", "fs_read_xattr", "fs_write_xattr", "fs_execute", "fs_read_acl", "fs_write_acl", "fs_write_owner", "fs_synchronize"],  # Adjust the permissions as needed for the role
                "principal_type": "user"
            }
        ]
        rc.fs.set_acl_v2(path=path, acl={'acl': role_acl})

    def every_batch(self, file_list, work_obj):
        for file_info in file_list:
            self.apply_acl(work_obj.rc, file_info['path'])

    @staticmethod
    def work_start(work_obj):
        pass

    @staticmethod
    def work_done(work_obj):
        pass
