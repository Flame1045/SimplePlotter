# Intro
This is a easy repo to help you plot like a genius!  
  
  
![Like This](https://github.com/Flame1045/SimplePlotter/blob/main/docs/Figure_1.png)

# Requirements
```
python
matplotlib
argparse
numpy
``` 

# How to Use
  First, clone this repo
  ```
  git clone https://github.com/Flame1045/SimplePlotter.git
  ```
  
  Then, install the requirements package
  ```
  pip install -r requirements.txt
  ```
  
  And you got the enviroment ready!   
  To plot, simply type in command to run this program
  ```
  python plot.py --exper_dir "./test1"
  ```
  And there's your plot.  
  
  We'll see how to alter config file to plot your desire plot in next section.  
  
# Config
  There are two types of config.  
 * The [CONFIG.yaml](https://github.com/Flame1045/SimplePlotter/blob/main/CONFIG.yaml) 
     * This config is to set plot Title, X and Y axis name, Legend position. (Note that please d'not change "CONFIG.yaml" name to prevent can't find file error)
     * Param explain : 
        * Title : Can be any string 
        * X and Y axis name : Can be any string 
        * Legend position : 'best','upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center'
 * The [config.yaml](https://github.com/Flame1045/SimplePlotter/blob/main/test1/config_subplot1.yaml) 
    * This config is to set plot details, such as data.txt location, data range, split character, Legend name.  
    * The name of this type of file can be changed freely, however please put it under a folder. The name of folder is up to you, such as test1 in my repo, and use the below argument when running this program.  
    ```
    --exper_dir "./your_directory" 
    ```
    * Param explain : 
      * Filename : Path to your raw data that need to plot
      * Xstart : It's in [row, col] format, row and col count from 1. This indicate the starting point of data that belong to x-axis   
      * Xend : It's in [row, col] format, row and col starts from 1. This indicate the ending point of data that belong to x-axis  
      * Ystart : It's in [row, col] format, row and col count from 1. This indicate the starting point of data that belong to y-axis   
      * Yend : It's in [row, col] format, row and col count from 1. This indicate the ending point of data that belong to y-axis 
      * Splitchar : The way how each data is split. Supports space(' ') and other type of characters
      * Legend : THe name you want to show on the final output graph
      
  
  
  

