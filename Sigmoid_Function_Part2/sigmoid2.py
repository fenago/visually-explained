from manim import *

class sigmoid2(ThreeDScene):
    def construct(self):

        #<------------- Sigmoid Function domain, range and deciding probability --------------->
        sigmoid_function_tex = Tex("The Sigmoid Function").to_edge(UP)
        sigmoid_function = MathTex(r"S(x)=\frac{ 1 }{ 1 + e^{-x} }", color= YELLOW).shift(LEFT * 3 + UP * 1.8)
        sigmoid_function_domain = MathTex(r"x\varepsilon\mathbb{R}\Rightarrow\text{ Input any real value}", color= YELLOW, font_size= 35).shift(sigmoid_function.get_center() + RIGHT * 5.2 + UP *0.3)
        sigmoid_function_range = MathTex(r"S(x) \varepsilon [0,1]\Rightarrow\text{ Probability}", color= YELLOW, font_size= 35).shift(sigmoid_function.get_center() + RIGHT * 5 + DOWN *0.3)

        pisewise_function = MathTex(r"y = \begin{cases}1 & s(x) \geq 0\\0 & s(x) < 0.5\end{cases}", color= YELLOW, font_size= 40).shift(LEFT * 3)
        pisewise_function_tex = Text("If probability of datapoint being\npositive class >= 50%, assign it as\nthe positive class. Otherwise it is\nthe negative class", font_size= 20, color= YELLOW).shift(pisewise_function.get_center() + RIGHT * 6)
        pisewise_function_arrow = Arrow(start= pisewise_function.get_right(), end= pisewise_function_tex.get_left(), color= BLUE)

        y_range = MathTex(r"y\varepsilon\{0,1\}", font_size= 35, color= YELLOW).shift(DOWN * 2)




        self.play(Write(sigmoid_function_tex), run_time= 2)
        self.wait(1)
        self.play(Write(VGroup(sigmoid_function, sigmoid_function_domain, sigmoid_function_range)), run_time= 2)
        self.wait(4)
        self.play(Write(VGroup(pisewise_function, pisewise_function_arrow, pisewise_function_tex)), run_time= 2)
        self.wait(4)
        self.play(Write(y_range), run_time= 2)
        self.wait(2)
        #self.play(Write(Text("Decision Boundaries: Where do they fit in?",font_size= 30, color= RED).to_edge(DOWN)))
        #self.wait(2)
        self.play(FadeOut(sigmoid_function_tex, sigmoid_function, sigmoid_function_domain, sigmoid_function_range, pisewise_function, pisewise_function_arrow, pisewise_function_tex, y_range))

        #<----------------- Scene 1 ends here ---------------->



        #<----------------- NumberPlane, Decision Bounderies -------------->
        plane = NumberPlane( x_range= [-7, 8], y_range= [-4, 5],
            background_line_style={
                "stroke_width": 4,
                "stroke_opacity": 0.4
            }
        )
        
        #Boundary Line (single boundary where y= 0 and y= 1)
        boundary_line = always_redraw(lambda: Line(start= plane.c2p(4,0.5), end= plane.c2p(1,3.5)))

        #Boundary Lines (Multiples lines where y= 0, y= 1 and y= 2)
        line1 = Line(start= plane.c2p(4,1), end= plane.c2p(2.1,2.7))
        line2 = Line(start= plane.c2p(2.1,2.7), end= plane.c2p(1,3.5))
        line3 = Line(start= plane.c2p(2.1,2.7), end= plane.c2p(5,5.5))
        boundary_lines = VGroup(line1, line2, line3)

        #Arbitrary Dots when y=1 (i.e. on the left of boundary_lines)
        #Initial Color White
        d1, d2, d3, d4, d5, d6, d7, d8 = Dot(plane.c2p(0.5,0.5)).scale(0.7) , Dot(plane.c2p(1.8,0.3)).scale(0.7) , Dot(plane.c2p(1.3,1)).scale(0.7) , Dot(plane.c2p(1.6,1.3)).scale(0.7) , Dot(plane.c2p(2.5,1.1)).scale(0.7) , Dot(plane.c2p(2.2,1.8)).scale(0.7) , Dot(plane.c2p(1,1.2)).scale(0.7) , Dot(plane.c2p(1.5,2.5)).scale(0.7)
        dots_y1_white = VGroup(d1, d2, d3, d4, d5, d6, d7, d8)

        y1tex = Tex("y=1",font_size= 30, color= BLUE).shift(plane.c2p(0.5,1.8))


        #<---Arbitrary Dots when y=0 (i.e. on the rigth down side of boundary_line)--->        
        #Initial Color White
        d9, d10, d11, d12, d13, d14, d15 = Dot(plane.c2p(2.5,2.6)).scale(0.7) , Dot(plane.c2p(3.2,2.2)).scale(0.7) , Dot(plane.c2p(3.4,2.6)).scale(0.7) , Dot(plane.c2p(3.2,3)).scale(0.7) , Dot(plane.c2p(4,1.5)).scale(0.7) , Dot(plane.c2p(4.2,2.1)).scale(0.7) , Dot(plane.c2p(3.9,3)).scale(0.7)
        dots_y0_white = VGroup(d9, d10, d11, d12, d13, d14, d15)
        y0tex = Tex("y=0",font_size= 30, color= RED).shift(plane.c2p(5,3))

        #<--- Dots when y=2 (i.e. on the right up side of boundary_line) --->
        #Initial Color White
        dot16, dot17, dot18, dot19 = Dot(plane.c2p(2,3)).scale(0.7) , Dot(plane.c2p(2.3,3.2)).scale(0.7) , Dot(plane.c2p(1.9,3.3)).scale(0.7) , Dot(plane.c2p(1.8,3.6)).scale(0.7)
        dots_y2_white = VGroup(dot16, dot17, dot18, dot19)

        y2tex = Tex("y=2",font_size= 30, color= YELLOW).shift(plane.c2p(2,4))



        #self.add(plane, boundary_lines, dots_y1_white, dots_y2_white)
        self.play(Create(plane), run_time= 2)
        self.wait(2)
        self.move_camera(zoom= 1.2, frame_center= plane.c2p(2,1.5), run_time= 2)
        self.wait(2)
        self.play(Create(VGroup(dots_y1_white, dots_y0_white, dots_y2_white)))
        self.wait(4)
        self.play(Create(boundary_line), run_time= 2)
        self.wait(4)
        self.play(dots_y1_white.animate.set_color(color= BLUE))
        self.wait(3)
        self.play(dots_y0_white.animate.set_color(color= RED), dots_y2_white.animate.set_color(color= RED))
        self.play(Write(VGroup(y1tex, y0tex)))
        self.wait(3)
        self.play(ReplacementTransform(boundary_line, boundary_lines), run_time= 2)
        self.wait(2)
        self.play(dots_y2_white.animate.set_color(color= YELLOW))
        self.play(Write(y2tex))
        self.wait(2)
        self.play(FadeOut(VGroup(dots_y1_white, dots_y0_white, y1tex, y0tex, boundary_lines, dots_y2_white, y2tex)), run_time= 1)
        self.wait(1)

        #<-------------Plane scene ends here ------------------>


        #<------------Single dimension Scene ------------------->
        
        num_line = NumberLine()

        #Boundary for y=0, y=1 and y= 2
        boundary_line1 = Line(start= num_line.get_bottom() , end= num_line.get_top(), color= YELLOW).shift(num_line.n2p(-3))
        boundary_line2 = Line(start= num_line.get_bottom() , end= num_line.get_top(), color= YELLOW)

        # Arbitrary Dots on the number Line when y=0
        d1, d2, d3, d4, d5 = Dot(num_line.n2p(-5)), Dot(num_line.n2p(-4.8)), Dot(num_line.n2p(-4)), Dot(num_line.n2p(-3.6)), Dot(num_line.n2p(-3.3))
        dots_y0_white = VGroup(d1, d2, d3, d4, d5)
        y0tex = Tex("y=0", color= RED, font_size= 25).shift(num_line.n2p(-5) + UP * 0.5)

        # Arbitrary Dots on the number Line when y=1
        d1, d2, d3, d4, d5 = Dot(num_line.n2p(-2.9)), Dot(num_line.n2p(-2.5)), Dot(num_line.n2p(-2)), Dot(num_line.n2p(-1.6)), Dot(num_line.n2p(-1.3))
        dots_y1_white = VGroup(d1, d2, d3, d4, d5)
        y1tex = Tex("y=1", color= BLUE, font_size= 25).shift(num_line.n2p(-1.5) + UP * 0.5)

        # Arbitrary Dots on the number Line when y=2
        d1, d2, d3, d4, d5 = Dot(num_line.n2p(0.5)), Dot(num_line.n2p(1.1)), Dot(num_line.n2p(2)), Dot(num_line.n2p(2.3)), Dot(num_line.n2p(3))
        dots_y2_white = VGroup(d1, d2, d3, d4, d5)
        y2tex = Tex("y=2", color= YELLOW, font_size= 25).shift(num_line.n2p(2) + UP * 0.5)

        self.play(ReplacementTransform(plane, num_line), run_time= 2)
        self.move_camera(zoom= 1, frame_center= num_line.n2p(0))
        self.wait(2)
        self.play(Create(VGroup(dots_y0_white, dots_y1_white, dots_y2_white)), run_time= 2)
        self.add(boundary_line1)
        self.wait(2)
        self.play(dots_y0_white.animate.set_color(color= RED), dots_y1_white.animate.set_color(color= BLUE), dots_y2_white.animate.set_color(color= BLUE), dots_y2_white.animate.set_color(color= BLUE))
        self.play(Write(VGroup(y0tex, y1tex)))
        self.wait(4)
        self.play(Create(boundary_line2))
        self.play(dots_y2_white.animate.set_color(color= YELLOW))
        self.play(Write(y2tex))
        self.wait(2)
        self.play(FadeOut(VGroup(num_line, dots_y0_white, dots_y1_white, dots_y2_white, boundary_line1, boundary_line2, y0tex, y1tex, y2tex )))
        self.wait(2)


        #<-------------- Scene Ends Here ---------------->


        #<------------- Mathematical Expressions -------->

        #MathTex.set_color(color= YELLOW)
        MathTex.set_default(font_size= 30, color=  YELLOW)
        Text.set_default(font_size= 20, color= YELLOW)
        Title = Text("1.Dimensional Decision Boundary", font_size= 25, color= WHITE).to_edge(UP)
        sigmoid_function = MathTex(r"\sigma=\frac{ 1 }{ 1 + e^{-x} }").shift(UP * 2.5 + LEFT * 5)
        sigmoid_function_domain = MathTex(r"x\varepsilon\mathbb{R}").shift(sigmoid_function.get_center() + RIGHT * 2 + UP *0.3)
        sigmoid_function_range = MathTex(r"\sigma \varepsilon [0,1]").shift(sigmoid_function.get_center() + RIGHT * 2 + DOWN *0.3)

        # x replaced with b+wx
        sigmoid_function_wx = MathTex(r"\sigma=\frac{ 1 }{ 1 + e^{-x} }").shift(sigmoid_function.get_bottom() + DOWN * 0.5)
        # Threshold
        threshold = Text("Assuming a threshold of 50%").shift(sigmoid_function_wx.get_bottom()+ DOWN * 0.5)
        
        #Mathematical steps goes on
        step1 = MathTex("\sigma(b+wx)=0.5").shift(threshold.get_bottom()+ DOWN * 0.5)
        step2 = MathTex(r"0.5=\frac{1}{1+e^{-(b+wx)}}").shift(step1.get_bottom()+ DOWN * 0.5)
        step3 = MathTex(r"0.5+0.5e^{-(b+wx)}=1").shift(step2.get_bottom()+ DOWN * 0.5)
        step4 = MathTex(r"1+e^{-(b+wx)}=2").shift(step3.get_bottom()+ DOWN * 0.5)
        step5 = MathTex(r"e^{-(b+wx)}=2-1").shift(UP * 2.5 + RIGHT * 2)
        step6 = MathTex(r"-(b+wx)=log(2-1)").shift(step5.get_bottom()+ DOWN * 0.5)
        step7 = MathTex(r"b+wx=0").shift(step6.get_bottom()+ DOWN * 0.5)
        step8 = MathTex(r"-\frac{b}{w}").shift(step7.get_bottom()+ DOWN * 0.5)
        
        #Point decision boundary
        pdb = Text("Point decision boundary").shift(DOWN * 0.5)
        arrow = Line(start= pdb.get_top(), end= step8.get_bottom() ).add_tip(tip_length= 0.5).scale(0.5)
        implication = MathTex(r"Implication:P(y=1|x=-\frac{b}{w})=0.5").shift(DOWN * 1 + RIGHT * 2)

        self.play(Write(Title))
        self.wait(2)
        self.play(Write(sigmoid_function))
        self.wait(2)
        self.play(Write(VGroup(sigmoid_function_domain, sigmoid_function_range)))
        self.wait(2)
        self.play(Write(sigmoid_function_wx))
        self.wait(2)
        self.play(Write(threshold))
        self.wait(2)
        self.play(Write(step1))
        self.wait(2)
        self.play(Write(VGroup(step2, step3, step4, step5, step6, step7)), run_time= 3)
        self.wait(2)
        self.play(Write(step8))
        self.wait(2)
        self.play(Write(VGroup(pdb, arrow)))
        self.wait(2)
        self.play(Write(implication))
        self.wait(2)
        self.play(FadeOut(VGroup(Title, sigmoid_function, sigmoid_function_domain, sigmoid_function_range, sigmoid_function_wx, threshold, step1, step2, step3, step4, step5, step6, step7, step8, pdb, arrow, implication)))


        Text.set_default(font_size= 25, color= YELLOW)
        MathTex.set_default(font_size= 30, color=  YELLOW)
        # Training Phase for the 1 Dimensional Case

        Title = Text("Training Phase for the 1 Dimensional Case", color= WHITE).to_edge(UP)
        question = Text("Training = Find w and b that maximize probability of seeing training data\noptimization Technique = How do we want to learn? (like Gradient Descent)").shift(Title.get_bottom() + DOWN * 0.5)
        gradient_descent = Text("Gradient Descent Algorithm used here:").shift(UP * 1.5 + LEFT * 3)
        iteration = Text("For iteration m of M:", color= WHITE).shift(gradient_descent.get_bottom() + DOWN * 0.5)
        bias_weigh = MathTex(r"w_{0}=1,b_{0}=1").shift(iteration.get_bottom() + DOWN * 0.5)
        weigh = MathTex(r"w_{m}=w_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)x_{i}").shift(bias_weigh.get_bottom() + DOWN * 0.5)
        bias = MathTex(r"b_{m}=b_{m-1}+\alpha\displaystyle\sum\limits_{i=0}^n (y_{i}-\sigma)").shift(weigh.get_bottom() + DOWN * 0.5)
        optimal_values = MathTex(r"\text{Optimal Values }:w_{m},b_{m}\text{    Decsion Boundary: }b_{m}+w_{m}x=0").shift(DOWN * 3.5 + LEFT * 2)
        learning_rate = MathTex(r"\alpha=:\text{ Learning Rate}").shift(UP * 1.2 + RIGHT * 3)
        number_of_training = MathTex(r"n=:\text{ Number of training Samples}").shift(learning_rate.get_bottom()+ DOWN * 0.5)
        xiyi = MathTex(r"(x_{i},y_{i}):\text{ Training sample i (feature, label)}").shift(number_of_training.get_bottom()+ DOWN * 0.5)
        sigmoid_Function = MathTex(r"\sigma= \text{ Sigmoid Function}").shift(xiyi.get_bottom()+ DOWN * 0.5)

        
        self.play(Write(Title))
        self.wait(2)
        self.play(Write(question))
        self.wait(2)
        self.play(Write(gradient_descent))
        self.wait(2)
        self.play(Write(VGroup(iteration, bias_weigh, weigh, bias)), run_time= 2)
        self.wait(2)
        self.play(Write(optimal_values))
        self.wait(2)
        self.play(Write(VGroup(learning_rate, number_of_training, xiyi, sigmoid_Function)))
        self.wait(2)
        self.play(FadeOut(VGroup(Title, question, gradient_descent, iteration, bias_weigh, weigh, bias, optimal_values, learning_rate, number_of_training, xiyi, sigmoid_Function)))
        self.wait()
