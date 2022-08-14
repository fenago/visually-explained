from manim import *
from numpy import e

class sigmoid(ThreeDScene):
    def construct(self):
        Title = Text("Training Phase", color= ORANGE).to_edge(UL)
        number_line = NumberLine()
        
        Dot.set_default(color= BLUE)
        dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12, dot13, dot14, dot15, dot16, dot17, dot18 = Dot(number_line.n2p(-6)), Dot(number_line.n2p(-5.8)), Dot(number_line.n2p(-5.5)), Dot(number_line.n2p(-5.2)), Dot(number_line.n2p(-4.9)), Dot(number_line.n2p(-4.4)), Dot(number_line.n2p(-4.1)), Dot(number_line.n2p(-3.3)), Dot(number_line.n2p(-3)), Dot(number_line.n2p(-2.8)), Dot(number_line.n2p(-2.3)), Dot(number_line.n2p(-2)), Dot(number_line.n2p(-1.7)), Dot(number_line.n2p(-1)), Dot(number_line.n2p(0)), Dot(number_line.n2p(0.5)), Dot(number_line.n2p(1)), Dot(number_line.n2p(2))
        dots_blue = VGroup(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12, dot13, dot14, dot15, dot16, dot17, dot18)
        
        Dot.set_default(color= RED)
        dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12, dot13, dot14, dot15, dot16, dot17, dot18 = Dot(number_line.n2p(6)), Dot(number_line.n2p(5.8)), Dot(number_line.n2p(5.5)), Dot(number_line.n2p(5.2)), Dot(number_line.n2p(4.9)), Dot(number_line.n2p(4.4)), Dot(number_line.n2p(4.1)), Dot(number_line.n2p(3.3)), Dot(number_line.n2p(3)), Dot(number_line.n2p(2.8)), Dot(number_line.n2p(2.3)), Dot(number_line.n2p(2)), Dot(number_line.n2p(1.7)), Dot(number_line.n2p(1)), Dot(number_line.n2p(-0.4)), Dot(number_line.n2p(-0.5)), Dot(number_line.n2p(-1)), Dot(number_line.n2p(-2))
        dots_red = VGroup(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12, dot13, dot14, dot15, dot16, dot17, dot18)
        

        Text.set_default(font_size= 20, color= YELLOW)
        MathTex.set_default(font_size= 25, color= YELLOW)
        #Iterations
        iteration = Text("Iteration: ").shift(DOWN * 1 + LEFT * 4)
        iteration_valuetracker = ValueTracker(0)
        iteration_value = always_redraw(lambda: DecimalNumber(num_decimal_places= 0,color= YELLOW, font_size= 25).shift(iteration.get_right() + RIGHT * 0.5).set_value(iteration_valuetracker.get_value()))


        #Learing rate
        learning_rate = MathTex(r"\alpha= 0.01").shift(iteration.get_bottom() + DOWN * 0.4)
        
        #Decision Boundary
        decision_boundary = MathTex(r"\text{Decision Boundary: }x=-\frac{b}{w}").shift(DOWN * 1.5 + RIGHT * 3.4)

        #Dot and a small line
        dot = Dot(number_line.n2p(-1), color= YELLOW)
        line = Line(start= dot.get_top() + UP * 0.1, end= dot.get_bottom() + DOWN * 0.1, color= YELLOW)
        pointer = VGroup(dot, line)

        self.add(number_line, dots_blue, dots_red, iteration, iteration_value, learning_rate, decision_boundary, pointer)
        self.wait(2)
        self.play(iteration_valuetracker.animate.set_value(1))
        self.wait(1)
        self.play(AnimationGroup(pointer.animate.shift(RIGHT * 0.1), iteration_valuetracker.animate.set_value(2), run_time= 2))
        self.wait(2)
        self.play(AnimationGroup(pointer.animate.shift(RIGHT * 0.1), iteration_valuetracker.animate.set_value(3), run_time= 2))
        self.wait(2)
        self.play(AnimationGroup(pointer.animate.shift(RIGHT * 1.4), iteration_valuetracker.animate.set_value(100), run_time= 6))
        self.wait(2)
        self.play(FadeOut(pointer))
        pointer.shift(LEFT * 1.1)

        number_plane = NumberPlane(
            background_line_style={
                "stroke_width": 4,
                "stroke_opacity": 0.4
            })

        sigmoid_function = number_plane.plot(lambda x: 1 / (1 + np.e**(-x)), color= ORANGE)
        dot = Dot(number_plane.c2p(-0.5,1/ ( 1 + e**(0.5)))).scale(0)
        horizantal_line = always_redraw(lambda: number_plane.get_horizontal_line(dot.get_center()))
        vertical_line = always_redraw(lambda: number_plane.get_vertical_line(number_plane.c2p(0.67+0.5,1/(1+np.e**0.67)+0.1)))
        vertical_line_text = Text("0.67", font_size= 20).shift(vertical_line.get_top() + UP * 0.2)
        probability = Text("Probability of sample belonging to positive class > 50% threshold", font_size= 25).shift(DOWN * 1.5)
        
        self.play(ReplacementTransform(number_line, number_plane), run_time= 2)
        self.play(FadeOut(iteration_value))
        self.set_camera_orientation(zoom= 1.4, run_time= 2)
        self.play(Create(VGroup(sigmoid_function, pointer)), run_time= 1)
        self.wait(2)
        self.play(Create(horizantal_line))
        self.wait(2)
        self.play(AnimationGroup(sigmoid_function.animate.shift(RIGHT * 1.5), pointer.animate.shift(RIGHT * 1.5), dot.animate.shift(RIGHT * 1.5)), run_time= 4)
        self.wait(2)
        self.play(Create(vertical_line))
        self.wait(2)
        self.play(Write(vertical_line_text), run_time= 2)
        self.wait(2)
        self.play(FadeOut(VGroup(iteration, iteration_value, learning_rate, decision_boundary)))
        self.wait(2)
        self.set_camera_orientation(zoom= 1, run_time= 2)
        self.play(Write(probability))
        self.wait(2)
        self.play(FadeOut(VGroup(number_plane, sigmoid_function, pointer, horizantal_line, vertical_line, vertical_line_text, probability, dots_blue, dots_red)))
        self.wait(2)



        #<------------------------------->
        Text.set_default(font_size= 20, color= YELLOW)
        MathTex.set_default(font_size= 25, color= YELLOW)
        Title = Text("2 Dimensional Decision Boundary", color= WHITE).to_edge(UP)
        sigmoid_function_text = MathTex(r"\sigma(x)=\frac{1}{1+e^{-x}}\text{    Sigmoid Function}").shift(Title.get_bottom() + DOWN * 0.5)
        step1 = MathTex(r"\sigma(b+wx)=\frac{1}{1+e^{-(b+wx)}}\text{    One Dimensional Sigmoid}").shift(sigmoid_function_text.get_bottom() + DOWN * 0.5)
        step2 = MathTex(r"\sigma(b+w_{1}x_{1}+w_{2}x_{2})=\frac{1}{1+e^{-(w_{1}x_{1}+w_{2}x_{2})}}\text{    Two Dimensional Sigmoid}").shift(step1.get_bottom() + DOWN * 0.5)
        threshold = MathTex(r"\text{Assuming the threshold of 0.5: } \sigma (b+w_{1}x_{1}+w_{2}x_{2})", color= WHITE).shift(step2.get_bottom() + DOWN * 0.5 + LEFT * 4)
        step3 = MathTex(r"0.5=\frac{1}{1+e^{-(b+w_{1}x_{1}+w_{2}x_{2})}}").shift(threshold.get_bottom() + DOWN * 0.5)
        step4 = MathTex(r"0.5+0.5e^{-(b+w_{1}x_{1}+w_{2}x_{2})}=1").shift(step3.get_bottom() + DOWN * 0.5)
        step5 = MathTex(r"1+e^{-(b+w_{1}x_{1}+w_{2}x_{2})}=2").shift(step4.get_bottom() + DOWN * 0.5)
        step6 = MathTex(r"e^{-(b+w_{1}x_{1}+w_{2}x_{2})}=2-1").shift(threshold.get_bottom() + DOWN * 0.5 + RIGHT * 4.5)
        step7 = MathTex(r"-(b+w_{1}x_{1}+w_{2}x_{2})=log(2-1)").shift(step6.get_bottom() + DOWN * 0.5)
        step8 = MathTex("b+w_{1}x_{1}+w_{2}x_{2}=0").shift(step7.get_bottom() + DOWN * 0.5)
        line_decision_boundary = Text("Line decision boundary", font_size= 20).shift(step8.get_right() + RIGHT * 2.5)
        arrow = Line(start= line_decision_boundary.get_left() , end= step8.get_right()).add_tip(tip_length= 0.08)
        equation_values = MathTex(r"P(y=1|b+w_{1}x_{1}+w_{2}x_{2}=0.5)").shift(step6.get_right() + RIGHT * 2.5)



        self.play(Create(Title))
        self.wait(2)
        self.play(Create(sigmoid_function_text))
        self.wait(2)
        self.play(Create(VGroup(step1, step2)))
        self.wait(2)
        self.play(Create(threshold))
        self.wait(2)
        self.play(Create(VGroup(step3, step4, step5)))
        self.wait(2)
        self.play(Create(VGroup(step6, step7, step8)))
        self.wait(2)
        self.play(Create(VGroup(line_decision_boundary, arrow)))
        self.wait(2)
        self.play(Write(equation_values))
        self.wait(2)

        self.play(FadeOut(VGroup(Title, sigmoid_function_text, step1, step2, threshold, step3, step4, step5, step6, step7, step8, line_decision_boundary, arrow, equation_values)))
