Port of Witch Hunt's official Umineko translation to the [Umineko Project](https://umineko-project.org) engine.

---

# What is this?

*Umineko no Naku Koro ni* is a visual novel released by 07th-Expansion. The game was originally released only in Japan on PC and PS3, with the PS3 release being significantly superior (better art, higher quality music, voice-acting, lip sync, animations, and a whole boatload of other improvements).

The PC release was later translated to English by a group called *Witch Hunt*. After a while, their translation was made official, received extra polish, and got published on Steam, but, sadly, it had none of the enhancements of the PS3 version.

However, there is a  fanmade port of the PS3 version to PC called *Umineko Project*. Because it was created before the official release, this port uses a fan translation created based partially on the older, unofficial Witch Hunt translation, partially on the official manga translation, and heavy editing done by the Umineko Project team.

However, some people prefer Witch Hunt's new official translation. This project exists to provide a language pack for Umineko Project that allows the use of the official translation combined with all of the improvements and enhancmenets of the PS3 version and the Umineko Project port.

## Do I need this?

If you have to ask, the answer is \<no\>, you don't. The fact that the Witch Hunt translation has the "official" status doesn't necessarily mean it's superior in any way. Both the Umineko Project and the Witch Hunt translations are perfectly readable, gramatically correct and clean English. 

The two teams, however, made several significantly different translation choices, and some of these choices such as character catchphrases and especially memorable lines stuck with fans one way or the other. This has led to a situation where some people will recommend against Umineko Project simply because it uses an unofficial translation, and that's *no goddamn good at all*. 

While I, personally, prefer the Umineko Project translation, I have created this project to resolve this *useless* conflict. If you simply *love* the official translation and can't enjoy Umineko Project without it, but you still *want* the cool PS3 stuff, this is for you. Otherwise, you should probably skip this altogether.

## How do I use this?

For one, please note that ***this is currently a work in progress and not finished*** -- not all chapters are translated yet, and there might be bugs and crashes. You can grab the `Witch-Hunt.file` from the [latest release](../../releases/latest) and put it in your Umineko Project folder, then select the language in the settings, if you want to help test it. If you want a stable and complete experience, please check back some time later when the whole thing is done.

Current progress is indicated below. While I try my best to update this project consistently, I cannot guarantee a specific pace of updates. Also, due to personal reasons, episodes may be released out of order. Note that "Complete" here merely means that the translation has been completely ported. It does not guarantee the episode being bug-free.

|Episode|Status|
|-|-|
|Episode 1: Legend of the Golden Witch|Complete|
|Episode 2: Turn of the Golden Witch|Complete|
|Episode 3: Banquet of the Golden Witch|Up to chapter 6|
|Episode 4: Alliance of the Golden Witch|Not started|
|Episode 5: End of the Golden Witch|Not started|
|Episode 6: Dawn of the Golden Witch|Complete|
|Episode 7: Requiem of the Golden Witch|Complete|
|Episode 8: Twilight of the Golden Witch|Not started|

---

# Notes on project structure for contributors

- The `story` folder is what you're interested in. Anything outside of it is irrelevant to this project. However, if you would like to be credited, please add yourself to `script/wh/credits.txt` under the existing contributors in the "Witch Hunt Translation Backport" section.
- `story/epX/en/` contains the original Umineko Project translation. Do not modify anything here.
- `story/epX/wh/` contains a copy of that translation that's being replaced with the WH translation as I progress through the project (see commits to know where I'm at)
- `story/rest-rondo.txt` and `story/rest-nocturne.txt` are an auto-generated version of the scripts. This won't run by itself and needs manual editing. The parts that are in these files haven't been touched by me yet.

## Suggested workflow

1. Cut a chunk of text out of `rest-X.txt` that corresponds to a chapter (one of the story/epX/wh/umiX_X.txt files that haven't been finished yet).
2. Paste that chunk into the corresponding file, replacing everything.
3. Commit and push those changes. This will let other developers know you've taken a chunk and are working on it.
4. Open the file you've just changed in an editor with good diff support (personally, I use VS Code).
5. Remove any suspicious translations and adjust lines to fit. The line numbers between the original translation and the new one *must* match, or else the wrong lines will be "translated". You may need to split/join some of the lines in the WH translation, but try to avoid taking any liberties while doing so such as adding extra words in the joined sentence.
6. Once you are finished with the episode, check your script for anything that matches the regex `@|~|!\w|#`. These are ponscripter control characters, and you may accidently end up leaving some of them in. Fix up the matches that aren't actual dialogue. Running `script_fixup.py epX` may help you here.
7. Once you are finished with the episode, run the "spacing fix". Essentially, make sure that every line has *no* spaces at the beginning of it, and a single space at the end (inside the backticks, not outside of them). `script_fixup.py` will handle this for you as well, if you choose to use it.

## Automated build process

This repository is set up to produce a pre-release on every push. If you can push to this repo, you can just wait for the build to finish after the push and download it from [here](../../releases/latest). This page is where testers should check for latest versions of the script as well.

## Manual build process
1. Install PHP somewhere on your PATH. No extra modules are required, just the default configuration is fine.
2. `cd` to the project root.
3. `mkdir out; php update-manager/update-manager.php dscript out/wh.txt . wh`
4. Check `out/wh.txt` for anything suspicious. You probably won't find anything because the script is too complicated for human consumption.
5. `php update-manager/update-manager.php script out/wh.txt "out/Witch-Hunt.file" 8`
6. Copy the generated `.file` file to the Umineko Project directory and choose "Witch-Hunt" as your language in the game settings.
