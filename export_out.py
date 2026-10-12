#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import csv
import json

import time
#date_string = '{{output_file}}'
#date_string = time.strftime("%Y-%m-%d_%H-%M")
# a1 = ['xyz']
# a2 = ['def']
# a3 = 'one.com'
# data = a1 + a2 + [a3]
# os.remove('patching.csv')
def export_file(input,output):
    with open('/root/ansible/' + output + '.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def main():
    fields = {
        "input": {"required": "true", "type": "list"},
        "output": {"required": "true", "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    data = module.params['input']
    date_string = module.params['output']
    export_file(input,output)
    module.exit_json(changed=False, msg='file has been created')


if __name__ == "__main__":
    main()
