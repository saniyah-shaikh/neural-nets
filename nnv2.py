# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:16:03 2017

@author: Saniyah
"""

def read_inputs(filename):
        file = open(filename, 'r') 
        inputs = []
        outputs = []
        for line in file: 
            elements = line.split(' ')
            inp = []
            for x in range(len(elements)-1):
                inp.append(int(elements[x]))
            out = int(elements[-1])
            inputs.append(inp)
            outputs.append(out)
        print ("Inputs: " + str(inputs))
        print ("Outputs: " + str(outputs))
        return inputs, outputs
    

class Neuron(object):
    def __init__(self, ins = [], ws = [], lw = 0.0015):
        self.inputs = ins
        self.weights = ws
        self.learn_w = lw
        
    def set_inputs(self, ins):
        self.inputs = ins
    
    def set_weights(self, ws):
        self.weights = ws
        
    def activation(self, v):
        return int(round(v))
        
    def calc_result(self):
        res = 0
        for x in range(len(self.inputs)):
            res += self.inputs[x] * self.weights[x]
        return self.activation(res)
        
    def reweight(self, expected):
        print ("Inputs: " + str(self.inputs))
        print ("Weights: " + str(self.weights))
        real = self.calc_result()
        print("Real: " + str(real) + " Expected: " + str(expected))
        for x in range(len(self.weights)):
            self.weights[x] = self.weights[x] + (self.learn_w * (expected - real) * self.inputs[x])
        return

class NeuralNet(object):
    def __init__(self, default_weights = [0, 0]):
        self.neuron = Neuron()
        self.neuron.set_weights(default_weights)

    def train(self, training_set_inputs, training_set_outputs):
        for x in range(len(training_set_inputs)):
            self.neuron.set_inputs(training_set_inputs[x])
            self.neuron.reweight(training_set_outputs[x])
            
    def think(self, inputs):
        self.neuron.set_inputs(inputs)
        return self.neuron.calc_result()
    
test = NeuralNet()
inputs, outputs = read_inputs("testdata-add-20-20.txt")
test.train(inputs, outputs)
print (test.think([15, 30]))