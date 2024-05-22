from manim import *

class ParaSurface3(ThreeDScene):
    def construct(self):
        Text.set_default(font_size= 20, color= YELLOW)
        MathTex.set_default(font_size= 25, color= YELLOW)
        Title = Text("Higher Dimensional Logistic Regression", color= BLUE).to_edge(UP)

        #One Dimensional Data
        onedimensional = Text("One Dimensional").shift(Title.get_bottom() + LEFT * 5 + DOWN * 0.5)
        sigmoid_function = MathTex(r"\sigma(b+wx)=\frac{1}{1+e^{-b(b+wx)}}").shift(onedimensional.get_bottom() + DOWN * 0.5)
        weigh_bias = MathTex(r"w_{0}=1,b_{0}=1").shift(sigmoid_function.get_bottom() + DOWN * 0.5)
        iteration = Text("For iteration m of M:").shift(weigh_bias.get_bottom() + DOWN * 0.5)
        weigh = MathTex(r"w_{m}=w_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)x_{i}").shift(iteration.get_bottom() +  DOWN * 0.8)
        bias = MathTex(r"b_{m}=b_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)").shift(weigh.get_bottom() + DOWN * 0.5)
        optimal_values = MathTex(r"\text{Optimal Values }:w_{M},b_{M}").shift(bias.get_bottom() + DOWN * 0.8)
        decision_boundary = MathTex(r"\text{Decision Boundary: }b_{m}+w_{m}x=0").shift(optimal_values.get_bottom() + DOWN * 0.5)


        #two dimension
        twodimensional = Text("Two Dimensional").shift(Title.get_bottom() + DOWN * 0.5 + LEFT * 0.5)
        sigmoid_function2 = MathTex(r"\sigma(b+wx)=\frac{1}{1+e^{-b(b+wx)}}").shift(twodimensional.get_bottom() + DOWN * 0.5)
        xwR2 = MathTex(r"x,w\epsilon \mathbb{R}").shift(sigmoid_function2.get_bottom() + DOWN * 0.5)
        weigh_bias2 = MathTex(r"w_{0}=\text{[1 1]}^{T} ,b_{0}=1").shift(xwR2.get_bottom() + DOWN * 0.5)
        iteration2 = Text("For iteration m of M:").shift(weigh_bias2.get_bottom() + DOWN * 0.5)
        weigh2 = MathTex(r"w_{m}=w_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)x_{i}").shift(iteration2.get_bottom() +  DOWN * 0.8)
        bias2 = MathTex(r"b_{m}=b_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)").shift(weigh2.get_bottom() + DOWN * 0.5)
        optimal_values2 = MathTex(r"\text{Optimal Values }:w_{M},b_{M}").shift(bias2.get_bottom() + DOWN * 0.8)
        decision_boundary2 = MathTex(r"\text{Decision Boundary: }b_{m}+w_{m}x=0").shift(optimal_values2.get_bottom() + DOWN * 0.5)


        #two dimension
        threedimensional = Text("Three Dimensional").shift(Title.get_bottom() + DOWN * 0.5 + RIGHT * 4)
        sigmoid_function3 = MathTex(r"\sigma(b+w^{T}x)=\frac{1}{1+e^{-b(b+w^{T}x)}}").shift(threedimensional.get_bottom() + DOWN * 0.5)
        xwR3 = MathTex(r"x,w\epsilon \mathbb{R^{d}}").shift(sigmoid_function3.get_bottom() + DOWN * 0.5)
        weigh_bias3 = MathTex(r"w_{0}=\text{[1 1 1 ,,, 1]}^{T} ,b_{0}=1").shift(xwR3.get_bottom() + DOWN * 0.5)
        iteration3 = Text("For iteration m of M:").shift(weigh_bias3.get_bottom() + DOWN * 0.5)
        weigh3 = MathTex(r"w_{m}=w_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)x_{i}").shift(iteration3.get_bottom() +  DOWN * 0.8)
        bias3 = MathTex(r"b_{m}=b_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)").shift(weigh3.get_bottom() + DOWN * 0.5)
        optimal_values3 = MathTex(r"\text{Optimal Values }:w_{M},b_{M}").shift(bias3.get_bottom() + DOWN * 0.8)
        decision_boundary3 = MathTex(r"\text{Decision Boundary: }b_{m}+w_{m}x=0").shift(optimal_values3.get_bottom() + DOWN * 0.5)


        self.play(Create(Title))
        self.wait(2)
        self.play(Create(VGroup(onedimensional, twodimensional, threedimensional, sigmoid_function, sigmoid_function2, xwR2, sigmoid_function3, xwR3)))
        self.wait(3)
        self.play(Write(VGroup(sigmoid_function, weigh_bias, iteration, weigh, bias, optimal_values, decision_boundary)))
        self.wait(3)
        self.play(Write(VGroup(sigmoid_function2, weigh_bias2, iteration2, weigh2, bias2, optimal_values2, decision_boundary2)))
        self.wait(3)
        self.play(Write(VGroup(sigmoid_function3, weigh_bias3, iteration3, weigh3, bias3, optimal_values3, decision_boundary3)))
        self.wait(3)
        self.play(FadeOut(VGroup(Title, onedimensional, sigmoid_function, weigh_bias, iteration, weigh, bias, optimal_values, decision_boundary, threedimensional, xwR3, xwR2, sigmoid_function3, weigh_bias3, iteration3, weigh3, bias3, optimal_values3, decision_boundary3, twodimensional, sigmoid_function2, weigh_bias2, iteration2, weigh2, bias2, optimal_values2, decision_boundary2, threedimensional, xwR3, sigmoid_function3, weigh_bias3, iteration3, weigh3, bias3, optimal_values3, decision_boundary3)))
        self.wait(3)
