
# **CRUD Flask and SQL Server**

<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p align="center">
    Template for a CRUD (Create, Read, Update, and Delete) using Flask (Python) and Microsoft SQL Server
    <br />
    <a href="https://github.com/ErickOF/CRUD-Flask-SQLServer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ErickOF/CRUD-Flask-SQLServer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ErickOF/CRUD-Flask-SQLServer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This template is a CRUD (Create, Read, Update. and Delete) built with Flask and Microsoft SQL Server. This contains only a User Table:

|          User          |
|------------------------|
| id_card: INT           |
| id_user: INT           |
| [name]: VARCHAR(30)    |
| last_name: VARCHAR(30) |
| phone_number: INT      |
| email: VARCHAR(100)    |

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

### Built With

[![Python][Python3]][Python-url]
[![Flask][PyFlask]][Flask-url]
[![SQLServer][MSSQLServer]][SQLServer-url]


<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.12.
* SQL Server 2022.
* Microsoft SQL Management Studio 20.


### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/ErickOf/CRUD-Flask-SQLServer.git
   ```

2. Install Python packages

   ```sh
   pip install -r requirements.txt
   ```

3. Create a DB in Microsoft SQL Management Studio.

4. Update JSON file in `API/config/development.json` with DB configuration:

```json
{
    "user": "<db-user>",
    "password": "<db-password>",
    "host": "localhost",
    "port": 3306,
    "database": "<db-name>"
}
```


<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- USAGE EXAMPLES -->
## Usage

There are stored procedures for each CRUD operation:
* Create: `createNewUser`
* Read: `getUsers` and `getUserByID`
* Update: `updateUser`
* Delete: `deleteUser`

and they are called from API:

* Create:
    * `<hostname>:<port>/users/create` (POST Method)
* Read:
    * `<hostname>:<port>/users/<_id>` (GET Method)
    * `<hostname>:<port>/users` (GET Method)
* Delete:
    * `<hostname>:<port>/users/<_id>` (DELETE Method)
* Update:
    * `<hostname>:<port>/users/<_id>` (PUT Method)

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/ErickOF/CRUD-Flask-SQLServer/issues) for a full list of proposed features (and known issues).

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your feature branch (`git checkout -b feature-<feature-name>`)
3. Commit your changes (`git commit -m 'Add some <feautre>'`)
4. Push to the branch (`git push origin feature-<feature-name>`)
5. Open a pull request

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- CONTACT -->
## Contact

Erick Andrés Obregón Fonseca - <erickobregonf@gmail.com>

Project Link: [https://github.com/ErickOF/CRUD-Flask-SQLServer](https://github.com/ErickOF/CRUD-Flask-SQLServer)

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)

<p align="right">
    <a href="#readme-top">back to top</a>
</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ErickOF/CRUD-Flask-SQLServer.svg?style=for-the-badge
[contributors-url]: https://github.com/ErickOF/CRUD-Flask-SQLServer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ErickOF/CRUD-Flask-SQLServer.svg?style=for-the-badge
[forks-url]: https://github.com/ErickOF/CRUD-Flask-SQLServer/network/members
[stars-shield]: https://img.shields.io/github/stars/ErickOF/CRUD-Flask-SQLServer.svg?style=for-the-badge
[stars-url]: https://github.com/ErickOF/CRUD-Flask-SQLServer/stargazers
[issues-shield]: https://img.shields.io/github/issues/ErickOF/CRUD-Flask-SQLServer.svg?style=for-the-badge
[issues-url]: https://github.com/ErickOF/CRUD-Flask-SQLServer/issues
[license-shield]: https://img.shields.io/github/license/ErickOF/CRUD-Flask-SQLServer.svg?style=for-the-badge
[license-url]: https://github.com/ErickOF/CRUD-Flask-SQLServer/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/erickandresobregonf
[Python3]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[PyFlask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[MSSQLServer]: https://img.shields.io/badge/Microsoft_SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white
[SQLServer-url]: https://www.microsoft.com/en-us/sql-server/sql-server-2022
