# Preparatory Assignment

The purpose of this preparatory assignment is to make sure that you (and your computer) are well prepared for the block course in August to avoid having technical issues during the block course. Therefore, this __assignment is mandatory__ and has to be __submitted until Friday, August 7th__. 

The assignment can be __accessed and submitted via [GitHub Classroom](https://classroom.github.com/a/XeAN5a_k)__. This requires a [GitHub user account](https://github.com/). Please create one and register for [GitHub Education benefits](https://education.github.com/benefits).

__Important notes:__ 

* Please make sure to __name the output files exactly as described.__
* If you encounter problems which you cannot solve on your own, create a new topic in the [GitHub forum of this course](https://github.com/orgs/geoscripting/teams/advanced-geoscripting-2020/discussions) and describe your problem.  

## Learning goals

After you have completed this assignment you will be able to ...

*  name different best practice methods for scientific computing, 
*  install and configure all required software for the course,
*  use Jupyter notebook to write Python code and
*  use git to track your work progress. 

## 1. Best Practices in Scientific Computing

<img src="./img/phdcomic_final.png" alt="final" width="300px" align="right" />

Read the paper by [Wilson et al. (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/) on Best Practices for Scientific Computing and answer the following questions. Write your answer in a text file called _scientific\_programming.txt_.

1. The paper describes several problems scientist face when performing scientific data analyses. From your experience in performing (GIS) analyses, which of these problems seem familiar to you? Have you faced other problems not mentioned in the paper? (~100 words)
2. Which methods described in the paper could help you avoid these problems in the future? (~100 words)
3. One of the recommendations by [Wilson et al. (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/) for scientists is to use a Version Control System (VCS). Briefly explain in your own words, what the benefits of VCS are in the context of scientific analyses. (~100 words)

<sup>Image source: “Piled Higher and Deeper” by Jorge Cham, http://www.phdcomics.com</sup>

## 2. Install required software

1. Follow the instructions given in the section [Software Setup](../software_setup) to install and configure all software that is required for the course on your computer. 

2. Execute the python file _check\_environment.py_ from within your new Python environment to verify that all required packages have been installed successfully. Using the following command the output of the program will be written to a new text file called _check\_environment\_result.txt_. Make sure that you don't get any import errors. 

	```
	$ python check_environment.py > check_environment_result.txt
	```

## 3. Using git and Jupyter Notebooks

In this last section, you will use git to track the changes of the files that we have created so far. If you are not familiar with git yet, work through the section [Introduction to git](git/index.rst) before continuing with the exercises. 

### Clone GitHub repository and track your changes

1. If you haven't done so already, clone the GitHub repository of this assignment on your computer. Make sure to use the __URL of your repository__. 

	```
	git clone https://github.com/geoscripting/preparatory-assignment-redfrexx.git
	```
	
2. In the previous two exercises you have created two files. Copy these files into the main folder of the cloned repository. Create a commit for each one of them in order to track them in your local git repository, e.g.

	```
	git add scientific_programming.txt
	git commit -m "added scientific_programming.txt" 
	```

### Create a new Jupyter notebook

1. Activate the _advgeoscripting_ environment and start a Jupyter Notebook server. 
2. Create a new Jupyter notebook using the Python 3 kernel and name it _preparatory\_assignment.ipynb_. 
3. Import the function ```check_packages()``` from _check\_environment.py_ and execute it in order to check whether the notebook is using the right anaconda environment 'advgeoscripting'. If you get a ```ModuleImportError```, check whether the right kernel is selected (Jupyter Menu: Kernel &rarr; Change kernel).
4. If everything works, save your notebook and add it to your git repository by creating a new commit.
5. Within the notebook, write a new function called ```list_sum()```, which calculates the sum of all numbers in a list. e.g. 

	``` python
	>>> numbers = [1,2,3,4]
	>>> numbers_sum = list_sum(numbers)
	>>> print(numbers_sum)
	10
	```

6. Create a new commit containing the changes of the notebook. 

### Synchronise your repository with GitHub

The last task of this assignment is to push all your commits to GitHub. 

```
git push origin master 
```

__One last note:__ If you make further edits to your files (e.g. editing your answers to the questions in exercise 1) remember that you can always synchronise these changes with your GitHub repository by creating further commits and pushing them to GitHub. 


### Well done, your ready for the course! :) 







