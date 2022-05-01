<!--
*** Template source: https://github.com/othneildrew/Best-README-Template
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** Using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPL v3.0 License][license-shield]][license-url]
<!--
[![LinkedIn][linkedin-shield]][linkedin-url]
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h3 align="center">MiSCA ID Sticker Generator</h3>

  <p align="center">
    Short scripts to turn your MiSCA roster report into a sheet of scannable ID codes ready to print
    <br />
    <a href="https://github.com/akorinda/MiSCA-ID-Sticker-Generator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/akorinda/MiSCA-ID-Sticker-Generator">View Demo</a>
    · -->
    <a href="https://github.com/akorinda/MiSCA-ID-Sticker-Generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/akorinda/MiSCA-ID-Sticker-Generator/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

As you get more and more members on your team checking everyone in and out begins to take significant time. The idea here is to create scannable codes, currently QR only, which can be printed on sticker sheets and affixed to an athlete's equipment (i.e. helmet). 

Why?
* Less time checking in/out means more time to ride!
* Increased safety through increased tracking accuracy
* Less chance for crossing the wrong name off on a papersheet
* Can be integrated with a spreadsheet to track who is out riding and who has returned
* Digital tracking can provide data reports and detail useful in grant applications 



### Built With

* [Python 3.10.4](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

Option 1) Download and run "Create Rider QR.exe" on Windows
Option 2) Run a local copy of the script following these steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3 or newer (original development on 3.10)  [Download the Latest Python versions](https://www.python.org/downloads/)
* [Python PIP Requirements](https://github.com/akorinda/MiSCA-ID-Sticker-Generator/blob/master/requirements.txt)
  

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/akorinda/MiSCA-ID-Sticker-Generator.git
   ```
2. Install Python packages
   ```sh
   py -m pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage

Executing the two Python scripts will create sheet of codes which a standard 2D scanner can read to enter rider information into an electronic record. These can then be printed on Avery 1"x1" sticker label sheets and distributed to the athletes. Only those with the role "Rider" will be recognized.

__Suggested use case:__ Place a sticker on each altheles' equipment and scan it as they come and leave practice. The scanned data can populate a spreadsheet to track attendance and provide an electronic record that everyone returned from the ride. If requested I can create a sanitized version of what MMBC used in 2021 and link it here. Create an issue if you are interested.


__Work Flow:__
1. Download your rider roster. Important columns are a key (unique identifier), first name, and last name
2. Convert the roster to an Excel format (*.xls or *.xlsx) if it isn't already
3. Run "Create Rider QR.exe or "Create-Images.py"
4. Follow the instructions presented in the text window
5. Print the docx file on Avery Presta 94103 1"x1" sticker labels


__Sticker Considerations:__<br>
The code spacing is currently fixed and only validated for Avery 1"x1" sticker label sheets. It is not on the roadmap to make more templates available but contributions are welcome and appreciated. We choose Avery 94103 for their removable yet water resistant adhesive. These came off cleanly from the athlete's equipment at the end of the season.


__Placement Considerations:__<br>
At Midland Mountain Bike Crew (MMBC) we found helmets worked best. We tried bike frames but the curve was too much for our cheap 2D scanner. With a QR code lighting did matter and it was possible for the code to be too light but shading with a hand resolved the issue. Similarly, putting the helmet under a brim kept the code shaded and protected it from rain; however, the helmet had to be removed from the rider's head to scan. In the future we want to try a 1D barcode to see if the laser scan is less sensitive to light levels.


__Are Duplicants Needed?__<br>
The program will ask you how many copies of each sticker you want. We started the season with 3 stickers for each rider. In 2021, out of 64 riders, only one went through all three. We used an inkjet printer and the stickers were succeptible to smugging from rain; two stickers were replaced for water damage. After 12 weeks one sticker would not scan because it had become too faded from sun exposure.


__Barcode Scanner Requirements__<br>
QR codes require a 2D capable barcode scanner. MMBC used a basic [wired 1D 2D barcode scanner](https://www.amazon.com/Evnvn-Scanning-Auto-Sensing-Warehouse-Bookstore/dp/B08D98XQV4/ref=asc_df_B08D98XQV4/?tag=hyprod-20&linkCode=df0&hvadid=475716043645&hvpos=&hvnetw=g&hvrand=562984632817239689&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9017117&hvtargid=pla-939626915235&psc=1) in 2021 with success. If power isn't a concern I'd suggest trying a bluetooth one. We found the cord either got in the way or athletes didn't come close enough without prompting. It is not recommended to scan with a barcode scanner directly to a mobile phone. Scanners work like typeboards and phones aren't desired for such quick input. It is possible to use most smartphone cameras as barcode scanners.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/akorinda/MiSCA-ID-Sticker-Generator/issues) for a list of proposed features (and known issues).

Overview:
* Increase user input/output flexibility
* Increase code flexibility (QR, Code 128, etc)
* Select specific athletes
* Have a graphical rather than text interface



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GNU GPL v3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Andy Korinda - [akorinda](https://github.com/akorinda)

Project Link: [https://github.com/akorinda/MiSCA-ID-Sticker-Generator](https://github.com/akorinda/MiSCA-ID-Sticker-Generator)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/akorinda/MiSCA-ID-Sticker-Generator.svg?style=for-the-badge
[contributors-url]: https://github.com/akorinda/MiSCA-ID-Sticker-Generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/akorinda/MiSCA-ID-Sticker-Generator.svg?style=for-the-badge
[forks-url]: https://github.com/akorinda/MiSCA-ID-Sticker-Generator/network/members
[stars-shield]: https://img.shields.io/github/stars/akorinda/MiSCA-ID-Sticker-Generator.svg?style=for-the-badge
[stars-url]: https://github.com/akorinda/MiSCA-ID-Sticker-Generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/akorinda/MiSCA-ID-Sticker-Generator.svg?style=for-the-badge
[issues-url]: https://github.com/akorinda/MiSCA-ID-Sticker-Generator/issues
[license-shield]: https://img.shields.io/github/license/akorinda/MiSCA-ID-Sticker-Generator.svg?style=for-the-badge
[license-url]: https://github.com/akorinda/MiSCA-ID-Sticker-Generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
