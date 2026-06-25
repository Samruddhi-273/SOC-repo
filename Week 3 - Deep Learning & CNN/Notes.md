## Introduction to Deep Learning

### What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses multi-layer neural networks to learn complex patterns from data. It powers applications such as image recognition, speech recognition, NLP, recommendation systems, and autonomous vehicles.

### Why Deep Learning Became Popular

* Availability of large datasets
* Powerful GPUs
* Improved algorithms
* Open-source frameworks such as TensorFlow and Keras

### Applications

* Image Classification
* Object Detection
* Speech Recognition
* Natural Language Processing
* Medical Diagnosis
* Self-Driving Cars


# Neuron and Neural Networks

## Biological Neuron

A biological neuron receives signals through dendrites and passes output through an axon.

## Artificial Neuron

Mathematically:

[z = w_1x_1 + w_2x_2 + ... + w_nx_n + b]

Output:

[a = f(z)]

Where:

* x = input
* w = weights
* b = bias
* f = activation function


## Neural Network Structure

### Input Layer

Receives features.

### Hidden Layers

Perform transformations.

### Output Layer

Produces predictions.


# TensorFlow, Keras and PyTorch

## TensorFlow

* Developed by Google
* Production friendly
* Excellent deployment ecosystem

## Keras

* High-level API
* Simplifies TensorFlow usage

## PyTorch

* Developed by Meta
* Preferred in research
* Dynamic computation graphs


# Handwritten Digit Recognition (MNIST)

Dataset:

* 70,000 images
* Digits 0–9
* Image size: 28×28

Steps:

1. Load dataset
2. Normalize pixel values
3. Flatten images
4. Build neural network
5. Train model
6. Evaluate performance


# Activation Functions

Activation functions introduce non-linearity.

## Sigmoid

[\sigma(x)=\frac{1}{1+e^{-x}}]

Range:0 to 1

Used in binary classification.

### Problems

* Vanishing gradients
* Slow training


## Tanh

[tanh(x)]

Range:-1 to 1`

Advantages:

* Zero-centered outputs


## ReLU

[ReLU(x)=max(0,x)]

Advantages:

* Fast
* Most commonly used

Disadvantage:

* Dead neurons

## Softmax

Converts outputs into probabilities.

Used for:

* Multi-class classification



# Derivatives

Derivative measures rate of change.

Example:

[f(x)=x^2]

[f'(x)=2x]

Importance:

* Used in gradient descent
* Helps optimize neural networks


# Matrix Basics

Deep Learning heavily relies on matrices.

Example:

[
A=\begin{bmatrix}
1 & 2 \
3 & 4
\end{bmatrix}
]

Operations:

* Addition
* Multiplication
* Transpose
* Dot Product

Matrices help perform computations efficiently on GPUs.


# Loss Function

Loss measures prediction error.

## Mean Squared Error (MSE)

[MSE=\frac{1}{n}\sum(y-\hat y)^2]

Used in:

* Regression

## Binary Cross Entropy

[-\frac1n\sum[y\log(p)+(1-y)\log(1-p)]]

Used in:

* Binary classification


## Categorical Cross Entropy

Used for:

* Multi-class classification

Goal:

* Minimize loss


# Gradient Descent

Optimization algorithm used to minimize loss.

Update Rule:

[w = w - \alpha \frac{\partial L}{\partial w}]

Where:

* α = learning rate
* L = loss

Process:

1. Calculate loss
2. Compute gradients
3. Update weights
4. Repeat


# Neural Network from Scratch

Steps:

1. Initialize weights
2. Forward propagation
3. Compute loss
4. Backpropagation
5. Update weights

This demonstrates how neural networks learn without high-level libraries. 


# Batch vs Mini-Batch vs SGD

## Batch Gradient Descent

Uses entire dataset.

Pros:

* Stable

Cons:

* Slow

## Stochastic Gradient Descent (SGD)

Uses one sample at a time.

Pros:

* Faster updates

Cons:

* Noisy


## Mini-Batch Gradient Descent

Uses small batches.

Pros:

* Efficient
* Most widely used


# Chain Rule

Fundamental concept behind backpropagation.
Allows gradients to flow backward through layers.

# TensorBoard

Visualization tool for TensorFlow.

Features:

* Training loss graphs
* Accuracy tracking
* Histograms
* Graph visualization

Benefits:

* Easier debugging
* Better monitoring

# GPU Benchmarking

Why GPUs?

* Massive parallelism
* Faster matrix operations
* Faster training

CPU: Sequential computation

GPU: Parallel computation

# Customer Churn Prediction using ANN

Goal: Predict whether customer will leave a company.

Pipeline:

1. Data Cleaning
2. Encoding
3. Feature Scaling
4. ANN Creation
5. Training
6. Evaluation


# Evaluation Metrics

## Confusion Matrix

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |



## Precision

[Precision=\frac{TP}{TP+FP}]

Measures correctness of positive predictions.

## Recall

[Recall=\frac{TP}{TP+FN}]

Measures ability to find positives.


## F1 Score

[F1=\frac{2PR}{P+R}]

Balances precision and recall.

# Dropout Regularization

Problem:Overfitting

Solution:Randomly disable neurons during training.

Benefits:

* Better generalization
* Reduces overfitting


# Handling Imbalanced Datasets

Problem:Model predicts majority class.

Solutions:

* Undersampling
* Oversampling
* SMOTE
* Class weights


# Computer Vision Basics

Computer Vision enables machines to understand images.

Applications:

* Face Recognition
* Medical Imaging
* Autonomous Vehicles
* Security Systems


# Convolutional Neural Networks (CNN)

CNNs are specialized neural networks for image processing.

Main Components:

### Convolution Layer

Extracts features.

Examples:

* Edges
* Corners
* Shapes

### Pooling Layer

Reduces dimensions.

Types:

* Max Pooling
* Average Pooling

Benefits:

* Faster computation
* Reduced overfitting

---

### Fully Connected Layer

Performs final classification.

---

# CIFAR-10 Image Classification

Dataset:

* 60,000 images
* 10 classes

Classes:

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

Pipeline:

1. Load dataset
2. Normalize
3. Build CNN
4. Train
5. Evaluate

# Padding and Stride

## Padding

Adds zeros around image borders.

Benefits:

* Preserve spatial dimensions
* Prevent information loss

Types:

* Valid Padding
* Same Padding

## Stride

Controls filter movement.

Moves one pixel.

Larger stride:

* Faster computation
* Smaller output

---

# Data Augmentation

Technique to artificially increase dataset size.

Methods:

* Rotation
* Zoom
* Flip
* Shift
* Brightness adjustment

Benefits:

* Better generalization
* Reduced overfitting

## Note
### ANN Pipeline

Input
 ↓
Hidden Layers
 ↓
Activation Function
 ↓
Output
 ↓
Loss Function
 ↓
Backpropagation
 ↓
Gradient Descent


### CNN Pipeline

Image
 ↓
Convolution
 ↓
ReLU
 ↓
Pooling
 ↓
Fully Connected Layer
 ↓
Prediction
