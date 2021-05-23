# color recognition
digikala represents a cup one months ago and one of the questions was recognition of colors of products. there was a train set of data with about 6000 images with 12 color classes and a test set with 2000 image without labels. in this repository we work with the train set and try to recognize the color of the images.
the images is noise free and we dont need any preprocessing before the the main model.

you can download the data from this link:
https://quera.ir/assignment/20120/download_problem_initial_project/66279/

1. first step to build the model is to prepare the data. the data must be in the shape of an numpy array. go to the file step1.py
after that we have a list named imageaddress that includs addresses of all files and a list named labels that has the label of any image.


2. second step is to convert your images to numpy array. the input for a CNN model should be some numbers that come from the image pixels. the convertion take a while to convert and i don't know why!(please if anybody can help me whit that i would be appreciated)

3. third step is to turn data labels into categorical numbers. 

4. in this step we want to split our data to train and test sets.

5. step 5 is about to give weights to our classes. if we don't calculate weights our models prediction would be wrong and not measurable. for calculates weights we divide the number of datas in each class by sum of all datas and then substract 1 from that and put weights in a dictionary.

6. we need to convert our labelset to categorical.

7. it's time to make the model. i used and old model structure os mine that i used it for another purpose. but it has very good results on this data and I decide to use it here.

8. I've got this result after 100 epochs:
loss: 0.0386 - acc: 0.9856 - val_loss: 1.9504 - val_acc: 0.7422

let me know your results. i'll be happy too.
