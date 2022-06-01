[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7950652&assignment_repo_type=AssignmentRepo)
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
`github_username: SnowSword1010`, `repo: dyte-vit-2022-SnowSword1010`, `twitter_handle: @jmayank2001`, `linkedin_username: mayank-1010`, `email_client: mayank.jain2019a@vitstudent.ac.in`, `email: jmayank2001@gmail.com`, `project_title: Dyte-CLI-App`, `project_description: A Cli tool for managing release process`

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Given a list of Github repositories, assuming all of them are node js projects with a package.json and package-lock.json in the root, and the name and version of a dependency, we want to give the current version of that dependency and tell if the version is greater than or equal to the version specified or not.

Secondly, for all the repositories that have the version lower than the one specified, if passed as additional param, let’s say `-update`, it should create a PR updating the version.

### Prerequisites

* Have python installed

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/dyte-vit-2022-SnowSword1010.git
   ```
2. Create virtual environment
  ```sh
    python3 -m venv venv
  ```
3. Activate virtual environment
  ```sh
  source venv/bin/activate
  ```
4. Install requirements
   ```sh
   pip3 install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
```sh
  python3 main.py [-h] [-update] --i csv_filename --d dependency_name
```

h flag (optional): help
update flag (optional): sets the update flag to true which comes in required when we want to update the dependency version to the one specified by the user.
NOTE: Although the project demanded the creation of pull requests, I could not implement the entire thing due to time constraints. I cloned the repo and made changes into it locally instead.

--i flag (mandatory): used to specify the csv file name where data would be read from. --i examples/example1.csv could be used to test the utility.
--d flag (mandatory): used to specify the dependency name. --d axios@0.23.4 can be used to test the utility

Sample usage command:
```sh
  python3 main.py -update --i examples/example1.csv --d axios@0.23.4
```

<!-- CONTACT -->
## Contact

Your Name - Mayank Jain @SnowSword1010 - mayank.jain2019a@vitstudent.ac.in

Project Link: [https://github.com/dyte-submissions/dyte-vit-2022-SnowSword1010](https://github.com/dyte-submissions/dyte-vit-2022-SnowSword1010)

<p align="right">(<a href="#top">back to top</a>)</p>


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
