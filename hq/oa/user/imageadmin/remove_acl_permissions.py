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
