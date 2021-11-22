<h3 align="center">foamTEX</h3>

  <p align="center">
    An open source utility for creating publication quality figures in LaTex, with scripts generated from OpenFOAM data files.
    <br />
    <a href="https://github.com/LeoTurnell-Ritson/foamTEX"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LeoTurnell-Ritson/foamTEX/issues">Report Bug</a>
    ·
    <a href="https://github.com/LeoTurnell-Ritson/foamTEX/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

foamTex is a python biased utility for generating LaTeX scripts from raw OpenFOAM data files. This project is currently in early development.

For more information about OpenFOAM or LateX:


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Installation is supper easy and the main foamTex.py source file can be run as an executable out of the box without any prerequisites (other than python3) Note: there is not requirement for either LateX or OpenFOAM. If you wish to run foamTEX as an executable follow the instructions bellow (written for bash Unix shell). 

### Prerequisites

* pyinstaller if you wish to run foamTEX as an executable (see https://pypi.org/project/pyinstaller/)
  ```sh
  pip install pyinstaller
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/LeoTurnell-Ritson/foamTEX.git
   ```

2. If you wish to run foamTEX as a pre-compiled executable: Grant execution permissions to Allmake file
   ```sh
   chmod u+x Allmake
   ```
3. Run Allmake
   ```sh
   ./Allmake
   ```
4. Add foamTEX to path
   ```sh
   export PATH=$PATH:$(pwd)/dist
   ``` 
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/LeoTurnell-Ritson/foamTEX/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

 l.turnell.ritson@gamil.com

Project Link: [https://github.com/LeoTurnell-Ritson/foamTEX](https://github.com/LeoTurnell-Ritson/foamTEX)

<p align="right">(<a href="#top">back to top</a>)</p>