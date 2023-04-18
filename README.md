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
     * This config is to set plot Title, X and Y axis name, Legend position. (Note that please keep the "CONFIG.yaml" intact to prevent can't find file error)
        * Title : can be any string 
        * X and Y axis name : can be any string 
        * Legend position : support 'best' 'upper right' 'upper left' 'lower left' 'lower right' 'right' 'center left' 'center right' 'lower center' 'upper center'     'center'
 * The [config.yaml](https://github.com/Flame1045/SimplePlotter/blob/main/test1/config_subplot1.yaml) 
    * This config is to set plot details, such as data.txt location, data range, split character, Legend name.  
    * The name of this type of file can be changed freely, however please put it under a folder. The name of folder is up to you, such as test1 in my repo, and use the below argument when running this program.  
    ```
    --exper_dir "./your_directory" 
    ```
    * The most im
      
  
  
  

