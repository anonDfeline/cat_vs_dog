from pickle_utils import load_obj
import numpy as np
import scipy
from scipy import ndimage
import tensorflow as tf

def forward_propagation(X, parameters):
    
    A_prev = tf.convert_to_tensor(X)
    for i in range(len(parameters) // 2 - 1):
        W = tf.convert_to_tensor(parameters["W"+str(i+1)])
        b = tf.convert_to_tensor(parameters["b"+str(i+1)])
        Z = tf.matmul(W, A_prev) + b
        A = tf.nn.relu(Z)
        A_prev = A
    i+=1
    W = tf.convert_to_tensor(parameters["W"+str(i+1)])
    b = tf.convert_to_tensor(parameters["b"+str(i+1)])
    Z = tf.nn.sigmoid(tf.matmul(W, A_prev) + b)
    
    with tf.Session() as sess:
        pred = sess.run(Z)
        
    return pred
    
def forward_propagation_np(X, parameters):
    A_prev = X
    for i in range(len(parameters) // 2 - 1):
        W = parameters["W"+str(i+1)]
        b = parameters["b"+str(i+1)]
        Z = np.dot(W, A_prev) + b
        A = np.maximum(Z, 0)
        A_prev = A
        
    i+=1
    W = parameters["W"+str(i+1)]
    b = parameters["b"+str(i+1)]
    Z = np.dot(W, A_prev) + b
    A = 1 / (1 + np.exp(-Z))
    return A

def main():
    params = load_obj("params_0001")

    test_path = "test1/download.jpg"

    image = np.array(ndimage.imread(test_path, flatten=False))
    my_image = scipy.misc.imresize(image, size=(64, 64))
    print(my_image.shape)
    my_image = np.array(my_image[:,:,:3]).reshape(64*64*3,1)

    my_image = np.array(my_image, dtype="float32") / 255

    pred = forward_propagation(my_image, params)

    print(pred)
    print("dog" if pred >= 0.5 else "cat")
    
if __name__ == "__main__":
    main()

