
# Ansible Playbooks Collection

This repository contains a collection of Ansible playbooks designed to automate various system administration tasks, particularly for managing Windows environments and sending email notifications.

## 📁 Repository Structure

```
Ansible-Playbooks/
├── CDrive_space.yml       # Playbook to check C: drive space on Windows hosts
├── send_mail.yml          # Playbook to send emails
├── Windows-Inventory/     # Directory containing Windows inventory files
└── README.md              # Project documentation
```

## ⚙️ Getting Started

### Prerequisites

- Ansible installed on your control node.
- Target hosts (Windows or Linux) accessible via SSH or WinRM.
- Properly configured inventory files.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mechmank/Ansible-Playbooks.git
   cd Ansible-Playbooks
   ```

2. **Configure Inventory**:
   - Edit or create your inventory files under `Windows-Inventory/`.
   - Make sure to set correct hostnames, user credentials, and connection settings (especially for WinRM with Windows hosts).

### Running Playbooks

Use the following command format to run any playbook:

```bash
ansible-playbook -i Windows-Inventory/your_inventory_file.ini playbook_name.yml
```

Replace `your_inventory_file.ini` with your actual inventory filename and `playbook_name.yml` with the desired playbook.

## 📝 Available Playbooks

### `CDrive_space.yml`

- **Purpose**: Checks the available disk space on the C: drive of remote Windows machines.
- **Usage**:
  ```bash
  ansible-playbook -i Windows-Inventory/hosts.ini CDrive_space.yml
  ```

### `send_mail.yml`

- **Purpose**: Sends a formatted email, useful for notifications after other automation tasks.
- **Note**: You may need to configure the SMTP server and authentication details within the playbook variables.

## 🛠️ Customization

- You can easily add new playbooks to automate other tasks.
- Use Jinja2 templates and variables for dynamic configuration.

## 🧪 Testing

Before deploying on production systems, it is advisable to test the playbooks on a sandbox or staging environment to ensure safety and accuracy.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

Pull requests are welcome! Please fork the repository, make your changes, and submit a pull request.

## 📞 Support

For issues or suggestions, open an [issue](https://github.com/Mechmank/Ansible-Playbooks/issues) in the repository.
