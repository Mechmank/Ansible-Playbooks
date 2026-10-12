#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import csv


def export_file(in_data, out_name):
    with open('/root/ansible/' + out_name + '.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(in_data)


def main():
    fields = {
        "input": {"required": True, "type": "list"},
        "output": {"required": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    in_data = module.params['input']
    out_name = module.params['output']
    export_file(in_data, out_name)
    module.exit_json(changed=False, msg='file has been created')


if __name__ == "__main__":
    main()



=======================================================================================================

# How to use

---
- name: OS_version identifier
  hosts: all
  tasks:
    - name: Setting facts
      set_fact:
        details:
          - "{{ inventory_hostname }}"
          - "{{ ansible_facts['hostname'] }}"
          - "{{ ansible_facts['os_family'] }}"

    - name: Exporting output
      export_out:
        input: "{{ details }}"
        output: output
      delegate_to: localhost
