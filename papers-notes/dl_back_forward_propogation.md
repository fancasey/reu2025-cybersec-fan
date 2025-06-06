# Forward Passes and Back Propogation
This is the essential process of deep learning.
## [First, the Chain Rule](https://machinelearningmastery.com/the-chain-rule-of-calculus-for-univariate-and-multivariate-functions/)
We learned in Calc I that for one variable $x$, 

$$\frac{d}{dx}f(g(x)) = \frac{df}{dg} \cdot \frac{dg}{dx}$$

or alternatively, 

$$\frac{d}{dx}f(g(x)) = f'(g(x))g'(x)$$

With multiple variables, consider vectors 

$$\mathbf{u} \in \mathbb{R^m}, \mathbf{v} \in \mathbb{R^n}$$ 

and functions (or in the case of DL, linear transformations) 

$$g: \mathbb{R^m} \rightarrow \mathbb{R^n}, f: \mathbb{R^n} \rightarrow \mathbb{R}, f \circ g: \mathbb{R^m} \rightarrow \mathbb{R}$$

So that $g(\mathbf{u}) = \mathbf{v}, f(g(\mathbf{u})) = f(\mathbf{v})$. If we want to find the partial derivative $\frac{\partial f}{\partial u_i}$, that would be

$$\frac{\partial f}{\partial u_i} = \frac{\partial f}{\partial v_1} \cdot \frac{\partial v_1}{\partial u_i} + \frac{\partial f}{\partial v_2} \cdot \frac{\partial v_2}{\partial u_i} + \ldots + \frac{\partial f}{\partial v_n} \cdot \frac{\partial v_n}{\partial u_i}$$

A way to think about this is to say: OK, $f$ is affected by $\mathbf{v}$, which is affected by $\mathbf{u}$. If I want to see how $u_i$ affects $f$, then I should see how $\mathbf{v}$ affects $f$ first. We can do this component-wise. Then for each component, let's see how $u_i$ affects that component, $v_j$. Multiplying the two gives us how $u_i$ affects $f$ for that specific component $v_j$. Since $\mathbf{v} = \mathbf{v_1} + \mathbf{v_2} + \ldots + \mathbf{v_n}$, where $\mathbf{v_i} \in \mathbb{R^n}$ filled with $0$ in all but the $i^\text{th}$ spot, where it's $v_i$, it would make sense to add up those partial derivatives. Note that this is not a rigorous proof, just some intuition as to where this comes from.

It follows from here that the gradient is

$$\begin{align*}
\nabla f &= \begin{bmatrix}
    \frac{\partial f}{\partial u_1} \\
    \frac{\partial f}{\partial u_2} \\
    \vdots \\
    \frac{\partial f}{\partial u_m}
\end{bmatrix}
\end{align*}$$

## [Now, Deep Learning](https://towardsdatascience.com/neural-networks-backpropagation-by-dr-lihi-gur-arie-27be67d8fdce/?source=friends_link&sk=3c5ba280bdb2f55d1c464967192d0fb4)
Basically, the way a neural network is a model that tries to solve a problem based on data. We formulate problems this way: given an input, you expect an output. We'll take our data and format it into vectors: the input is an $\mathbf{u} \in \mathbb{R^m}$ vector and the output is an $\mathbf{v} \in \mathbb{R^n}$ vector. Maybe there's a linear relationship between the input and output! So we try to find $A \in \mathbb{R^n} \times \mathbb{R^m}, \mathbf{b} \in \mathbb{R^n}$ such that

$$A \mathbf{u} + \mathbf{b} \approx \mathbf{v}$$
*Note:* $A$ and $\mathbf{b}$ are not given to us. We are only given $\mathbf{u}$, and we have to **find** the $A$ and $\mathbf{b}$ that get us close to $\mathbf{v}$. How to do this is described in the [back propogation section](#back-propogation).

But as we see in real life, not all relationships are linear! So we need add an activation function (ReLU, sigmoid) that is non-linear. Let's use the sigmoid function. So now we have:

$$\mathbf{z} = \sigma(A \mathbf{u} + \mathbf{b})$$

Maybe this is good if we want our output components to be between 0 and 1 (as that's the range for the sigmoid function), but that's not always the case. Well, we have this new vector $\mathbf{z}$, so let's put that through a linear transformation to hopefully fit $\mathbf{v}$!

$$A' \mathbf{z} + \mathbf{b}' \approx \mathbf{v}$$

*Note:* Although this is a linear transformation, we're not gonna get a line, since we had that non-linear activation function to get $\mathbf{z}$! So the hope is that this fits $\mathbf{v}$ even better!

## Forward pass
And the people who came up with neural networks were pretty clever in that they applied this logic multiple times. I'm gonna be pretty lazy with my notation here, so feel free to follow somewhere else if you don't understand, but the idea is to have multiple linear transformations & additions of however many dimensions you want, passing them through activation functions along the way, as long as the sequence is able to take in some $\mathbf{u}$ and give out some $\hat{\mathbf{v}}$, which looks like this:

$$\mathbf{z_1} = \sigma(A_1 \mathbf{u} + \mathbf{b_1}), \mathbf{z}_i = \sigma(A_i \mathbf{z}_{i - 1} + \mathbf{b_i}), A_l \mathbf{z}_l + \mathbf{b}_l = \hat{\mathbf{v}} \approx \mathbf{v}$$

where $l$ is 1 more than the number of layers there are. Going through this is called a **forward pass**.

## The cost function
Ok, so for some input, we have a guess at what the output could be and the actual output. So it makes sense to want to know how close we were. Well vectors are really just points in a space, so we could find the distance between them. There are a lot of ways to compute distance, but one of them would be to subtract terms and then square the difference. From here, we'll just take the average of the squared differences: this is called **mean squared error (MSE)**. If we have $d$ data points, the MSE would be:

$$\frac{1}{d}\sum^{d}_{i = 1}(\hat{\mathbf{v}}_i - \mathbf{v}_i)^T(\hat{\mathbf{v}}_i - \mathbf{v}_i)$$

We could also (maybe more obviously) use absolute value (or any other norm), but squaring distances has the nice effect of emphasizing points that are farther away. 

So now we have this nice expression for our **cost**. We'd like to minimize the cost. How do we do this? Well, first it might help to make this a function. Most immediately, we can make our cost function $c$ take in guesses and actual values:

$$c(\hat{\mathbf{v}}, \mathbf{v}) = \frac{1}{d}\sum^{d}_{i = 1}(\hat{\mathbf{v}}_i - \mathbf{v}_i)^T(\hat{\mathbf{v}}_i - \mathbf{v}_i)$$

where $\hat{\mathbf{v}}$ is a collection of $d$ guesses and $\mathbf{v}$ is a collection of $d$ corresponding actual values.

We're given the actual values, but we can't actually control the guesses, at least not directly. What we *can* control is how we get those guesses. And how did we get those guesses? With $\mathbf{A} = A_1, A_2, \ldots, A_l$ and $\mathbf{b} = \mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_l$. So really, our cost function should take in the $\mathbf{u}, \mathbf{A}, \mathbf{b},$ and $\mathbf{v}$, and give us back the MSE. Moreover, we can only change $\mathbf{A}$ and $\mathbf{b}$, so let's set $\mathbf{u}$ and $\mathbf{v}$ to be constant in $c$:

$$c(\mathbf{A}, \mathbf{b}) = \frac{1}{d}\sum^{d}_{i = 1}(\hat{\mathbf{v}}_i - \mathbf{v}_i)^T(\hat{\mathbf{v}}_i - \mathbf{v}_i)$$

where $\mathbf{u}, \mathbf{v}$ are fixed and $\hat{\mathbf{v}}$ is calculated using $\mathbf{u}, \mathbf{A}, \mathbf{b}$.

## Gradient descent
Now we have a cost function that takes in two variables (or many variables if you think of each component of $\mathbf{A}$ and $\mathbf{b}$ to be a variable) and turns it into one. We'd like to minimize this: to do this, we're going to use **gradient descent**.

I mentioned the gradient in the [chain rule section](#first-the-chain-rule). Basically, it's the partial derivative of a function for each variable in that function. My claim is that the gradient tells us (locally) the way to move so that we travel the farthest, *and* how much how to move by.

## Back propogation