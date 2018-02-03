# SEPIA
_SEPIA - Suggestive Evolving Pixel Interpreting Algorithm_

### A machine learning algorithm to learn and detect image contents

## Suggestion

SEPIA uses a cost averaging algorithm to use image pixel data in the most efficient way possible. Using center-biased radial cost increase gradients, the algorithm is made to use **approximate** pixel locations, meaning it is optimised specifically for two dimensional, low detail, two-toned images (e.g. a black square against a white background, or letters of the alphabet). It is also fully scaleable in all ways, meaning that it can work with almost any shapes with as many combinations and variations as required, without a need to edit any code.

For example,

```
1 0 1 0 1
0 0 1 1 1
1 0 0 1 0
0 1 1 1 0
0 0 0 1 0
```

would become

```
0.375 0.21875 0.3515625 0.27734375 0.35546875
0.3359375 0.2412109375 0.2890625 0.3544921875 0.421875
0.46484375 0.271484375 0.30517578125 0.361328125 0.1748046875
0.22265625 0.390625 0.41796875 0.59765625 0.08984375
-0.140625 0.0625 0.1953125 0.671875 -0.09375
```

... without any other data.

Under close observation, this clearly shows that the most dominant number in the input has the largest effect on those around it: a `1` can leave a trace on the surrounding numbers, as when the algorithm is in use after training, the entered pixel data might include some information that it has never seen before (maybe the whole shape is move a little to the right, or one angle of the triange is steeper than ever previously encountered. In this case, the aforementioned can 'save the day', as in training the adjacent and almost adjacent `1`s can still leave a positive effect on those that were untouched. However, as the pixel costs are a result of an average of all of the training info (plus what is passed on from adjacent pixels), any anomolies can be cancelled out with relatively few generations.

In a smaller sample, we would find that
```
1 0
0 0
```
would become
```
1 0.5
0.5 0.25
```

However, as there are minus scores for having a '0' status, we would be left with
```
1 -0.25
-0.25 -0.5
```

But then, every value's status has to intefere with every other value's status, and we have generated a new `0.0` now, which has to be given minus points, and this continues until eventually there are no more required steps, and the simple, four digit `1000` sequence we entered at the start finally gets interpreted and 'saved' as 
```
0.5 -0.125 
-0.09375 -0.1875
```
... clearly a lot more complicated than our original number, but we can see patterns. The lowest number is `-0.1875`, which makes sense, as to the eyes of the algorithm, a diagonal is further away than a horizontal or vertical joint. Then, the next lowest is `-0.125`, which is because in a picture, a horizontal pixel is generally more likely to be defined during training with many different offsets than a vertical one, so it is lower to avoid over-compensation. Finally, the biggest number (other than `0.5`, which is the biggest, for obvious reasons) is `-0.09375`, as it is a vertically offset pixel, so it gets more compensation than a diagonal or horizontal offset, and wasn't extremely negative in the first stage either, so it has a much higher calculated score than the others - and remember: these numbers were all zeros to begin with, and without any training data it turned them into these confusing yet very logical decimals in just the first generation.

In the following generations of data, the numbers are converted to this sugggestive format, and averaged out with the average from previous generations. All in all, this optimises SEPIA for shape recognition, so __do _not_ attempt to use it for text, audio, or coloured pictures.
