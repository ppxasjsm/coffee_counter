## Getting a touch screen app in python working


This is an attempt to build a touch screen enabled python app to count coffee consumption in the chemistry department using a raspberry pi


### 1. Installing [kivy](kivy.org)   
After some very basic googling kivy seems to be the thing to use to build a responsive python touchscreen app. 

`conda install kivy -c conda-forge`

Next running the test hello world up from the website:

```python
import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
```


This resulted in an initial error:

```
python -d main.py 
[INFO   ] [Logger      ] Record log in /Users/toni_brain/.kivy/logs/kivy_19-12-29_5.txt
[INFO   ] [Kivy        ] v1.11.1
[INFO   ] [Kivy        ] Installed at "/Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.7.6 | packaged by conda-forge | (default, Dec 26 2019, 23:46:52) 
[Clang 9.0.0 (tags/RELEASE_900/final)]
[INFO   ] [Python      ] Interpreter at "/Users/toni_brain/miniconda3/envs/coffee/bin/python"
[INFO   ] [Factory     ] 184 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_pil, img_gif (img_pygame, img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: pil(['text_pygame'] ignored)
[CRITICAL] [Window      ] Unable to find any valuable Window provider. Please enable debug logging (e.g. add -d if running from the command line, or change the log level in the config) and re-run your app to identify potential causes
pygame - ModuleNotFoundError: No module named 'pygame'
  File "/Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/core/__init__.py", line 63, in core_select_lib
    fromlist=[modulename], level=0)
  File "/Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/core/window/window_pygame.py", line 13, in <module>
    import pygame

[CRITICAL] [App         ] Unable to get a Window, abort.

```

I guess we are in dependency heaven. Let's install pygame, but using pip of course...because why  not. 

```
pip install pygame 
Collecting pygame
  Downloading https://files.pythonhosted.org/packages/32/37/453bbb62f90feff2a2b75fc739b674319f5f6a8789d5d21c6d2d7d42face/pygame-1.9.6-cp37-cp37m-macosx_10_11_intel.whl (4.9MB)
     |████████████████████████████████| 4.9MB 1.4MB/s 
Installing collected packages: pygame
Successfully installed pygame-1.9.6

```

Starting the first app again now works successfully:

```
python -d main.py 
[INFO   ] [Logger      ] Record log in /Users/toni_brain/.kivy/logs/kivy_19-12-29_6.txt
[INFO   ] [Kivy        ] v1.11.1
[INFO   ] [Kivy        ] Installed at "/Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.7.6 | packaged by conda-forge | (default, Dec 26 2019, 23:46:52) 
[Clang 9.0.0 (tags/RELEASE_900/final)]
[INFO   ] [Python      ] Interpreter at "/Users/toni_brain/miniconda3/envs/coffee/bin/python"
[INFO   ] [Factory     ] 184 symbols loaded
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_pygame, img_pil, img_gif (img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: pygame
[INFO   ] [Window      ] Provider: pygame
[WARNING] [Deprecated  ] Pygame has been deprecated and will be removed after 1.11.0: Call to deprecated function __init__ in /Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/core/window/window_pygame.py line 42.Called from /Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/core/__init__.py line 71 by core_select_lib().
[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
[INFO   ] [GL          ] Backend used <gl>
[INFO   ] [GL          ] OpenGL version <b'2.1 INTEL-10.36.25'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel Inc.'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel(R) Iris(TM) Graphics 6100'>
[INFO   ] [GL          ] OpenGL parsed version: 2, 1
[INFO   ] [GL          ] Shading version <b'1.20'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <16>
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[WARNING] [Deprecated  ] Pygame has been deprecated and will be removed after 1.11.0: Call to deprecated function __init__ in /Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/core/text/text_pygame.py line 36.Called from /Users/toni_brain/miniconda3/envs/coffee/lib/python3.7/site-packages/kivy/uix/label.py line 349 by _create_label().
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Leaving application in progress...

```

### 2. Following the pong tutorial.

To get familiar with kivy I decided to follow the tutorial online [here](https://kivy.org/doc/stable/tutorials/pong.html)