# qq commands

qq fs_walk_tree --path /testimagedata | \
  jq -r '.tree_nodes[].path' | \
    xargs -d '\n' -I % -n1 -P 4 \
      qq fs_modify_acl --path '%' \
        add_entry -t "local:imageadmin" \
          -y Allowed \
          -r "Read" "Execute/Traverse" "Write file" \
          -f "Object inherit" "Container inherit"

qq fs_walk_tree --path /testimagedata/tab1 | \
  jq -r '.tree_nodes[].path' | \
    xargs -d '\n' -I % -n1 -P 4 \
      qq fs_modify_acl --path '%' \
       remove_entry -p 3


qq fs_walk_tree --path /testimagedata/tab1 | \
  jq -r '.tree_nodes[].path' | \
    xargs -d '\n' -I % -n1 -P 4 \
      qq fs_get_acl --path '%'



time qq fs_walk_tree --path /testimagedata | \
  jq -r '.tree_nodes[].path' | \
    xargs -d '\n' -I % -n1 -P 4 \
      qq fs_modify_acl --path '%' \
        modify_entry --old-trustee "local:imageadmin" \
          --new-rights "Read" "Execute/Traverse" "Write file" \
          --new-flags "Object inherit" "Container inherit"


admin@QNAS-5:~$ qq fs_modify_acl --path "/testimagedata" modify_entry -h
usage: qq fs_modify_acl modify_entry [-h] [-p POSITION] [--old-trustee OLD_TRUSTEE] [--old-type {Allowed,Denied}] [--old-rights RIGHT [RIGHT ...]] [--old-flags [FLAG [FLAG ...]]] [--new-trustee NEW_TRUSTEE] [--new-type {Allowed,Denied}]
                                     [--new-rights RIGHT [RIGHT ...]] [--new-flags [FLAG [FLAG ...]]] [-a] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -p POSITION, --position POSITION
                        The position of the entry to modify.
  --old-trustee OLD_TRUSTEE
                        Modify an entry with this trustee. e.g. Everyone, uid:1000, gid:1001, sid:S-1-5-2-3-4, or auth_id:500
  --old-type {Allowed,Denied}
                        Modify an entry of this type
  --old-rights RIGHT [RIGHT ...]
                        Modify an entry with these rights. Choices: All, Read, Take ownership, Write directory, Write file, Add file, Add subdir, Change owner, Delete, Delete child, Execute, Execute/Traverse, Extend, Extend file, Modify, Read ACL, Read EA, Read
                        attr, Read contents, Synchronize, Traverse, Write ACL, Write EA, Write attr, Write data, Write group
  --old-flags [FLAG [FLAG ...]]
                        Modify an entry with these flags. Choices: Container inherit, Inherit only, Inherited, No propagate inherit, Object inherit
  --new-trustee NEW_TRUSTEE
                        Set the entry to have this trustee. e.g. Everyone, uid:1000, gid:1001, sid:S-1-5-2-3-4, or auth_id:500
  --new-type {Allowed,Denied}
                        Set the type of the entry.
  --new-rights RIGHT [RIGHT ...]
                        Set the rights of the entry. Choices: All, Read, Take ownership, Write directory, Write file, Add file, Add subdir, Change owner, Delete, Delete child, Execute, Execute/Traverse, Extend, Extend file, Modify, Read ACL, Read EA, Read attr,
                        Read contents, Synchronize, Traverse, Write ACL, Write EA, Write attr, Write data, Write group
  --new-flags [FLAG [FLAG ...]]
                        Set the flags of the entry. Choices: Container inherit, Inherit only, Inherited, No propagate inherit, Object inherit
  -a, --all-matching    If multiple entries match the arguments, modify all of them
  -d, --dry-run         Do nothing; display what the result of the change would be.
