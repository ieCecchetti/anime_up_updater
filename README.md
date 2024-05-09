# anime_up_updater

## Description

Anime_up_updater is a simple script python able to collect informations about anime that actually `in airing` arount the globe. Go and check it if you are a fan!

## Table of Contents

- [anime\_up\_updater](#anime_up_updater)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Poetry](#poetry)
    - [Docker](#docker)
  - [Usage](#usage)
  - [Contributing](#contributing)
    - [Reporting Issues](#reporting-issues)
    - [Submitting Pull Requests](#submitting-pull-requests)
  - [License](#license)
  - [Next steps](#next-steps)

## Installation

The project has been built with poetry and docker. So for executing is necessary to install both.

### Poetry

To install, from the main proj folder, follows this steps:

1. Visit the [Poetry website](https://python-poetry.org/) to download the installer for your operating system.
2. Run the installer according to the instructions provided for your operating system.
3. After installation, verify that Poetry is installed correctly by opening a terminal or command prompt and typing:

```bash
poetry --version
```

This command should display the installed version of Poetry.
For more detailed installation instructions and usage guidelines, refer to the [Poetry Installation Guide](https://python-poetry.org/docs/).

Then for installing the project:

```bash
# in case you are using vscode: this will make vsCode recognise and create the .venv 
poetry config virtualenvs.in-project true
# create virtual env
poetry install
# activate the env
poetry shell
```

Then you are ready to launch it!

### Docker

To use also the storage in mongo, can be usefull to install docker-desktop. Here the steps:

1. Download Docker Desktop:
Go to the official Docker website: [Docker-Desktop](https://www.docker.com/products/docker-desktop). Click on the "Download for Mac" or "Download for Windows" button, depending on your operating system.
2. Install Docker Desktop:
   Once the download is complete, double-click the downloaded file to start the installation process.

   In case of MacOs you can do it with brew. To install Docker Desktop using Homebrew on macOS, open the terminal and type:

   ```bash
   brew update
   brew install --cask docker
   ```

3. Launch Docker Desktop:
   After the installation is complete, launch Docker Desktop from your applications menu or desktop shortcut.
4. Verify Installation:
   Open a terminal or command prompt and run the following command to verify that Docker is installed and running correctly:

   ```bash
   docker --version
   ````

Then you are ready. So before launching the script just type in your terminal (inside the proj folder):

```bash
docker compose up --build -d
```

This will start a detached docker container with your mongo db.

## Usage

After the configuration you can execute the script by typing:

```bash
poetry run script
```

This is the general way of using it. It will create a local file called for example `airing_anime_list_31-07_4_2024` containing the unfiltered anime list. This is a local file that will be used by the script to not re-download the data all the time (avoiding ban).
To have the filtered one is important to add the parameter `--filter-result` to the bash in addition to the specification of where to store it.

Actually you have 2 ways to store it:

1. Storing data in db

   ```bash
    poetry run script --db-conn-str "mongodb://localhost:27017/" --database "anime_up" --collection "my_airing_anime"
   ```

   In case you dont specify `database` and `collection` the default one will be chosen: "anime_up" for the db and "airing_anime" for the collection.
   As reported before, the code provides a simple docker-compose with a mongodb in case you want to test it. Just type `docker-compose up -d` to launch it. I will not provide any additional info on docker and docker compose usage.
2. Storing data into a specific file

   ```bash
   poetry run script --output-file "/Users/someone/Desktop" 
   ```

## Contributing

We welcome contributions to our project! If you would like to contribute, please follow these guidelines:

### Reporting Issues

If you encounter any issues with the project, please feel free to report them here. When reporting issues, please include detailed information such as steps to reproduce the problem, expected behavior, and actual behavior.

### Submitting Pull Requests

If you would like to contribute code to the project, you can submit a pull request. Here's how:

1. Fork the project repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Push your changes to your fork.
5. Submit a pull request to the main project repository.

Please make sure your code follows our coding standards and includes appropriate documentation. We'll review your pull request and provide feedback as needed.

Thank you for contributing to our project!

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes. See the LICENSE file for more details.

## Next steps

- [ ] Suggest me something
