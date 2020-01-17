# Answer-Script-Evaluation
## This application evaluates student answer scripts using Natural Language Processing (NLP).
For the project, we have taken huge data for training. We have trained the model with 66Gb of text data (wiki corpus) (https://dumps.wikimedia.org/enwiki/) that has
almost all the words with its nearby predictive words. This huge data is fed to Latent Semantic
Indexing and we get a LSI model. This model has a size of about 2.5 GB and this model
contains all the data in numerical form. This step is performed because machine learning
algorithms can only understand numbers and not text. To work with text data in machine
learning, we convert all the text data to a numerical form that is understood by the machine
learning algorithms. 
###    
After the LSI model is created, the making scheme is taken and stop
words are removed from it and converted to dictionary. This dictionary contains all the unique
words and these words are mapped to some unique numbers. The dictionary contains these
unique numbers as keys and the occurrence of those words as values. This dictionary is then
converted to bag of words. The same procedure is applied to the answer sheet as well. The bag
of words that was created by the marking scheme is passed to the LSI model and the data is
prepared for comparison and we get a set of indexing values which eases the comparing
process.
###    
Now the answer sheet’s corpus is taken and is passed through the LSI model and set of
values is generated. This set of values is again compared with the indexed values of the marking
scheme. The LSI model compares these values from answer sheet and marking scheme and
assigns a comparsion percentage. This process is applied to each sentence and each sentence will
have a comparison score. The average of these comparison scores is taken for one answer and
this average is the comparison score of that answer. Marks is assigned based on this compariosn
score for each answers and after all answers are processed, marks are added up and total marks is
obtained.
###
### Stages of evaluation:
##### 1. Input Text Processing
##### 2. Removing Stop Words
##### 3. Bag of Words
##### 4. Comparison of Text
##### 5. Sentiment Analysis
##### 6. Assigning Marks
###
## The front end of this application looks like this.
###  
![front](https://user-images.githubusercontent.com/40026126/72591767-00e90380-3927-11ea-958f-5943d3875ff3.png)
###  
## The application after evaluating.
###
![front1](https://user-images.githubusercontent.com/40026126/72591774-047c8a80-3927-11ea-898c-f4cbea0fd121.png)
### 
## Output on the terminal.
###
![output](https://user-images.githubusercontent.com/40026126/72591778-08a8a800-3927-11ea-9ef4-48732d55675c.png)
###
## Similarities with each sentence.
###
![sim](https://user-images.githubusercontent.com/40026126/72593537-3e4f9000-392b-11ea-9261-3931c08cd6d2.png)
###  
In the above figure, entities in the index 0 refers to first sentence in the answer sheet. The
comparison scores written against it indicates the index number, similarity with that of the
marking scheme sentences. Here 0 , 0.9099441 indicates that sentence 0 of answer sheet has a
comparison percentage of 90% with sentence 0 of marking scheme.
### 
Similarly, the second entity 5, 0.68514407 indicates that sentence 0 of answer sheet has a comparison percentage of 68% with
sentence number 5 of marking scheme. 
### 
Similarly, the entire set of sentences are listed for each
answer script. For each index of answer script, the marking scheme index with maximum comparison percentage is selected and assigned as most similar with the corresponding comparison percentage.
### 
## One of the sample answer to a question from student's answer script.
###
![as1](https://user-images.githubusercontent.com/40026126/72593915-347a5c80-392c-11ea-8547-d38df062cc8a.png)
###
## Sample answer to a question from teacher's marking scheme.
###
![as2](https://user-images.githubusercontent.com/40026126/72593919-36dcb680-392c-11ea-9440-137c916fd0d1.png)
###
## Marks allotment to every subsequent question number.
###
![marks](https://user-images.githubusercontent.com/40026126/72592725-3393fb80-3929-11ea-86fb-a0858112fea8.png)
###
## This file contains question number attended by student.
###
![attended](https://user-images.githubusercontent.com/40026126/72592730-37278280-3929-11ea-9949-f05ea4936944.png)
