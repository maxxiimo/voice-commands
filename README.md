# Dragonfly Voice Command Modules

I'm sharing this list of voice command modules to help others overcome RSI/hand use issues. I developed something called Trigger Finger from keyboard use, and tendinitis in my wrists from mouse use. If I don't use voice commands by half day my hands will be aching. Not fun.

## My Set Up

### Software
- Windows 7 – When I started doing this Dragon only work with Windows. (I recommend using Cmder, or an Ubuntu installation on VMware or similar and from their Putty in, or terminal into a VPS like DigitalOcean.*)
- Dragon NaturallySpeaking 14
- Dragonfly
- Sublime 3

### Hardware
- Wacom Cintiq or Intuos for pen mousing
- Table Mike 3-in-1
- Wireless trackball (remove the trackball and use the device for clicking/scrolling only)

## How to Use

I use the commands in these modules quite a bit in my day to day programming. Some are more complete than others – for example Ruby vs. Python (as of this writing I'm just starting to learn Python), and overall the library grows as I run into things that are needed or I find better ways to do things.

Basically the way to think about calling up and naming macros is use the first thing that comes to mind. On occasion I add second and third candidates as well. I also namespace by language, application, or major function. Sometimes the namespace is optional. Here's a practical example. If I wanted to create an HTML table the best word cue for that would probably be "HTML table". And so it is...

"**HTML table**" produces `<table>` [1](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L157)

"**HTML table with class**" produces `<table class="">` and places your cursor between the quotes. [2](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L158)
"**close table**" produces `</table>` [3](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L228)
"**HTML table complete**" gives you all the essentials of a basic table. [4](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L159)

BTW when [HTML] is enclosed by brackets saying the word is optional.

NOTE: In the later case none of the indentations have been added yet. This is because a lot of these macros were imported from Dragon NaturallySpeaking's built-in command macro system, which is a lot harder to customize, organize, program, and has no export to [plaintext/any other application] feature so I had to do some labor-intensive manual trickery to get it over and it took forever.

## Why This Way?

The hardest thing about coding with your voice is writing all of the non-English words and symbols and controlling spacing between things...

bool, var, elsif

CamelCase

method()

`<%= link_to '', root_path, title: '' %>`

```javascript
function () {
  return
}
```

So rather than create weird sounds to make things happen in the way I need them to happen, I decided to create a massive library of word cues. This way just works better for me and my brain. Plus through this effort I end up creating a super useful coding cheat sheet as I learn the language. For example: [Git][https://github.com/maxxiimo/voice-commands/blob/master/_git.py], [Linux](https://github.com/maxxiimo/voice-commands/blob/master/_linux.py)

## Contribute

So there it is, if you have some really good ideas to make things better submit a pull request and if it fits the mold I will add your work.

* If you decide to try DigitalOcean earn me some credit by using my referral link - http://pages.news.digitalocean.com/dcn/AyKQ30vur1Nt8H30LIWxk-j5xHmafGnoECQwn1ooO745F9qnHNMIeEAbzmTgNsm0IxJY3CxZMyxTjev35FX3Tg==/Y0VpP0qXG00gR0236IE0jD4
