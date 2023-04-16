<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache 2.0 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/capcom6/api-registry">
    <img src="assets/logo.svg" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">API Registry</h3>

  <p align="center">
    API registry service is a Python-based open source tool for managing and browsing OpenAPI YAML specifications and Swagger UI documentation.
    <br />
    <!-- <a href="https://github.com/capcom6/api-registry"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/capcom6/api-registry">View Demo</a> -->
    ·
    <a href="https://github.com/capcom6/api-registry/issues">Report Bug</a>
    ·
    <a href="https://github.com/capcom6/api-registry/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
- [About The Project](#about-the-project)
- [Built with](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [How it works](#how-it-works)
  - [Configuration](#configuration)
  - [Security](#security)
  - [Release notes](#release-notes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://github.com/capcom6/api-registry) -->

This open source project is a simple API registry service created with Python. It was built to provide an easy and convenient way to manage and browse OpenAPI YAML specifications and Swagger UI documentation.

The project is currently in its MVP (minimum viable product) stage, and is designed to be a basic starting point for building a more robust API registry system. It allows users to upload zip-archive files containing OpenAPI YAML specifications, and provides a simple user interface for browsing and accessing available APIs.

The project was inspired by the need for a lightweight and easy-to-use API registry service that could be easily customized and extended. It was built with Python and uses the FastAPI web framework, and Swagger UI for documentation.

We welcome contributions from the community to help improve and expand the functionality of the project. Please feel free to submit issues, pull requests, or feature requests on the project's GitHub repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Built with

* [![FastAPI](https://img.shields.io/badge/fastapi-0.95.1-blue.svg)](https://fastapi.tiangolo.com/)
* [![Jinja2](https://img.shields.io/badge/jinja2-3.1.2-blue.svg)](https://palletsprojects.com/p/jinja/)  
* [![Uvicorn](https://img.shields.io/badge/uvicorn-0.21.1-blue.svg)](https://www.uvicorn.org/)
* [![Swagger UI](https://img.shields.io/badge/swagger--ui-4.18.2-orange.svg)](https://swagger.io/tools/swagger-ui/)  
<!-- * [Vue.js](https://vuejs.org/) - A progressive, incrementally-adoptable JavaScript framework for building user interfaces.
  ![Vue.js version](https://img.shields.io/badge/vue.js-2.6.14-green.svg) -->
<!-- * [PyYAML](https://pyyaml.org/) - A YAML parser and emitter for Python.
  ![PyYAML version](https://img.shields.io/badge/pyyaml-6.0-blue.svg) -->
<!-- * [Click](https://click.palletsprojects.com/en/8.0.x/) - A Python package for creating command line interfaces.
  ![Click version](https://img.shields.io/badge/click-8.1.3-blue.svg) -->
<!-- * [python-dotenv](https://github.com/theskumar/python-dotenv) - A Python package that allows you to use variables defined in a .env file in your Python projects.
  ![python-dotenv version](https://img.shields.io/badge/python--dotenv-1.0.0-blue.svg) -->
<!-- * [python-multipart](https://github.com/andrew-d/python-multipart) - A Python module for handling HTTP multipart/form-data requests.
  ![python-multipart version](https://img.shields.io/badge/python--multipart-0.0.6-blue.svg) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before running the app, you should have the following installed on your system:

* Docker - You can download and install Docker from [here](https://www.docker.com/get-started).

### Installation

To run the app in a Docker container follow these steps:

1. Open a terminal or command prompt.

2. Pull the latest version of the `capcom6/api-registry` Docker image:

   ```
   docker pull capcom6/api-registry:latest
   ```

3. Start the app in a Docker container, exposing port 8000:

   ```
   docker run -p 8000:8000 capcom6/api-registry:latest
   ```

4. Open a web browser and navigate to `http://localhost:8000` to access the app.

That's it! You should now be able to access the app in your web browser at `http://localhost:8000`. If you encounter any issues, please refer to the project's documentation or open an issue on the project's GitHub repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### How it works

When you start the server, it listens for incoming requests on port 8000 by default. When you upload a zip-archive containing OpenAPI YAML specifications, the service expects the zip-archive to contain a folder for each project, with the OpenAPI spec in YAML format located in the project folder. The service extracts the files and stores them in a local directory. The service then reads the contents of the OpenAPI YAML files and generates Swagger UI documentation for each API.

The user interface provides a list of available APIs, and allows you to view the Swagger UI documentation for each API by clicking on the API name.

### Configuration

This app is designed to work out of the box without any additional configuration.

### Security

The API registry service does not include any built-in authorization or authentication mechanism. To enhance security, it is recommended to use an external service or tool, such as Nginx, to provide basic authentication and restrict access to the application. Alternatively, deploying the application in a private network can provide an additional layer of security and help prevent unauthorized access from external sources.

To help users get started with basic authentication using Nginx, a sample Docker Compose file is [provided](deployments/docker-compose.yml). This file includes a configuration for an Nginx reverse proxy that provides basic authentication for the API registry service. To use this configuration, you will need to modify the [`htpasswd`](deployments/nginx/.htpasswd) file to include your own username and password.

Note that this configuration is only intended as a starting point, and may need to be customized or extended to meet the specific security needs of your application. It is recommended to consult with a security expert or follow industry best practices when implementing security measures for your application.

### Release notes

* Uploading a new zip-archive will overwrite any previously uploaded API specifications

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

* Parsing metadata from OpenAPI specs and displaying it in the user interface.
* Adding support for simple search functionality based on metadata fields.
* Enhancing support for uploading and managing multiple versions of an API.
* Integrating with other API management tools and services to provide a more comprehensive solution for API management.
* Improving the user interface and user experience, including customization options and branding support.

We welcome feedback and suggestions from the community to help shape the future roadmap of the API registry service. Please feel free to share your thoughts or ideas by opening issues or submitting pull requests on the project's GitHub repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache-2.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/capcom6/api-registry](https://github.com/capcom6/api-registry)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We would like to thank the following individuals and organizations for their contribution to the development of the API registry service:

* The creators and maintainers of FastAPI, which form the backbone of the API registry service.
* The contributors to the OpenAPI Specification, which provides a common standard for describing RESTful APIs.
* The developers of the Swagger UI library, which provides a user-friendly interface for browsing and testing API endpoints.

Finally, we would like to thank our users and contributors for their valuable feedback and support. We are committed to continuing to improve and extend the API registry service, and look forward to working with the community to make it a more comprehensive and powerful tool for API management.

<p align="right">(<a href="#readme-top">back to top</a>)</p> 



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/capcom6/api-registry.svg?style=for-the-badge
[contributors-url]: https://github.com/capcom6/api-registry/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/capcom6/api-registry.svg?style=for-the-badge
[forks-url]: https://github.com/capcom6/api-registry/network/members
[stars-shield]: https://img.shields.io/github/stars/capcom6/api-registry.svg?style=for-the-badge
[stars-url]: https://github.com/capcom6/api-registry/stargazers
[issues-shield]: https://img.shields.io/github/issues/capcom6/api-registry.svg?style=for-the-badge
[issues-url]: https://github.com/capcom6/api-registry/issues
[license-shield]: https://img.shields.io/github/license/capcom6/api-registry.svg?style=for-the-badge
[license-url]: https://github.com/capcom6/api-registry/blob/master/LICENSE.txt
[product-screenshot]: https://github.com/capcom6/api-registry/raw/master/assets/ui.png
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Redis]: https://img.shields.io/badge/Redis-000000?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
