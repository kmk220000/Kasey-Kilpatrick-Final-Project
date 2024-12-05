# An Interactive Stream Schedule

## Demo
Demo Video: [Link](https://utdallas.box.com/s/kfwtt3i8yl4apanwd3krgozbo1yzdf8n)

## GitHub Repository
GitHub Repo: [Link](https://github.com/kmk220000/Kasey-Kilpatrick-Final-Project.git)

### Disclaimer
You MUST install the fonts in the `themes/cyberpunk space/fonts` folders to your computer before using the program for it to display the custom fonts. Otherwise, it will just use Arial font. (To install: Open font file > click `Install` in the top left corner)

## Description

My PFDA Final Project is an Interactive Stream Schedule for livestreamers to post on their social media every week with the games they plan to play for that week. I wanted to make this because I have been meaning to create a schedule for myself, and I thought that if I made it interactive and simple and gave it different themes, maybe I could sell the application to other streamers who are just starting out for a much smaller price than it would be to commission one like this. I coded it so that if I make other themes in the future, as long as the files are named and ordered correctly, the rest of the code should work properly. Nothing related to each theme is hard-coded into the program.

There is a very specific hierarchy of files in my repository. Of course, there is this file, the `proposal` file, and the `requirements` file. In the `src` folder, there is the `project` file that contains all code and there is a `themes` folder. The `themes` folder currently only has the `cyberpunk space` folder, but it will have more in the future. In that theme, there are two folders: `days` and `fonts`. The `days` folder has `OFF` and `ON` folders containing the images needed for the light mode (stream day) and dark mode (no stream day) images necessary for the program. The `fonts` folder has the fonts needed for that theme. **Unfortunately, you currently need to install each font to your computer for it to work properly, but I plan to fix that in the future.** The `cyberpunk space base` image can also be found in that theme's folder. This is the background image that the days and buttons are placed on top of. This file naming convention is very important because every theme needs to be named like this, except `cyberpunk space` would be replaced with the new theme name.

I made the theme's design in Adobe Illustrator, and for any future themes, I would just need to edit that Illustrator file to fit the new theme before I upload it to the application. The right side of the design is transparent so that art or other images can be uploaded under the theme, fitting the shape of the design. There are also spaces for other text that I plan to add in the future.

To improve this project, I would like to add several new features. I want the user to be able to add `Week of xx/xx-xx/xx`, custom hashtags, social media handles with logos of the platform, their own custom logo, credit to the person who made the art they uploaded, and a description of the stream if they want to. I also want to make it so that the time is converted into the other two timezones, the `Edit Games` window gives you errors if you don't put in correct data, and days with no stream have a message that can be customized. Lastly, I want the GUI itself to be a lot more appealing to the user instead of the boring default designs, so I will be designing my own GUI to upload to the program. I will make this project into an actual `.exe` application for people to own on their computer, and any issues with installing fonts and third party modules will hopefully be fixed.

Creating this project was very fun but challenging, as I had to teach myself  `tkinter` and many other things. It got frustrating at times and I'm a bit sad I wasn't able to implement some of the other features, but I think my project is far above the Minimum Viable Outcome that I set for myself on my proposal, so I'm happy with it! If I can implement those other features, even if the program still isn't good enough to sell, I will have reached my Ideal Outcome on the proposal and I will be able to use this to create my own schedules!