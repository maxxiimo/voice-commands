# Dragonfly Voice Command Modules

I'm sharing this list of voice command modules to help others overcome RSI/hand use issues. I developed something called Trigger Finger from keyboard use, and tendinitis in my wrists from mouse use. If I don't use voice commands by half day my hands will be aching. Not fun.

## My Set Up

### Software
- Windows 7 – When I started doing this Dragon only work with Windows. (I recommend using Cmder, or an Ubuntu installation on VMware or similar and from their Putty in, or terminal into a VPS like DigitalOcean.&#8224;)
- Dragon NaturallySpeaking 14
- Dragonfly
- SpeechStart Commands
- Sublime 3
- Command Line

### Hardware
- Wacom Cintiq or Intuos for pen mousing
- Table Mike 3-in-1
- Wireless trackball (remove the trackball and use the device for clicking/scrolling only)

## How to Use

I use the commands in these modules quite a bit in my day to day programming. Some are more complete than others – for example Ruby vs. Python (as of this writing I'm just starting to learn Python), and overall the library grows as I run into things that are needed or I find better ways to do things.

Basically the way to think about calling up or naming macros is to use the first thing that comes to your mind, because chances are that's what it's going to be. Here's a practical example. If I wanted to create an HTML table the best word cue for that would probably be "HTML table". And so it is...

"**HTML table**" produces `<table>` ([1](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L157))

"**HTML table with class**" produces `<table class="">` and places your cursor between the quotes. ([2](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L158))

"**close table**" produces `</table>` ([3](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L228))

"**HTML table complete**" gives you all the essentials of a basic table. ([4](https://github.com/maxxiimo/voice-commands/blob/master/_html.py#L159))

BTW on occasion I add second and third best word combination candidates as well. I also namespace by language, application, or major function. Sometimes the namespace is optional – for example when [HTML], the obvious namespace for markup related commands, is enclosed by brackets saying the word is optional.

NOTE: In the "**HTML table complete**" case above none of the indentations have been added to the output code yet. This is because a lot of these macros were imported from Dragon NaturallySpeaking's built-in command macro system, which has no export to [plaintext/any other application] feature so I had to do some labor-intensive manual trickery to get it over...and it took forever. You may find other instances of things like this, but not too many.

## Why This Way?

First Dragon NaturallySpeaking is is a lot harder to customize, organize, and program than Dragonfly. Dragonfly is just Python. But really, why this method of creating word cues?

I have found that for me the hardest thing about coding with your voice is writing all of the non-English words, symbols, and also controlling the capitalization and spacing between things. It's super time-consuming with out voice macros. Take for example the following:

bool, var, elsif

CamelCase

method()

```
<%= link_to '', root_path, title: '' %>
```

```javascript
function () {
  return
}
```

There is no really efficient way to just use your voice to get these things, and these are only just the tip of the iceberg.

So rather than create weird sounds to make things happen – in the way I need them to happen, I decided to create a massive library of word cues. This way just works out better for me and my brain. Plus as I learn new languages, frameworks, applications, through this effort I get a super useful coding cheat sheet for free. For example: [Git](https://github.com/maxxiimo/voice-commands/blob/master/_git.py), [Linux](https://github.com/maxxiimo/voice-commands/blob/master/_linux.py)

## Contribute

So there it is. If you have some really good ideas to make things better, shoot me an email or submit a pull request and if it fits the mold I will add your work.

&#8224; If you decide to try DigitalOcean go ahead and add some credits to my account by using my referral link:

[DigitalOcean](http://pages.news.digitalocean.com/dcn/AyKQ30vur1Nt8H30LIWxk-j5xHmafGnoECQwn1ooO745F9qnHNMIeEAbzmTgNsm0IxJY3CxZMyxTjev35FX3Tg==/Y0VpP0qXG00gR0236IE0jD4)
