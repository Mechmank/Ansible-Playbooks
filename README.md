
# CI/CD Web Hosting Pipeline

This repository demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline designed to automate the deployment of a static website to a shared hosting environment using GitHub Actions.

## 🚀 Features

- **Automated Deployment**: Utilizes GitHub Actions to automatically deploy website changes to a shared hosting server via FTP.
- **Static Website Hosting**: Hosts static files including HTML, CSS, JavaScript, and SCSS.
- **Organized Structure**: Maintains a clean directory structure for easy management of website assets and deployment scripts.

## 📁 Project Structure

```
CI-CD-webhost/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow for deployment
├── hostfiles/                  # Directory containing website files
│   ├── index.html
│   ├── styles/
│   └── scripts/
├── run-script.txt              # Deployment script or instructions
└── README.md                   # Project documentation
```

## ⚙️ Getting Started

### Prerequisites

- A GitHub account with access to this repository.
- Access to a shared hosting server with FTP credentials.
- Basic knowledge of Git and GitHub Actions.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mechmank/CI-CD-webhost.git
   cd CI-CD-webhost
   ```

2. **Configure FTP Credentials**:
   - Navigate to the repository on GitHub.
   - Go to `Settings` > `Secrets and variables` > `Actions`.
   - Add the following repository secrets:
     - `FTP_HOST`: Your FTP server address.
     - `FTP_USERNAME`: Your FTP username.
     - `FTP_PASSWORD`: Your FTP password.

3. **Customize Website Content**:
   - Modify the files within the `hostfiles/` directory to update your website content.

4. **Commit and Push Changes**:
   ```bash
   git add .
   git commit -m "Update website content"
   git push origin main
   ```

   Upon pushing, GitHub Actions will trigger the deployment workflow defined in `.github/workflows/deploy.yml`.

## 🔄 Deployment Workflow

The `deploy.yml` workflow automates the following steps:

- **Checkout Repository**: Retrieves the latest code from the `main` branch.
- **FTP Deployment**: Connects to the specified FTP server and uploads the contents of the `hostfiles/` directory.
- **Post-Deployment Actions**: Executes any additional scripts or commands defined in `run-script.txt`.

This setup ensures that any changes pushed to the `main` branch are automatically deployed to your hosting server, streamlining the update process.

## 🛠️ Customization

- **Deployment Directory**: If your hosting server requires a specific directory structure, adjust the paths in the `deploy.yml` workflow accordingly.
- **Additional Workflows**: You can add more workflows for tasks like testing, linting, or backup by creating additional YAML files in the `.github/workflows/` directory.
- **Environment Variables**: For enhanced security and flexibility, consider adding more secrets or environment variables as needed.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## 📞 Support

For issues or questions, please open an [issue](https://github.com/Mechmank/CI-CD-webhost/issues) in the repository.
